import parser

from flask import Flask
from flask_restful import reqparse, Resource, Api
from flask_sqlalchemy import SQLAlchemy

from com.cm.paste.util.db.db import delete_paste_id, get_paste_id, save

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('api_dev_key', type=str, location='headers')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pb:xxx@localhost/pb'
db = SQLAlchemy(app)
db.init_app(app)


class App(Resource):
    def post(self):
        parser.add_argument('paste_data', type=str, location='json')
        parser.add_argument('custom_url', type=str, location='json')
        parser.add_argument('user_name', type=str, location='json')
        parser.add_argument('paste_name', type=str, location='json')
        parser.add_argument('expire_date', type=str, location='json')
        args = parser.parse_args()
        if auth(args['api_dev_key']):
            try:
                return save(args['paste_data'], args['custom_url'], args['user_name'], args['paste_name'],
                            args['expire_date'])
            except Exception as e:
                app.logger.debug(e)
                return {'error': 'Some error'}
        else:
            return {'error': 'auth error'}

    def get(self, paste_id):
        args = parser.parse_args()
        if auth(args['api_dev_key']):
            return get_paste_id(paste_id)
        else:
            return {'error': 'auth error'}

    def delete(self, paste_id):
        args = parser.parse_args()
        if auth(args['api_dev_key']):
            if delete_paste_id(paste_id):
                return None, 204
        else:
            return {'error': 'auth error'}


api.add_resource(App, '/v1/paste', '/v1/paste/<string:paste_id>', endpoint='paste')


def auth(api_dev_key):
    return True


if __name__ == '__main__':
    app.run()
