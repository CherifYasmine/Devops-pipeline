from flask import jsonify

def generate_response(code, message, user={}):
    if user != {}:
        return {'code': code, 'message': message, 'user': user}
    return ({'code': code, 'message': message})