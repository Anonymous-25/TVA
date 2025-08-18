import sqlite3
from config import DB_FILE

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL,
                    pdf_file TEXT,
                    img_file TEXT
                )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("✅ Database initialized")
