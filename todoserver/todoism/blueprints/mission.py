from flask import Blueprint, render_template, current_app, request
from flask_login import login_required
from ..models import Category, Plan
mission_bp = Blueprint('mission', __name__)


@mission_bp.route('/')
@login_required
def index():
    plan_list = Plan.query.all()

    return render_template('mission/index.html', plan_list=plan_list)