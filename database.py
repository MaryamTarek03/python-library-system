import sqlite3


def create_table():
    connection = sqlite3.connect('library.db')
    c = connection.cursor()

    # USER
    # c.execute('DROP TABLE user')
    # c.execute('''CREATE TABLE user(
    #     ssn text PRIMARY KEY NOT NULL,
    #     email text,
    #     name text,
    #     number text
    # )
    # ''')

    # LOAN
    # c.execute('DROP TABLE loan')
    # c.execute('''CREATE TABLE loan(
    #     loan_id TEXT PRIMARY KEY NOT NULL,
    #     user_id TEXT,
    #     book_id TEXT,
    #     issue_date TEXT,
    #     due_date TEXT,
    #     FOREIGN KEY(user_id) REFERENCES user(ssn),
    #     FOREIGN KEY(book_id) REFERENCES book(isbn))
    # ''')
    
    # ADMIN
    # c.execute('DROP TABLE admin')
    # c.execute('''CREATE TABLE admin(
    #     email TEXT PRIMARY KEY NOT NULL,
    #     name TEXT,
    #     password TEXT)
    # ''')
    connection.commit()
    connection.close()

create_table()
# USER
def add_user(ssn, name, email, number):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('INSERT INTO user(ssn, name, email, number) VALUES(?,?,?,?)', (ssn, name, email, number))
    connection.commit()
    connection.close()

user_list = [
    ('30408141401126', 'Maryam Tarek', 'mariamtarek2233@gmail.com', '01203311425'),
    ('3040-8141-40-1126', 'Maryam Tarek', 'mariamtarek2233@gmail.com', '01203311425'),
    ('alyaa-ssn', 'Alyaa Gamal', 'alyaa@gmail.com', '01200000000'),
    ('menna-ssn', 'Menna Hassan', 'menna@gmail.com', '01028248285'),
    ('26.19.164.10', 'Fred Cobb', 'ivatoeze@ca.com', '01069202046'),
    ('215.172.88.195', 'Ethan Gibson', 'lujur@zob.com', '01008499642'),
    ('56.164.200.3', 'Janie Ellis', 'nawga@we.com', '01093598760'),
    ('97.107.101.95', 'Curtis Delgado', 'johize@feldefpu.com', '01086563460'),
    ('6.200.63.210', 'Derek Curtis', 'guk@he.com', '01256350828'),
    ('99.35.193.65', 'Francisco Pope', 'ib@jikoro.com', '01108283761'),
    ('130.228.214.34', 'John Burns', 'ja@cab.com', '01093756056'),
    ('151.26.140.236', 'Leon Cummings', 'wuduli@anaumdu.com', '01065127436'),
    ('141.63.134.83', 'Kyle Byrd', 'ru@gesoca.com', '01006025184'),
]

# for item in user_list:
#     add_user(item[0], item[1], item[2], item[3])

def delete_user(ssn):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('DELETE FROM user WHERE ssn LIKE ?', (ssn,))
    connection.commit()
    connection.close()

# delete_user('30408141401126')

def update_user(ssn, name, email, number):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('UPDATE user SET name = ?, number = ?, email = ? WHERE ssn = ?', (name, number, email, ssn))
    connection.commit()
    connection.close()

# update_user('alyaa-ssn', email='alyaa@gmail.com', name='Alyaa Gamal', number='01207325896')

def show_user(search):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute("SELECT ssn, name, email, number FROM user WHERE name LIKE ? OR ssn LIKE ?", (f'%{search}%',f'%{search}%'))
    users = c.fetchall()
    connection.commit()
    connection.close()
    return users

# print(show_user('ssn'))

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

# ADMIN
def add_admin(name, email, password):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute('INSERT INTO admin(name, email, password) VALUES(?, ?, ?)', (name, email, password))
    books = c.fetchall()
    connection.commit()
    connection.close()

admin_list = [
    ('Alyaa Gamal', 'galyaa@gmail.com', '7454'),
    ('Menna Hassan', 'menna@gmail.com', '1111'),
    ('Maryam Tarek', 'maryam@gmail.com', '1234'),
    ('Wessam Reda', 'wessam@gmail.com', '1234'),
]

# for item in admin_list:
#     add_admin(item[0], item[1], item[2])

def get_admin(search):
    connection = sqlite3.connect('library.db')
    c = connection.cursor()
    c.execute("SELECT email, name, password FROM admin WHERE email LIKE ?", (search,))
    books = c.fetchall()
    connection.commit()
    connection.close()
    return books

def admin_exist(email):
    admin = get_admin(email)
    if admin == []:
        return False
    else: return True

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

