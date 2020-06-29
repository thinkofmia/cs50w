import os

from flask import Flask, session, render_template, request, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import csv
import requests

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

username = ""

@app.route("/")
def index(): #Home Page
    #Check if user is still logined
    if 'username' in session:
        username = session['username']
        headline = "Logined as "+session['username']
        session.modified = True
        return render_template("search.html", headline=headline)
    else:#Login/Register page
        username = ""
        headline = "Home Page"
        return render_template("home.html", headline=headline)

@app.route("/api/<string:isbn>", methods=["GET"])
def getAPI(isbn):
    book = db.execute("SELECT title, author, year, isbn, COUNT(reviewBank.reviewid) as review_count, AVG(reviewBank.score) as average_score \
                    FROM bookBank \
                    INNER JOIN reviewBank ON bookBank.isbn = reviewBank.bookid \
                    WHERE isbn = :isbn \
                    GROUP BY title, author, year, isbn",
                    {"isbn": isbn}).fetchone()
    if book: #Shows results
        api_result = dict(book.items())
        api_result['average_score'] = float('%.1f'%(api_result['average_score'])) #Requires this to properly serialize
        return jsonify(api_result)
    else: #return error if results not found
        return jsonify({"Error": "Invalid isbn!! "}), 422

@app.route("/book/<string:title>", methods=["GET","POST"])
def checkBook(title):
    error = ""
    headline = title
    book = db.execute("SELECT * FROM bookbank WHERE title = :book",
                            {"book": title}).fetchone()
    if (request.method=="POST"):
        reviewCheck = db.execute("SELECT * FROM reviewbank WHERE reviewer = :user AND bookid = :bookid",
                            {"user": session['username'], "bookid": book.isbn }).fetchone()
        if reviewCheck:
            error = "You have already submitted a review! "
        else:
            if (request.form.get("score") and request.form.get("review")):
                db.execute("INSERT INTO reviewbank(reviewer, score, review, bookid) VALUES (:username, :score, :review, :bookid)",
                    {"username" : session['username'], "score" : request.form.get("score"), "review" : request.form.get("review"), "bookid": book.isbn })
                db.commit()
                error = "Your review has been submitted! "
            else:
                error = "Fill in the blanks first!! "
    our_reviews = db.execute("SELECT * FROM reviewbank WHERE bookid = :bookID",
                            {"bookID": book.isbn}).fetchall()
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "Cb8VEqqmGbVTLIDk4UNg", "isbns": book.isbn}).json()
    gr_reviews = res['books'][0]
    return render_template("book.html", headline=headline, book=book, ourReviews=our_reviews, goodReadReviews=gr_reviews, errorMsg=error)

@app.route("/search", methods=["GET","POST"])
def search():
    searchQuery = request.form.get("search")
    if request.method == "GET":
        headline = "Please enter into the search box!"
        return render_template("search.html", headline=headline)
    elif (searchQuery==""):
        headline = "Error searching without input. Please try again. "
        return render_template("search.html", headline=headline)
    else:
        headline = "Searching for "+searchQuery
        searchList = db.execute("SELECT * FROM bookbank WHERE isbn LIKE :search OR title LIKE :search OR author LIKE :search",
                            {"search": "%"+searchQuery+"%"}).fetchall()
        if searchList: #If results shows
            return render_template("searchResults.html", headline=headline, search_list=searchList)
        else: 
            headline = "No such book found, please search again. "
            return render_template("search.html", headline=headline)
    
@app.route("/logout")
def logout():
    session.pop("username", None)
    headline = "Successful logout!"
    return render_template("index.html", headline=headline)

@app.route("/welcome/<string:mode>", methods=["GET","POST"])
def welcome(mode): #Login to User Page 
    if request.method == "GET":
        headline = "Please login or register first!"
        return render_template("index.html", headline=headline)
    elif (mode == 'Login'):
        #Set variables of the sent username and password
        requestUser = request.form.get("username")
        requestPassword = request.form.get("password")
        #Save results to database
        accounts = db.execute("SELECT * FROM accounts WHERE username = :username",
                            {"username": requestUser}).fetchone()
        #Check if username exists and password correct
        if (accounts and accounts.passw == requestPassword): #If correct
            session['username'] = requestUser
            username = requestUser
            headline = f"Welcome {session['username']}! Do have a look around"
            session.modified = True
            return render_template("search.html", headline=headline)
        else: #If failed
            headline = "Login Page - Invalid user or password. Please try again"
            return render_template("login.html", headline=headline)

    elif (request.form.get("password")== request.form.get("repw") and mode=='Register'):
        #Save cookie of session id
        session["username"] = request.form.get("username")
        #Save results to database
        db.execute("INSERT INTO accounts(username, passw) VALUES (:username, :password)",
        {"username" : request.form.get("username"), "password" : request.form.get("password")})
        db.commit()
        #Display page
        headline = f"Welcome {session['username']}! Do have a look around"
        session.modified = True
        return render_template("search.html", headline=headline)
    else :
        headline = "Password doesn't match! Register again. "
        return render_template("index.html", headline=headline)
        

@app.route("/login")
def login(): #Login Page
    headline = "Login Page"
    return render_template("login.html", headline=headline)

@app.route("/register")
def register(): #Register Page
    headline = "Register Page"
    return render_template("register.html", headline=headline)