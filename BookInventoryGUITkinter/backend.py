import sqlite3


def connect():
    conn = sqlite3.connect("bookinventory.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, "
                "ISBN integer)")
    conn.commit()
    conn.close()


def insert_table(title, author, year, isbn):
    conn = sqlite3.connect("bookinventory.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def delete_row(bookid):
    conn = sqlite3.connect("bookinventory.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book where id=?", (bookid,))
    conn.commit()
    conn.close()


def view_all():
    conn = sqlite3.connect("bookinventory.db")
    cur = conn.cursor()
    cur.execute("SELECT * from book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("bookinventory.db")
    cur = conn.cursor()
    cur.execute("SELECT * from book WHERE title=? OR author=? OR year=? OR ISBN=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def update_row(bookid,title,author,year,isbn):
    conn = sqlite3.connect("bookinventory.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,ISBN=? WHERE id=?", (title, author, year,isbn,bookid))
    conn.commit()
    conn.close()


connect()
