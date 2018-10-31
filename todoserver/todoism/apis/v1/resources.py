from flask import jsonify, current_app, request, url_for
from todoism.apis.v1 import api_v1
from todoism.apis.v1.errors import api_abort
from todoism.models import Admin, TodoList
from todoism.apis.v1.auth import generate_token, auth_required
from todoism.apis.v1.schemas import todo_list_schema, todo_lists_schema
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

        user = Admin.query.filter_by(username=username).first()
        if user is None or not user.validate_password(password):
            return api_abort(code=400, message='Either the username or password was invalid.')

        token, expiration = generate_token(user)

        response = jsonify({
            'access_token': token,
            'token_type': 'Bearer',
            'expires_in': expiration
        })
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Pragma'] = 'no-cache'
        return response


class TodoListAPI(MethodView):
    def get(self, todo_list_id):
        todo_list = TodoList.query.get_or_404(todo_list_id)
        return jsonify(todo_list_schema(todo_list))


class TodoListsAPI(MethodView):
    # decorators = [auth_required]

    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = current_app.config['TODOISM_ITEM_PER_PAGE']
        pagination = TodoList.query.paginate(page, per_page)
        todo_lists = pagination.items
        current = url_for('.todo_lists', page=page, _external=True)
        prev = None
        if pagination.has_prev:
            prev = url_for('.todo_lists', page=page-1, _external=True)
        next = None
        if pagination.has_next:
            next = url_for('.todo_lists', page=page+1, _external=True)
        return jsonify(todo_lists_schema(todo_lists, current, prev, next, pagination))


api_v1.add_url_rule('/', view_func=IndexAPI.as_view('index'), methods=['GET'])
api_v1.add_url_rule('/oauth/token', view_func=AuthTokenAPI.as_view('token'), methods=['POST'])
api_v1.add_url_rule('/user/todo_lists', view_func=TodoListsAPI.as_view('todo_lists'), methods=['GET', 'POST'])
api_v1.add_url_rule('/user/todo_list/<int:todo_list_id>', view_func=TodoListAPI.as_view('todo_list'),
                    methods=['GET', 'POST', 'DELETE', 'PATCH'])




