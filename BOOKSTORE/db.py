import sqlite3
from config import DB_FILE

# ---------------------- Add Book ----------------------
def add_book(title, description, price, pdf_file, image_file):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO books (title, description, price, pdf_file, image_file) VALUES (?, ?, ?, ?, ?)",
              (title, description, price, pdf_file, image_file))
    conn.commit()
    conn.close()

# ---------------------- Get All Books ----------------------
def get_books():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    conn.close()
    return books

# ---------------------- Clear All (optional) ----------------------
def clear_books():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM books")
    conn.commit()
    conn.close()
