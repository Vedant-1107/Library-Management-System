# Library Management System

  This is a Python-based Library Management System that provides functionalities to manage books, users, and transactions (issuing and returning books). It uses MySQL for database management and allows users to perform various library operations via a command-line interface.

## Features

### <1.> Add Books: 
  
  Add new books to the library with their title, author, and quantity.

### <2.> Add Users:
  
  Add library users with their name and email.

### <3.> Issue Books:

  Issue books to users and update their availability.

### <4.> Return Books:

  Record the return of books and update their availability.

### <5.> View Records:

  Display all books, users, and transaction records.

## Usage Instructions

### <1.> Add a Book:
  Enter the book's title, author, and quantity when prompted.

### <2.> Add a User:
  Enter the user's name and email.

### <3.> Issue a Book:
  Provide the user ID and book ID to issue a book.

### <4.> Return a Book:
  Provide the transaction ID to mark a book as returned.

### <5.> View Records:
  Choose the appropriate option to view books, users, or transaction records.

## Notes

  <1.> The program automatically initializes the database and creates necessary tables.<br>
  <2.> Duplicate email addresses are not allowed when adding users.

## Future Enhancements

  <1.> Add a graphical user interface (GUI) for better user experience.<br>
  <2.> Support for exporting reports in CSV or PDF format.<br>
  <3.> Implement advanced search and filter functionalities for books and users.
