from flask import url_for


def category_schema(category):
    return {
        'id': category.id,
        'self': url_for('.category', category_id=category.id, _external=True),
        'kink': 'Category',
        'name': category.name,
    }


def categorise_schema(categorise):
    return {
        'self': url_for('.categorise', _external=True),
        'kind': 'CategoryCollection',
        'items': [category_schema(category) for category in categorise]
    }