import sqlite3

conn = sqlite3.connect("books.db")
c = conn.cursor()

# Naye columns add karo agar pehle se na ho
try:
    c.execute("ALTER TABLE books ADD COLUMN pdf_file TEXT;")
except:
    print("Column pdf_file already exists")

try:
    c.execute("ALTER TABLE books ADD COLUMN image_file TEXT;")
except:
    print("Column image_file already exists")

conn.commit()
conn.close()

print("Database upgraded ✅")
