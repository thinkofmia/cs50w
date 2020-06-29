# Project 1: RecoBooks
Web Programming with Python and JavaScript

## Short Write Up
In this project, users with registered accounts are able to make and view reviews of a particular list of books. This gives our users better recommendations to the books available now, and is also includes additional data from the GoodReads as well.

In the folder 'static' is the place where the css and scss files are held.

In the folder 'templates' is the place where the html files are held.
- 'book.html' refers to the html page when the user views a particular book
- 'home.html' refers to the html page when the user accesses the home page or by clicking the logo
- 'index.html' refers to the html base template for all the other pages
- 'login.html' refers to the html page where the user is to be logined
- 'register.html' refers to the html page where the user is registering a new account
- 'search.html' refers to the html page where the user is asked to provide a search query for books
- 'searchResults.html' refers to the html page where the results of the user's search query is displayed

'application.py' is the main python app running the entire project
'import.py' is the python file that imports the data from 'books.csv' over to our database

Youtube Link: https://youtu.be/gAxfzXxtEUY

## Requirements
[x] Registration: Users should be able to register for your website, providing (at minimum) a username and password.

[x] Login: Users, once registered, should be able to log in to your website with their username and password.

[x] Logout: Logged in users should be able to log out of the site.

[x] Import: Provided for you in this project is a file called books.csv, which is a spreadsheet in CSV format of 5000 different books. Each one has an ISBN number, a title, an author, and a publication year. In a Python file called import.py separate from your web application, write a program that will take the books and import them into your PostgreSQL database. You will first need to decide what table(s) to create, what columns those tables should have, and how they should relate to one another. Run this program by running python3 import.py to import the books into your database, and submit this program with the rest of your project code.

[x] Search: Once a user has logged in, they should be taken to a page where they can search for a book. Users should be able to type in the ISBN number of a book, the title of a book, or the author of a book. After performing the search, your website should display a list of possible matching results, or some sort of message if there were no matches. If the user typed in only part of a title, ISBN, or author name, your search page should find matches for those as well!

[x] Book Page: When users click on a book from the results of the search page, they should be taken to a book page, with details about the book: its title, author, publication year, ISBN number, and any reviews that users have left for the book on your website.

[x] Review Submission: On the book page, users should be able to submit a review: consisting of a rating on a scale of 1 to 5, as well as a text component to the review where the user can write their opinion about a book. Users should not be able to submit multiple reviews for the same book.

[x] Goodreads Review Data: On your book page, you should also display (if available) the average rating and number of ratings the work has received from Goodreads.

[x] API Access: If users make a GET request to your website’s /api/<isbn> route, where <isbn> is an ISBN number, your website should return a JSON response containing the book’s title, author, publication date, ISBN number, review count, and average score. The resulting JSON should follow the format:
{
    "title": "Memory",
    "author": "Doug Lloyd",
    "year": 2015,
    "isbn": "1632168146",
    "review_count": 28,
    "average_score": 5.0
}
If the requested ISBN number isn’t in your database, your website should return a 404 error.

[x] You should be using raw SQL commands (as via SQLAlchemy’s execute method) in order to make database queries. 

[x] You should not use the SQLAlchemy ORM (if familiar with it) for this project.
    
[x] In README.md, include a short writeup describing your project, what’s contained in each file, and (optionally) any other additional information the staff should know about your project.

[x] If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to requirements.txt!