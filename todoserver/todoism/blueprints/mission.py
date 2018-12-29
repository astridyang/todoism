from flask import Blueprint, render_template, current_app, request
from flask_login import login_required
from ..models import Mission
mission_bp = Blueprint('mission', __name__)


@mission_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        day_completed_mission = request.form['day_completed_mission']
        day_used_hour = request.form['day_used_hour']
        print(day_completed_mission)
        print(day_used_hour)
    else:
        missions = Mission.query.filter(Mission.is_completed == 0)
        return render_template('mission/index.html', missions=missions)

