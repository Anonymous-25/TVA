import base64
import os

UPLOAD_IMG = "uploads/images/"
UPLOAD_PDF = "uploads/pdfs/"

os.makedirs(UPLOAD_IMG, exist_ok=True)
os.makedirs(UPLOAD_PDF, exist_ok=True)

def save_uploaded_file(upload, folder):
    file_path = os.path.join(folder, upload.name)
    with open(file_path, "wb") as f:
        f.write(upload.getbuffer())
    return file_path

def get_img_base64(path):
    if path and os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        return "data:image/jpeg;base64," + base64.b64encode(data).decode()
    return ""
