# TODO: add .env
import uuid
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from com.cm.paste.models import Pbuser, Paste
from com.cm.paste.util.util import six_letter_random_str, get_hash_url

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pb:xxx@localhost/pb'
db = SQLAlchemy(app)
db.init_app(app)


def get_user_id(user_name):
    user = Pbuser.query.filter_by(name=user_name).first()
    user_id = user.user_id if user else None
    return user_id


def get_content(content_key):
    return {'content_key': f'data of {content_key}'}


def get_paste_id(paste_id):
    paste = Paste.query.filter_by(url_hash=paste_id).first()
    content_key = paste.content_key if paste else None
    content = get_content(content_key)
    return {'content': content} if content else {'error': 'Content not found'}


def delete_paste_id(paste_id):
    paste = Paste.query.filter_by(url_hash=paste_id).first()
    if paste:
        try:
            current_db_sessions = db.session.object_session(paste)
            current_db_sessions.delete(paste)
            current_db_sessions.commit()
            return True
        except Exception as e:
            app.logger.info(e)
    return False


def save(paste_data, custom_url=None, user_name=None, paste_name=None, expire_date=None):
    paste_id = six_letter_random_str()
    url = get_hash_url(custom_url) if custom_url else get_hash_url(paste_id)
    user_id = get_user_id(user_name=user_name)  # It's OK the user_id is None
    content_key = str(uuid.uuid1())
    try:
        paste = Paste(url_hash=custom_url if custom_url else paste_id, user_id=user_id, content_key=content_key,
                      expired=datetime.utcnow())
        db.session.add(paste)
        db.session.commit()
        return {'url': url}
    except Exception as e:
        app.logger.debug(e)
        return {'error': 'error'}, 400
