from datetime import datetime
from todoism.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        check_password_hash(self.password_hash, password)


class Today(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    score = db.Column(db.Integer)

    missions = db.relationship('Mission', back_populates='day')


class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timespan = db.Column(db.String(20))
    content = db.Column(db.String(50))

    day_id = db.Column(db.Integer, db.ForeignKey('today.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('mission_category.id'))

    day = db.relationship('Today', back_populates='missions')
    category = db.relationship('MissionCategory', back_populates='missions')


class MissionCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    missions = db.relationship('Mission', back_populates='category')


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    tasks = db.relationship('Task', back_populates='todo_list')


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(50))
    status = db.Column(db.Integer, default=0)

    list_id = db.Column(db.Integer, db.ForeignKey('todo_list.id'))
    todo_list = db.relationship('TodoList', back_populates='tasks')




