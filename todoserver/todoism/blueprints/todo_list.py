from flask import Blueprint
from ..models import TodoList, Task

todo_list_bp = Blueprint('todo_list', __name__)


@todo_list_bp.route('/todo_lists')
def show_todo_lists():
    todo_lists = TodoList.query.order_by(TodoList.timestamp.desc())
