import random
from todoism.models import TodoList, Task
from sqlalchemy.exc import IntegrityError
from todoism import db
from faker import Faker


fake = Faker()


def fake_todo_lists(count=20):
    for i in range(count):
        todo_list = TodoList(name=fake.word())
        db.session.add(todo_list)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def fake_tasks(count=50):
    for i in range(count):
        status = 0
        for j in range(3):
            status = j
        task = Task(content=fake.sentence(), status=status)

