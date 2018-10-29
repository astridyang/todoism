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
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)


class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timespan = db.Column(db.String(20))
    content = db.Column(db.String(50))

    day_id = db.Column(db.Integer, db.ForeignKey('today.id'))
    category_id = db.Column(db.Integer, db.ForeignKey(''))