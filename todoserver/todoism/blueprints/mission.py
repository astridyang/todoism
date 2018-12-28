from flask import Blueprint, render_template, current_app, request
from flask_login import login_required
from ..models import Mission
mission_bp = Blueprint('mission', __name__)


@mission_bp.route('/')
@login_required
def index():
    missions = Mission.query.filter(Mission.is_completed == 0)
    return render_template('mission/index.html', missions=missions)

