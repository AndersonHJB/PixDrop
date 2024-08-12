from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from werkzeug.utils import secure_filename
from models import db, User, Image
from utils import allowed_file, generate_links, copy_to_clipboard
import os

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)


@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    images = Image.query.filter_by(user_id=session['user_id']).all()
    return render_template('index.html', images=images)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['username'] = username
            session['user_id'] = user.id
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect(url_for('login'))


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'username' not in session:
        return redirect(url_for('login'))

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    files = request.files.getlist('file')
    links = []

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            image = Image(filename=filename, user_id=session['user_id'])
            db.session.add(image)
            db.session.commit()

            url, html, markdown = generate_links(filename)
            links.append({
                'url': url,
                'html': html,
                'markdown': markdown
            })
            copy_to_clipboard(markdown)

    return render_template('index.html', links=links)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)
