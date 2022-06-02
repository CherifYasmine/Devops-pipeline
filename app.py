import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from create_db import create_db_table
from user import delete_user, insert_user, get_users, get_user_by_id, update_user
from utils.utils import generate_response
create_db_table('database.db')
def create_app(name):
    app = Flask(name)
    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.route('/api/users', methods=['GET'])
    def api_get_users():
        return jsonify(get_users())

    @app.route('/api/users/<user_id>', methods=['GET'])
    def api_get_user(user_id):
        return (get_user_by_id(user_id))

    @app.route('/api/users/add',  methods = ['POST'])
    def api_add_user():
        user = request.get_json()
        if not user:
            return generate_response(400, 'Invalid payload.')
        return (insert_user(user))

    @app.route('/api/users/update',  methods = ['PUT'])
    def api_update_user():
        user = request.get_json()
        if not user:
            return generate_response(400, 'Invalid payload.')
        return (update_user(user))

    @app.route('/api/users/delete/<user_id>',  methods = ['DELETE'])
    def api_delete_user(user_id):
        return (delete_user(user_id))
    return app

if __name__ == "__main__":
        app = create_app(__name__)
        app.run()