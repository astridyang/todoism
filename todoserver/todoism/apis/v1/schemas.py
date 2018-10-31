from flask import url_for


def todo_list_schema(todo_list):
    return {
        'id': todo_list.id,
        'self': url_for('.todo_list', todo_list_id=todo_list.id, _external=True),
        'kink': 'TodoList',
        'name': todo_list.name,
        'tasks': todo_list.tasks
    }


def todo_lists_schema(todo_lists, current, prev, next, pagination):
    return {
        'self': current,
        'kind': 'TodoListCollection',
        'items': [todo_list_schema(todo_list) for todo_list in todo_lists],
        'prev': prev,
        'next': next,
        'last': url_for('.todo_lists', page=pagination.pages, _external=True),
        'first': url_for('.todo_lists', page=1, _external=True),
        'count': pagination.total
    }