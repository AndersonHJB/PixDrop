import os
import pyperclip
from flask import url_for


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def generate_links(filename):
    url = url_for('uploaded_file', filename=filename, _external=True)
    html = f'<img src="{url}" alt="{filename}">'
    markdown = f'![{filename}]({url})'
    return url, html, markdown


def copy_to_clipboard(text):
    pyperclip.copy(text)
