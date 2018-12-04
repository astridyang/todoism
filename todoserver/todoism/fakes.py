import random
from todoism.models import Category, Admin
from sqlalchemy.exc import IntegrityError
from todoism import db
from faker import Faker


fake = Faker()


def fake_categorise(count=12):
    author = Admin.query.first()
    category = Category(name="default", author=author)
    db.session.add(category)
    for i in range(count):
        category = Category(name=fake.word(), author=author)
        db.session.add(category)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


