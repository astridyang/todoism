from flask import jsonify, current_app, request, url_for
from todoism.apis.v1 import api_v1
from todoism.apis.v1.errors import api_abort
from todoism.models import User, Category
from todoism.apis.v1.auth import generate_token, auth_required
from todoism.apis.v1.schemas import category_schema, categorise_schema
from flask.views import MethodView


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
            'expires_in': expiration,
            'code': 200
        })
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Pragma'] = 'no-cache'
        return response


class CategoryAPI(MethodView):
    def get(self, category_id):
        category = Category.query.get_or_404(category_id)
        # todo
        # if g.current_user != category.author:
        #     return api_abort(403)
        return jsonify(category_schema(category))


class CategoriseAPI(MethodView):
    # todo
    decorators = [auth_required]

    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = current_app.config['TODOISM_ITEM_PER_PAGE']
        pagination = Category.query.paginate(page, per_page)
        categorise = pagination.items
        current = url_for('.categorise', page=page, _external=True)
        prev = None
        if pagination.has_prev:
            prev = url_for('.categorise', page=page-1, _external=True)
        next = None
        if pagination.has_next:
            next = url_for('.categorise', page=page+1, _external=True)
        return jsonify(categorise_schema(categorise, current, prev, next, pagination))


api_v1.add_url_rule('/', view_func=IndexAPI.as_view('index'), methods=['GET'])
api_v1.add_url_rule('/oauth/token', view_func=AuthTokenAPI.as_view('token'), methods=['POST'])
api_v1.add_url_rule('/user/categorise', view_func=CategoriseAPI.as_view('categorise'), methods=['GET', 'POST'])
api_v1.add_url_rule('/user/category/<int:category_id>', view_func=CategoryAPI.as_view('category'),
                    methods=['GET', 'POST', 'DELETE', 'PATCH'])




