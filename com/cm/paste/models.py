from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pb:xxx@localhost/pb'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Pbuser(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(32), unique=True, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.name}'


class Paste(db.Model):
    url_hash = db.Column(db.String(16), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('pbuser.user_id'), nullable=True)
    content_key = db.Column(db.String(512), unique=True, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    expired = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.url_hash}'

if __name__ == '__main__':
    # TODO: flask db init flask db migrate flask db upgrade https://flask-migrate.readthedocs.io/en/latest/index.html
    db.create_all()

