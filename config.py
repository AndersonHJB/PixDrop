import os

class Config:
    SECRET_KEY = os.urandom(24)
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    @staticmethod
    def init_app(app):
        pass
