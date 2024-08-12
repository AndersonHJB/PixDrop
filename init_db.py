# flask shell
from app import db

db.create_all()
from models import User

admin = User(username='admin')
admin.set_password('admin123')
db.session.add(admin)
db.session.commit()
