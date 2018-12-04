from datetime import datetime
from todoism.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    plans = db.relationship('Plan', back_populates='category')

    def delete(self):
        default_category = Category.query.get(1)
        plans = self.plans[:]
        for plan in plans:
            plan.category = default_category
        db.session.delete(self)
        db.session.commit()


class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # TODO index
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    name = db.Column(db.String(30))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', back_populates='plans')










