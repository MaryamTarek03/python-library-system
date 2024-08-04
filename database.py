import sqlite3


def create_table():
    connection = sqlite3.connect('library.db')
    c = connection.cursor()

    c.execute('''CREATE TABLE user(
        email text PRIMARY KEY NOT NULL,
        name text,
        number text
    )
    ''')
    connection.commit()
    connection.close()



# USER
def add_user(email, name, number):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('INSERT INTO user(name, email, number) VALUES(?,?,?)', (name, email, number))
    connection.commit()
    connection.close()

def delete_user(email):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('DELETE FROM user WHERE email LIKE ?', (email,))
    connection.commit()
    connection.close()

def update_user(name, email, number):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('UPDATE user SET name = ?, number = ? WHERE email LIKE ?', (name, number, email))
    connection.commit()
    connection.close()

def show_user(search):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute("SELECT name, email, number FROM user WHERE name LIKE ?", (f'%{search}%',))
    users = c.fetchall()
    connection.commit()
    connection.close()
    return users


# BOOK
def add_book(isbn, title, author, genre):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('INSERT INTO book(isbn, title, author, genre) VALUES(?,?,?,?)', (isbn, title, author, genre))
    connection.commit()
    connection.close()

def delete_book(isbn):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('DELETE FROM book WHERE isbn LIKE ?', (isbn,))
    connection.commit()
    connection.close()

def update_book(isbn, title, author, genre):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('UPDATE book SET title = ?, author = ?, genre = ? WHERE isbn LIKE ?', (title, author, genre, isbn))
    connection.commit()
    connection.close()

def show_book(search):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute("SELECT isbn, title, author, genre FROM book WHERE title LIKE ? OR isbn LIKE ? OR author LIKE ? OR genre LIKE ?", (f'%{search}%', f'%{search}%', f'%{search}%',f'%{search}%'))
    books = c.fetchall()
    connection.commit()
    connection.close()
    return books


# LOAN
# def add_loan(loan_id, user_id):
#     connection = sqlite3.connect('library.db')
#     c = connection.cursor()
#     c.execute('INSERT INTO book(isbn, title, author, genre) VALUES(?,?,?,?)', (isbn, title, author, genre))
#     connection.commit()
#     connection.close()

# def delete_book(isbn):
#     connection = sqlite3.connect('library.db')
#     c = connection.cursor()
#     c.execute('DELETE FROM book WHERE isbn LIKE ?', (isbn,))
#     connection.commit()
#     connection.close()

# def update_book(isbn, title, author, genre):
#     connection = sqlite3.connect('library.db')
#     c = connection.cursor()
#     c.execute('UPDATE book SET title = ?, author = ?, genre = ? WHERE isbn LIKE ?', (title, author, genre, isbn))
#     connection.commit()
#     connection.close()

# def show_book(search):
#     connection = sqlite3.connect('library.db')
#     c = connection.cursor()
#     c.execute("SELECT isbn, title, author, genre FROM book WHERE title LIKE ? OR isbn LIKE ? OR author LIKE ? OR genre LIKE ?", (f'%{search}%', f'%{search}%', f'%{search}%',f'%{search}%'))
#     books = c.fetchall()
#     connection.commit()
#     connection.close()
#     return books
