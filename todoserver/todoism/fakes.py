import random
from todoism.models import Category, Plan, Mission
from sqlalchemy.exc import IntegrityError
from todoism import db
from faker import Faker


fake = Faker()


def fake_categorise(count=12):
    category = Category(name="default")
    db.session.add(category)
    for i in range(count):
        category = Category(name=fake.word())
        db.session.add(category)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def fake_plans(count=12):
    for i in range(count):
        plan = Plan(
            name=fake.sentence(),
            category=Category.query.get(random.randint(1, Category.query.count())),
        )
        db.session.add(plan)
    db.session.commit()
