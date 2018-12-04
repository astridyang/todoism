from flask import Blueprint, render_template, current_app, request
from flask_login import login_required
from ..models import Category
mission_bp = Blueprint('mission', __name__)


@mission_bp.route('/')
@login_required
def index():
    return render_template('mission/index.html')