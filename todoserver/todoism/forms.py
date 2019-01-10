from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, ValidationError, \
    DateField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length
from todoism.models import Category, Plan
from datetime import datetime


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(1, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Submit')


class CategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 30)])
    submit = SubmitField('Submit')

    def validate_name(self, field):
        if Category.query.filter_by(name=field.data).first():
            raise ValidationError('name already in use')


class PlanForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 60)])
    category = SelectField('Category', coerce=int, default=1)
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.id, category.name)
                                 for category in Category.query.order_by(Category.name).all()]


class MissionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 30)])
    plan = SelectField('Plan', coerce=int, default=1)
    unit = StringField('Unit', validators=[DataRequired(), Length(1, 10)])
    total_missions = IntegerField('Total missions', validators=[DataRequired()])
    start_at = DateField('Start at', format='%Y-%m-%d', default=datetime.utcnow(), validators=[DataRequired()])
    end_at = DateField('End at', format='%Y-%m-%d', default=datetime.utcnow(), validators=[DataRequired()])
    daily_times = FloatField('Daily times', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(MissionForm, self).__init__(*args, **kwargs)
        self.plan.choices = [(plan.id, plan.name)
                             for plan in Plan.query.order_by(Plan.name).all()]
