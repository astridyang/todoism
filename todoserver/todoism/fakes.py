import random
from todoism.models import TodoList
from sqlalchemy.exc import IntegrityError
from todoism import db
from faker import Faker


fake = Faker()


def fake_lists(count=10):
    for i in range(count):
        todo_list = TodoList(name=fake.word())
        db.session.add(todo_list)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
