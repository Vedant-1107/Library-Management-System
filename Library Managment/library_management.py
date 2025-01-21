import mysql.connector

# Connect to MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="vedant",  # Replace with your MySQL username
        password="Vedant@1107",  # Replace with your MySQL password
        database="library"  # Replace with your database name
    )

con = connect_to_db()
func = con.cursor()

# Create tables for books, users, and transactions
def initialize_db():
    func.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        quantity INT NOT NULL
    )
    """)

    func.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL
    )
    """)

    func.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        book_id INT NOT NULL,
        issue_date DATE NOT NULL,
        return_date DATE,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (book_id) REFERENCES books(id)
    )
    """)
    con.commit()

# Add a new book
def add_book(title, author, quantity):
    func.execute("INSERT INTO books (title, author, quantity) VALUES (%s, %s, %s)", (title, author, quantity))
    con.commit()
    print(f"Book '{title}' by {author} added successfully!")

# Add a new user
def add_user(name, email):
    try:
        func.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        con.commit()
        print(f"User '{name}' added successfully!")
    except mysql.connector.IntegrityError:
        print("Error: Email already exists.")

# Issue a book to a user
def issue_book(user_id, book_id):
    func.execute("SELECT quantity FROM books WHERE id = %s", (book_id,))
    book = func.fetchone()

    if book and book[0] > 0:
        func.execute("UPDATE books SET quantity = quantity - 1 WHERE id = %s", (book_id,))
        func.execute("INSERT INTO transactions (user_id, book_id, issue_date) VALUES (%s, %s, CURDATE())", (user_id, book_id))
        func.commit()
        print("Book issued successfully!")
    else:
        print("Error: Book is not available.")

# Return a book
def return_book(transaction_id):
    func.execute("SELECT book_id FROM transactions WHERE id = %s AND return_date IS NULL", (transaction_id,))
    transaction = func.fetchone()

    if transaction:
        book_id = transaction[0]
        func.execute("UPDATE books SET quantity = quantity + 1 WHERE id = %s", (book_id,))
        func.execute("UPDATE transactions SET return_date = CURDATE() WHERE id = %s", (transaction_id,))
        con.commit()
        print("Book returned successfully!")
    else:
        print("Error: Invalid transaction ID or book already returned.")

# Display all books
def view_books():
    func.execute("SELECT * FROM books")
    books = func.fetchall()
    print("\nBooks:")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")

# Display all users
def view_users():
    func.execute("SELECT * FROM users")
    users = func.fetchall()
    print("\nUsers:")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

# Display all transactions
def view_transactions():
    func.execute("SELECT * FROM transactions")
    transactions = func.fetchall()
    print("\nTransactions:")
    for transaction in transactions:
        print(f"ID: {transaction[0]}, User ID: {transaction[1]}, Book ID: {transaction[2]}, Issue Date: {transaction[3]}, Return Date: {transaction[4]}")

# Main menu
def main():
    initialize_db()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add User")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View Users")
        print("7. View Transactions")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            quantity = int(input("Enter quantity: "))
            add_book(title, author, quantity)
        elif choice == "2":
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            add_user(name, email)
        elif choice == "3":
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            issue_book(user_id, book_id)
        elif choice == "4":
            transaction_id = int(input("Enter transaction ID: "))
            return_book(transaction_id)
        elif choice == "5":
            view_books()
        elif choice == "6":
            view_users()
        elif choice == "7":
            view_transactions()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Close the database connection when the program ends
con.close()
