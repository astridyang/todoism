from datetime import datetime
import time
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
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    name = db.Column(db.String(30))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', back_populates='plans')

    missions = db.relationship('Mission', back_populates='plan')


class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    name = db.Column(db.String(30))
    unit = db.Column(db.String(10))
    total_missions = db.Column(db.Integer)
    start_at = db.Column(db.DateTime, index=True)
    end_at = db.Column(db.DateTime, index=True)
    total_days = db.Column(db.Integer)
    # daily plan mission
    daily_missions = db.Column(db.Integer)
    # daily plan minutes
    daily_times = db.Column(db.Integer)
    total_times = db.Column(db.Integer)
    total_used_times = db.Column(db.Integer, default=0)
    # current completed mission
    completed_missions = db.Column(db.Integer, default=0)
    # is_completed: 1 yes, 0 no
    is_completed = db.Column(db.Integer, default=0)
    # status = db.Column(db.Integer, default=1)
    # (1 show, 0 hide) in index.html
    is_show = db.Column(db.Integer, default=1)
    summary = db.Column(db.TEXT, default='')

    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    plan = db.relationship('Plan', back_populates='missions')
    logs = db.relationship('MissionLog', back_populates='mission')


class MissionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    log_id = db.Column(db.Integer)
    completed_mission = db.Column(db.Integer)
    used_time = db.Column(db.Integer)

    mission_id = db.Column(db.Integer, db.ForeignKey('mission.id'))
    mission = db.relationship('Mission', back_populates='logs')


# class Log(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
#     completed_mission = db.Column(db.Integer)
#     used_time = db.Column(db.Float)
#
#     mission_log_id = db.Column(db.Integer, db.ForeignKey('mission_log.log_id'))
#     mission_log = db.relationship('MissionLog', back_populates='logs')
#
#     mission_id = db.Column(db.Integer, db.ForeignKey('mission.id'))
#     mission = db.relationship('Mission', back_populates='logs')









