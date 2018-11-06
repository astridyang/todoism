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


def plan_schema(plan):
    return {
        'id': plan.id,
        'self': url_for('.plan', plan_id=plan.id, _external=True),
        'kink': 'Plan',
        'name': plan.name,
    }


def plans_schema(plans):
    return {
        'self': url_for('.plans', _external=True),
        'kind': 'PlanCollection',
        'items': [plan_schema(plan) for plan in plans]
    }


def missions_schema():
    return {
        'self': url_for('.missions', _external=True),
        'kind': 'MissionCollection'
    }