import random
from todoism.models import TodoList, Task
from sqlalchemy.exc import IntegrityError
from todoism import db
from faker import Faker


fake = Faker()


def fake_todo_lists(count=12):
    for i in range(count):
        todo_list = TodoList(name=fake.word())
        db.session.add(todo_list)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def fake_tasks(count=50):
    for i in range(count):
        task = Task(
            content=fake.sentence(),
            status=random.randint(1, 3),
            todo_list=TodoList.query.get(random.randint(1, TodoList.query.count()))
        )
        db.session.add(task)
        db.session.commit()

