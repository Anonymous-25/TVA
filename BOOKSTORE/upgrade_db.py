import sqlite3
import os

DB_PATH = "books.db"  # Repo root me save hoga

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Books table banega agar missing hai
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            type TEXT,
            description TEXT,
            price REAL,
            pdf_filename TEXT,
            img_filename TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_book(title, type, description, price, pdf_filename, img_filename):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO books (title, type, description, price, pdf_filename, img_filename)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (title, type, description, price, pdf_filename, img_filename))
    conn.commit()
    conn.close()

def get_books():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

def delete_book(book_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
