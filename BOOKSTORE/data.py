import streamlit as st

# Inject SVG before sidebar navigation
import streamlit as st

st.set_page_config(layout="wide")

# Example data
search_items = [
    "Search your book here....",
    "Bookstore", "Dashboard", "Users", "Orders",
    "Settings", "Profile", "HelloWorld", "Helpdesk",
    "Books on Python", "Best Sellers", "Order History"
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
                         options=[""] + search_items,
                         index=1,placeholder="🔍 Search here...")

# --- SHOW RESULTS ---
if query:
   print(query)
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






import streamlit as st

st.set_page_config(layout="wide")

# Dummy book data with working image URLs (Unsplash for demo)
books = [
    {"title": "Dune", "price": "$15", "image": "https://images.unsplash.com/photo-1544939631-7a61f2e46aa0?w=500"},
    {"title": "Neuromancer", "price": "$12", "image": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=500"},
    {"title": "Foundation", "price": "$14", "image": "https://images.unsplash.com/photo-1507842217343-583bb7270b66?w=500"},
    {"title": "Snow Crash", "price": "$10", "image": "https://images.unsplash.com/photo-1544717302-de2939b7ef71?w=500"},
    {"title": "Hyperion", "price": "$18", "image": "https://images.unsplash.com/photo-1528209392022-46e91d82f0b2?w=500"},
    {"title": "The Expanse", "price": "$20", "image": "https://images.unsplash.com/photo-1532012197267-da84d127e765?w=500"},
    {"title": "Ender's Game", "price": "$11", "image": "https://images.unsplash.com/photo-1524578271613-d550eacf6090?w=500"},
    {"title": "Ready Player One", "price": "$16", "image": "https://images.unsplash.com/photo-1512820790803-83ca734da794?w=500"},
    {"title": "The Martian", "price": "$13", "image": "https://images.unsplash.com/photo-1495446815901-a7297e633e8d?w=500"},
    {"title": "Brave New World", "price": "$9", "image": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=500"},
    {"title": "Fahrenheit 451", "price": "$8", "image": "https://images.unsplash.com/photo-1496104679561-38d3af2aa394?w=500"},
    {"title": "2001: A Space Odyssey", "price": "$17", "image": "https://images.unsplash.com/photo-1473181488821-2d23949a045a?w=500"},
    {"title": "Dune", "price": "$15", "image": "https://images.unsplash.com/photo-1544939631-7a61f2e46aa0?w=500"},
    {"title": "Neuromancer", "price": "$12",
     "image": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=500"},
    {"title": "Foundation", "price": "$14",
     "image": "https://images.unsplash.com/photo-1507842217343-583bb7270b66?w=500"},
    {"title": "Snow Crash", "price": "$10", "image": "https://images.unsplash.com/photo-1544717302-de2939b7ef71?w=500"},
    {"title": "Hyperion", "price": "$18",
     "image": "https://images.unsplash.com/photo-1528209392022-46e91d82f0b2?w=500"},
    {"title": "The Expanse", "price": "$20",
     "image": "https://images.unsplash.com/photo-1532012197267-da84d127e765?w=500"},
    {"title": "Ender's Game", "price": "$11",
     "image": "https://images.unsplash.com/photo-1524578271613-d550eacf6090?w=500"},
    {"title": "Ready Player One", "price": "$16",
     "image": ""},
    {"title": "The Martian", "price": "$13",
     "image": ""},
    {"title": "Brave New World", "price": "$9",
     "image": ""},
    {"title": "Fahrenheit 451", "price": "$8",
     "image": ""},
    {"title": "2001: A Space Odyssey", "price": "$17",
     "image": ""},

]

# Inject HTML + CSS + JS
st.components.v1.html(f"""
<html>
<head>
<style>
.carousel-container {{
  display: flex;
  align-items: center;
  position: relative;
  width: 100%;
  overflow: hidden;
  margin: 20px 0;
}}
.carousel-track {{
  display: flex;
  transition: transform 0.5s ease;
}}
.carousel-item {{
  min-width: 150px;
  margin: 0 10px;
  text-align: center;
  background: #111;
  color: white;
  border-radius: 10px;
  padding: 10px;
}}
.carousel-item img {{
  width: 150px;
  height: 220px;
  border-radius: 10px;
  object-fit: cover;
}}
.carousel-btn {{
  position: absolute;
  top: 40%;
  transform: translateY(-50%);
  background: rgba(0,0,0,0.6);
  color: white;
  border: none;
  font-size: 24px;
  padding: 10px;
  cursor: pointer;
  border-radius: 50%;
  z-index: 2;
}}
.carousel-btn.left {{ left: 5px; }}
.carousel-btn.right {{ right: 5px; }}
</style>
</head>
<body>

<div class="carousel-container">
  <button class="carousel-btn left" onclick="moveCarousel(-1)">‹</button>
  <div class="carousel-track" id="carousel-track">
    {''.join(f'''
    <div class="carousel-item">
      <img src="{book['image']}" alt="{book['title']}"/>
      <p><b>{book['title']}</b></p>
      <p>{book['price']}</p>
      <button>Buy</button>
    </div>
    ''' for book in books)}
  </div>
  <button class="carousel-btn right" onclick="moveCarousel(1)">›</button>
</div>

<script>
let currentPosition = 0;
const track = document.getElementById("carousel-track");
const itemWidth = 170;  // card + margin
const visibleItems = 8; // show 8 books per row
const totalItems = track.children.length;
const maxScroll = Math.max(0, (totalItems * itemWidth) - (visibleItems * itemWidth));

function moveCarousel(direction) {{
  currentPosition += direction * itemWidth * 1; // scroll 2 cards
  if (currentPosition < 0) currentPosition = 0;
  if (currentPosition > maxScroll) currentPosition = maxScroll;
  track.style.transform = `translateX(-${{currentPosition}}px)`;
}}
</script>

</body>
</html>
""", height=500, scrolling=False)



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
    st.subheader("📚 Book Store")

    if not books:
        st.info("No books available yet.")
        return

    cols = st.columns(4)  # 4 cards in one row
    for i, book in enumerate(books):
        with cols[i % 4]:
            pdf_path = os.path.join(UPLOAD_PDF, str(book[4])) if book[4] else None
            img_path = os.path.join(UPLOAD_IMG, str(book[5])) if book[5] else None

            if img_path and os.path.exists(img_path):   # ✅ fixed
                st.image(img_path, width=150)
            else:
                st.image("https://via.placeholder.com/150x200.png?text=No+Image", width=150)

            st.markdown(f"**{book[1]}**")
            st.caption(book[2])
            st.write(f"💲 {book[3]}")

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
def admin_panel():
    st.subheader("🔐 Admin Panel - Manage Books")

    # Upload form
    with st.form("upload_form", clear_on_submit=True):
        title = st.text_input("Book Title")
        description = st.text_area("Description")
        price = st.number_input("Price", min_value=0.0, step=1.0)
        pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
        img_file = st.file_uploader("Upload Cover Image", type=["jpg", "jpeg", "png"])
        submit = st.form_submit_button("Add Book")

        if submit:
            if not title or not description:
                st.error("Please fill all details")
            else:
                pdf_filename, img_filename = None, None

                if pdf_file:
                    pdf_filename = f"{title.replace(' ', '_')}.pdf"
                    with open(os.path.join(UPLOAD_PDF, pdf_filename), "wb") as f:
                        f.write(pdf_file.read())

                if img_file:
                    img_filename = f"{title.replace(' ', '_')}.jpg"
                    with open(os.path.join(UPLOAD_IMG, img_filename), "wb") as f:
                        f.write(img_file.read())

                add_book(title, description, price, pdf_filename, img_filename)
                st.success(f"Book '{title}' added successfully!")

    # Show database
    st.subheader("📋 Book Database")
    books = get_books()
    if books:
        for book in books:
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                st.write(f"**{book[1]}** - {book[2]} (${book[3]})")
            with col2:
                if book[4]:
                    st.write("📄 PDF")
                if book[5]:
                    st.write("🖼️ Image")
            with col3:
                if st.button("❌ Delete", key=f"del_{book[0]}"):
                    delete_book(book[0])
                    st.warning(f"Book '{book[1]}' deleted!")
                    st.experimental_rerun()
    else:
        st.info("No books in database yet.")


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

    st.title("📖 Sci-Fi & Educational Bookstore")

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












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




import streamlit as st
import sqlite3

# Connect to your database
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Fetch book titles from the database
cursor.execute("SELECT title FROM books")
books = [row[0] for row in cursor.fetchall()]  # List of book titles

conn.close()

# Streamlit selectbox
selected_book = st.selectbox("Select a book:", books)

st.write("You selected:", selected_book)
