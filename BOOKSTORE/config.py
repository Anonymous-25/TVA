import os

# Upload folders
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_PDF = os.path.join(BASE_DIR, "uploads", "pdf")
UPLOAD_IMG = os.path.join(BASE_DIR, "uploads", "img")

# Ensure directories exist
os.makedirs(UPLOAD_PDF, exist_ok=True)
os.makedirs(UPLOAD_IMG, exist_ok=True)

DB_FILE = os.path.join(BASE_DIR, "books.db")
