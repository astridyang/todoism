from flask import url_for


def category_schema(category):
    return {
        'id': category.id,
        'self': url_for('.category', category_id=category.id, _external=True),
        'kink': 'Category',
        'name': category.name,
    }


def categorise_schema(categorise, current, prev, next, pagination):
    return {
        'self': current,
        'kind': 'CategoryCollection',
        'items': [category_schema(category) for category in categorise],
        'prev': prev,
        'next': next,
        'last': url_for('.categorise', page=pagination.pages, _external=True),
        'first': url_for('.categorise', page=1, _external=True),
        'count': pagination.total
    }