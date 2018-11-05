from flask import jsonify, current_app, request, url_for, g
from todoism.apis.v1 import api_v1
from todoism.apis.v1.errors import api_abort
from todoism.models import User, Category
from todoism.extensions import db
from todoism.apis.v1.auth import generate_token, auth_required
from todoism.apis.v1.errors import validation_error
from todoism.apis.v1.schemas import category_schema, categorise_schema
from flask.views import MethodView


def get_body_item():
    data = request.get_json()
    body = data.get('body')
    if body is None or str(body).strip() == '':
        raise validation_error('The item body is empty or invalid.')
    return body


class IndexAPI(MethodView):
    def get(self):
        return jsonify({
            "api_version": "1.0",
            "api_base_url": "http://localhost:5000/api/v1",
            "authentication_url": "http://localhost:5000/api/v1/token",
        })


class AuthTokenAPI(MethodView):
    def post(self):
        grant_type = request.form.get('grant_type')
        username = request.form.get('username')
        password = request.form.get('password')

        if grant_type is None or grant_type.lower() != 'password':
            return api_abort(code=400, message='The grant_type must be password')

        user = User.query.filter_by(username=username).first()
        if user is None or not user.validate_password(password):
            return api_abort(code=400, message='Either the username or password was invalid.')
        token, expiration = generate_token(user)

        response = jsonify({
            'access_token': token,
            'token_type': 'Bearer',
            'expires_in': expiration
        })
        response.status_code = 200
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Pragma'] = 'no-cache'
        return response


class CategoryAPI(MethodView):
    def get(self, category_id):
        category = Category.query.get_or_404(category_id)
        if g.current_user != category.author:
            return api_abort(403)
        return jsonify(category_schema(category))


class CategoriseAPI(MethodView):
    # todo
    # decorators = [auth_required]

    def get(self):
        categorise = Category.query.all()
        return jsonify(categorise_schema(categorise))

    def post(self):
        name = request.data.name
        author = g.current_user
        category = Category(name=name, author=author)
        db.session.add(category)
        db.session.commit()
        response = jsonify(category_schema(category))
        response.status_code = 201
        response.headers['Location'] = url_for('.category', category_id=category.id, _external=True)
        return response


api_v1.add_url_rule('/', view_func=IndexAPI.as_view('index'), methods=['GET'])
api_v1.add_url_rule('/oauth/token', view_func=AuthTokenAPI.as_view('token'), methods=['POST'])
api_v1.add_url_rule('/user/categorise', view_func=CategoriseAPI.as_view('categorise'), methods=['GET', 'POST'])
api_v1.add_url_rule('/user/category/<int:category_id>', view_func=CategoryAPI.as_view('category'),
                    methods=['GET', 'POST', 'DELETE', 'PATCH'])




