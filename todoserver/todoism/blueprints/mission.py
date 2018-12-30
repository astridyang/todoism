from flask import Blueprint, render_template, current_app, request, flash
from flask_login import login_required
from ..models import Mission
from ..utils import redirect_back
from ..extensions import db
mission_bp = Blueprint('mission', __name__)


@mission_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        ids = request.form.getlist('id[]')
        missions = request.form.getlist('day_completed_mission[]')
        hours = request.form.getlist('day_used_hour[]')
        for i in ids:
            mission = Mission.query.get_or_404(i)
            mission.completed_missions += int(missions[ids.index(i)])
            mission.total_used_hours += float(hours[ids.index(i)])
            db.session.commit()
        flash('submit success', 'success')
        return redirect_back()
    else:
        missions = Mission.query.filter(Mission.is_completed == 0)
        return render_template('mission/index.html', missions=missions)

