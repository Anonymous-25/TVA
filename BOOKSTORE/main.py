import streamlit as st
import sqlite3
# Inject SVG before sidebar navigation
import streamlit as st
import sqlite3


st.set_page_config(layout="wide")

from upgrade_db import init_db, get_books, add_book, delete_book

# ✅ App ke start me table create ho jaye
init_db()

import sqlite3
import streamlit as st
import base64

def search():
    # Connect to your database
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    # Fetch book titles from the database
    cursor.execute("SELECT title FROM books")
    book_titles = [row[0] for row in cursor.fetchall()]  # List of book titles

    conn.close()
    return book_titles

book_list = search()
print(book_list)
# Example data
search_items = [
    "Search your book here....",
    # Major Branches
    "Physics", "Chemistry", "Biology", "Mathematics", "Computer Science", "Astronomy",
    "Geology", "Environmental Science", "Engineering", "Medicine",

    # Physics Topics
    "Classical Mechanics", "Quantum Mechanics", "Thermodynamics", "Electromagnetism",
    "Optics", "Nuclear Physics", "Relativity", "Astrophysics",

    # Chemistry Topics
    "Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry", "Analytical Chemistry",
    "Biochemistry", "Industrial Chemistry",

    # Biology Topics
    "Genetics", "Microbiology", "Botany", "Zoology", "Evolutionary Biology",
    "Molecular Biology", "Neuroscience",

    # Mathematics Topics
    "Algebra", "Calculus", "Geometry", "Statistics", "Probability", "Linear Algebra",
    "Discrete Mathematics", "Number Theory", "Applied Mathematics",

    # Computer Science Topics
    "Programming", "Data Structures", "Algorithms", "Artificial Intelligence",
    "Machine Learning", "Databases", "Networking", "Cybersecurity",

    # Astronomy & Space Science
    "Cosmology", "Planetary Science", "Stellar Physics", "Exoplanets",

    # Engineering Fields
    "Mechanical Engineering", "Electrical Engineering", "Civil Engineering",
    "Chemical Engineering", "Software Engineering", "Biomedical Engineering",

    # Medicine & Health Science
    "Anatomy", "Physiology", "Pathology", "Pharmacology", "Public Health",

    # Environmental Science Topics
    "Climate Change", "Ecology", "Sustainability", "Renewable Energy",

    # Popular & Reference
    "Best Sellers", "Reference Books", "Lab Manuals", "Research Papers",
    "Textbooks", "Study Guides"
]

# --- TOPBAR STYLING ---
st.markdown("""
    <style>
    .topbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: #1E1E1E;
        color: white;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 8px 20px;
        z-index: 1000;
        border-bottom: 1px solid #333;
    }
    .topbar h2 {
        margin: 0;
        font-size: 18px;
        color: #00ADB5;
        flex: 1;
    }
    .block-container {
        padding-top: 80px !important; /* content niche push */
    }
    </style>
""", unsafe_allow_html=True)

# --- TOPBAR ---
col1, col2 = st.columns([1,3])
with col1:
    st.title("Tech-Verse Athenaeum")

with col2:
    query = st.selectbox("🔍 Search here...",
                         options=[""] + search_items + book_list,
                         index=1,placeholder="🔍 Search here...")

# --- SHOW RESULTS ---
if query:
    print(query)

    if st.button("Go"):
        # Store selection in session_state
        st.session_state['selected_book'] = query
        # Redirect to second page
        st.experimental_set_query_params(page="details")

st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"]::before {
        content: '';
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 20px;
        height: 80px;
        width: 140px;
        background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='77 65 361 161'><g fill='none' fill-rule='evenodd'><path d='M125 65h51v161h-51z' fill='%23e23324'/><path d='M282.236 65H341l-37.536 73.252L258.5 226l-29.607-57.779z' fill='%23931c1f'/><path d='M176 65h82.978l44.486 73.252L258.5 226l-29.607-57.779z' fill='%23e23324'/><path d='M331.764 226H273l37.536-73.252L355.5 65l29.607 57.779z' fill='%23931c1f'/><path d='M438 226h-82.978l-44.486-73.252L355.5 65l29.607 57.779zM77 65h48l-48 65z' fill='%23e23324'/></g></svg>") no-repeat center;
        background-size: contain;
    }
    </style>
    """,
    unsafe_allow_html=True
)

import streamlit as st
from streamlit_carousel import carousel

st.set_page_config(layout="wide")
items = [
    {
        "title": "Mountains",
        "text": "Beautiful mountain view",
        "img": "https://picsum.photos/id/1018/800/400",
        "link": ""  # Optional
    },
    {
        "title": "Forest",
        "text": "Green lush forest",
        "img": "https://picsum.photos/id/1015/800/400",
        "link": ""
    },
    {
        "title": "River",
        "text": "Peaceful river flow",
        "img": "https://picsum.photos/id/1019/800/400",
        "link": ""
    }
]

# No "height" parameter — only width works
carousel(items, width=800)



# --- INTRO SECTION ---
st.title("Tech-Verse Athenaeum")
st.subheader("Explore Sci-Fi books and educational content")

st.write(
    "Welcome to Tech-Verse Athenaeum — your ultimate hub for sci-fi adventures and educational knowledge. "
    "Dive into futuristic worlds, explore scientific concepts, and expand your imagination and learning."
)

# Optional: Display an image/banner

st.write("---")  # Divider

# --- FEATURES SECTION ---
st.header("Features")

features = [
    "📚 Extensive Sci-Fi Library: Explore hundreds of science fiction books and stories.",
    "🎓 Educational Content: Learn physics, coding, AI, space science, and more.",
    "🔍 Search & Filter: Easily find books or topics of your interest.",
    "💡 Author Insights: Get summaries, reviews, and key concepts from books.",
    "📖 Reading Tracker: Keep track of your reading progress and notes.",
    "🌐 Accessible Anywhere: Works on web, tablet, or mobile devices.",
    "⚡ User-Friendly Interface: Intuitive and responsive design for a smooth experience."
]

# Display features in two columns
cols = st.columns(2)
for i, feature in enumerate(features):
    cols[i % 2].write(feature)

st.write("---")  # Divider

# --- CALL TO ACTION ---
st.subheader("Start your journey into knowledge and imagination today!")



science_books = [
    "Enter book type here....",
    # Major Branches
    "Physics", "Chemistry", "Biology", "Mathematics", "Computer Science", "Astronomy",
    "Geology", "Environmental Science", "Engineering", "Medicine",

    # Physics Topics
    "Classical Mechanics", "Quantum Mechanics", "Thermodynamics", "Electromagnetism",
    "Optics", "Nuclear Physics", "Relativity", "Astrophysics",

    # Chemistry Topics
    "Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry", "Analytical Chemistry",
    "Biochemistry", "Industrial Chemistry",

    # Biology Topics
    "Genetics", "Microbiology", "Botany", "Zoology", "Evolutionary Biology",
    "Molecular Biology", "Neuroscience",

    # Mathematics Topics
    "Algebra", "Calculus", "Geometry", "Statistics", "Probability", "Linear Algebra",
    "Discrete Mathematics", "Number Theory", "Applied Mathematics",

    # Computer Science Topics
    "Programming", "Data Structures", "Algorithms", "Artificial Intelligence",
    "Machine Learning", "Databases", "Networking", "Cybersecurity",

    # Astronomy & Space Science
    "Cosmology", "Planetary Science", "Stellar Physics", "Exoplanets",

    # Engineering Fields
    "Mechanical Engineering", "Electrical Engineering", "Civil Engineering",
    "Chemical Engineering", "Software Engineering", "Biomedical Engineering",

    # Medicine & Health Science
    "Anatomy", "Physiology", "Pathology", "Pharmacology", "Public Health",

    # Environmental Science Topics
    "Climate Change", "Ecology", "Sustainability", "Renewable Energy",

    # Popular & Reference
    "Best Sellers", "Reference Books", "Lab Manuals", "Research Papers",
    "Textbooks", "Study Guides"
]

import streamlit as st
import sqlite3
import os
import base64
import random

# Directories
UPLOAD_IMG = "books-img"
UPLOAD_PDF = "books"

os.makedirs(UPLOAD_IMG, exist_ok=True)
os.makedirs(UPLOAD_PDF, exist_ok=True)

# ==========================
# Database Functions
# ==========================
def init_db():
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            price REAL,
            pdf_file TEXT,
            image_file TEXT
        )
    """)
    conn.commit()
    conn.close()
init_db()

def add_book(title, description, price, pdf_file, image_file):
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    c.execute("INSERT INTO books (title, description, price, pdf_file, image_file) VALUES (?, ?, ?, ?, ?)",
              (title, description, price, pdf_file, image_file))
    conn.commit()
    conn.close()


def get_books():
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    c.execute("SELECT * FROM books ORDER BY id DESC")
    books = c.fetchall()
    conn.close()
    return books


def delete_book(book_id):
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()


# ==========================
# Utility Functions
# ==========================
def generate_captcha():
    return str(random.randint(1000, 9999))


def check_password(username, password, captcha, captcha_input):
    return username == "admin" and password == "password123" and captcha == captcha_input


# ==========================
# Store Page
# ==========================
def show_store():
    books = get_books()
    st.header("📚 Book Store")

    if not books:
        st.info("No books available yet.")
        return

    cols = st.columns(4)  # 4 cards in one row
    for i, book in enumerate(books):
        with cols[i % 4]:
            pdf_path = os.path.join(UPLOAD_PDF, str(book[7])) if book[7] else None
            img_path = os.path.join(UPLOAD_IMG, str(book[8])) if book[8] else None

            if img_path and os.path.exists(img_path):   # ✅ fixed
                st.image(img_path, width=150)
            else:
                st.image("https://www.shutterstock.com/image-vector/picture-vector-icon-no-image-260nw-1732584341.jpg", width=150)

            description = book[3]

            st.markdown(book[1])
            st.caption(description)
            # st.write(f"💲 {book[4]}")
            # st.write(f"💲 {book[2]}")

            if pdf_path and os.path.exists(pdf_path):
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label="📥 Download PDF",
                        data=pdf_file,
                        file_name=os.path.basename(pdf_path),
                        mime="application/pdf",
                        key=f"download_{book[0]}"
                    )
            else:
                st.button("Not Available", disabled=True, key=f"notavail_{book[0]}")

# ==========================
# Admin Panel
# ==========================
# def admin_panel():
#     st.subheader("🔐 Admin Panel - Manage Books")
#
#     # Upload form
#     with st.form("upload_form", clear_on_submit=True):
#         title = st.text_input("Book Title")
#         type = st.selectbox("Type",
#                              options=[""] + science_books,
#                              index=1, placeholder="Enter Book Type here......")
#         description = st.text_area("Description")
#         price = st.number_input("Price", min_value=0.0, step=1.0)
#         pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
#         img_file = st.file_uploader("Upload Cover Image", type=["jpg", "jpeg", "png"])
#         submit = st.form_submit_button("Add Book")
#
#         if submit:
#             if not title or not description:
#                 st.error("Please fill all details")
#             else:
#                 pdf_filename, img_filename = None, None
#
#                 if pdf_file:
#                     pdf_filename = f"{title.replace(' ', '_')}.pdf"
#                     with open(os.path.join(UPLOAD_PDF, pdf_filename), "wb") as f:
#                         f.write(pdf_file.read())
#
#                 if img_file:
#                     img_filename = f"{title.replace(' ', '_')}.jpg"
#                     with open(os.path.join(UPLOAD_IMG, img_filename), "wb") as f:
#                         f.write(img_file.read())
#
#                 add_book(title, description, price, pdf_filename, img_filename)
#                 st.success(f"Book '{title}' added successfully!")
#
#     # Show database
#     st.subheader("📋 Book Database")
#     books = get_books()
#     if books:
#         for book in books:
#             col1, col2, col3 = st.columns([2, 1, 1])
#             with col1:
#                 st.write(f"**{book[1]}** - {book[2]} (${book[3]})")
#             with col2:
#                 if book[4]:
#                     st.write("📄 PDF")
#                 if book[5]:
#                     st.write("🖼️ Image")
#             with col3:
#                 if st.button("❌ Delete", key=f"del_{book[0]}"):
#                     delete_book(book[0])
#                     st.warning(f"Book '{book[1]}' deleted!")
#                     st.experimental_rerun()
#     else:
#         st.info("No books in database yet.")
#



import streamlit as st
import requests
import base64

# 🔑 GitHub Secrets (automatically load from secrets.toml)
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
GITHUB_REPO = st.secrets["GITHUB_REPO"]
GITHUB_BRANCH = st.secrets["GITHUB_BRANCH"]

def upload_to_github(file, path_in_repo):
    """Upload a file to GitHub repo via API"""
    content = file.getvalue()
    encoded_content = base64.b64encode(content).decode("utf-8")

    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{path_in_repo}"

    response = requests.put(
        url,
        headers={
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        },
        json={
            "message": f"Add {path_in_repo}",
            "content": encoded_content,
            "branch": GITHUB_BRANCH,
        },
    )
    return response

st.title("📚 Bookstore PDF Uploader")

uploaded_file = st.file_uploader("📤 Upload a PDF", type="pdf")

if uploaded_file:
    path_in_repo = f"books/{uploaded_file.name}"  # repo ke andar save path
    response = upload_to_github(uploaded_file, path_in_repo)

    if response.status_code in [200, 201]:
        st.success(f"✅ {uploaded_file.name} uploaded to GitHub repo at `{path_in_repo}`")
    else:
        st.error(f"❌ Upload failed: {response.json()}")

# ==========================
# Main App
# ==========================
def main():
    st.set_page_config(page_title="Bookstore", layout="wide")

    # Session state initialize
    if "admin" not in st.session_state:
        st.session_state["admin"] = False
    if "captcha" not in st.session_state:
        st.session_state["captcha"] = generate_captcha()


    menu = ["Store", "Admin Login", "Admin Panel"]
    choice = st.sidebar.radio("Menu", menu)

    if choice == "Store":
        show_store()

    elif choice == "Admin Login":
        st.subheader("🔑 Admin Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        st.write(f"Captcha: **{st.session_state['captcha']}**")
        captcha_input = st.text_input("Enter Captcha")

        if st.button("Login"):
            if check_password(username, password, st.session_state["captcha"], captcha_input):
                st.session_state["admin"] = True
                st.session_state["captcha"] = generate_captcha()
                st.success("✅ Login Successful!")
            else:
                st.error("❌ Invalid credentials or captcha")

    elif choice == "Admin Panel":
        if st.session_state["admin"]:
            admin_panel()
        else:
            st.warning("Please login as admin first.")


if __name__ == "__main__":
    init_db()
    main()




