import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import csv

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def updateBank(): #Updates book list from csv
    #Initialization of Book list
    f = open("books.csv")
    reader = csv.reader(f)
    print("Adding by isbn, title, author and year... ")
    for isbn, title, author, year in reader:
        #debug msg = f"{isbn} of {title} written by {author} in {year} has been recorded! "
        if (year!="year"):
            db.execute("INSERT INTO bookBank(isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                {"isbn" : isbn, "title" : title, "author" : author, "year" : int(float(year))})
            print(f"isbn: {isbn} title: {title} author: {author} year: {year}")
    db.commit()
    print("Book Bank updated! Yay! ")

if __name__ == '__main__':
    updateBank()