import sqlite3


class Database:

    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, "
                    "ISBN integer)")
        self.conn.commit()

    def insert_table(self,title, author, year, isbn):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def delete_row(self,bookid):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM book where id=?", (bookid,))
        self.conn.commit()

    def view_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * from book")
        rows = cur.fetchall()
        return rows

    def search(self,title="", author="", year="", isbn=""):
        cur = self.conn.cursor()
        cur.execute("SELECT * from book WHERE title=? OR author=? OR year=? OR ISBN=?", (title, author, year, isbn))
        rows = cur.fetchall()
        return rows

    def update_row(self,bookid, title, author, year, isbn):
        cur = self.conn.cursor()
        cur.execute("UPDATE book SET title=?,author=?,year=?,ISBN=? WHERE id=?", (title, author, year, isbn, bookid))
        self.conn.commit()

    def __del__(self):
        self.conn.close()