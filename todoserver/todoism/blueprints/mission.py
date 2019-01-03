from flask import Blueprint, render_template, current_app, request, flash
from flask_login import login_required
from ..models import Mission, Category, Plan, MissionLog, Log
from ..utils import redirect_back
from ..extensions import db
import time
from datetime import datetime
mission_bp = Blueprint('mission', __name__)


@mission_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        ids = request.form.getlist('id[]')
        missions = request.form.getlist('day_completed_mission[]')
        hours = request.form.getlist('day_used_hour[]')
        now = datetime.utcnow()
        log_id = int(now.strftime("%Y%m%d"))
        # log_id = int(now.strftime("%Y%m%d%H%M%S"))
        mission_log = MissionLog.query.filter(MissionLog.log_id == log_id).first()
        if mission_log:
            flash('One day can only submit once', 'warning')
            return redirect_back()
        else:
            mission_log = MissionLog(log_id=log_id)
            db.session.add(mission_log)
            db.session.commit()
            for i in ids:
                mission = Mission.query.get_or_404(i)
                completed_mission = int(missions[ids.index(i)])
                used_time = float(hours[ids.index(i)])
                mission.completed_missions += completed_mission
                # if completed
                if mission.completed_missions >= mission.total_missions:
                    mission.is_completed = 1
                mission.total_used_hours += used_time

                log = Log(completed_mission=completed_mission, used_time=used_time,
                          mission_log=mission_log, mission=mission)
                db.session.add(log)
                db.session.commit()
            flash('submit success', 'success')
            return redirect_back()
    else:
        missions = Mission.query.filter(Mission.is_completed == 0).all()
        total_time = 0.0
        for mission in missions:
            total_time += mission.daily_hours
        return render_template('home/index.html', missions=missions, total_time=total_time)


@mission_bp.route('/category/<int:category_id>', methods=['GET', 'POST'])
@login_required
def show_category(category_id):
    category = Category.query.get_or_404(category_id)
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['TODOISM_ITEM_PER_PAGE']
    pagination = Plan.query.with_parent(category).order_by(Plan.created_at.desc()).paginate(page, per_page)
    items = pagination.items
    return render_template('home/category.html', pagination=pagination, category=category, items=items)


@mission_bp.route('/plan/<int:plan_id>', methods=['GET', 'POST'])
@login_required
def show_plan(plan_id):
    plan = Plan.query.get_or_404(plan_id)
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['TODOISM_ITEM_PER_PAGE']
    pagination = Mission.query.with_parent(plan).order_by(Mission.created_at.desc()).paginate(page, per_page)
    items = pagination.items
    return render_template('home/plan.html', pagination=pagination, plan=plan, items=items)


@mission_bp.route('/view_log')
@login_required
def view_log():
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['TODOISM_ITEM_PER_PAGE']
    pagination = MissionLog.query.order_by(MissionLog.timestamp.desc()).paginate(page, per_page=per_page)
    items = pagination.items
    return render_template('home/log.html', items=items, pagination=pagination)


@mission_bp.route('/view_mission_log/<int:mission_id>')
@login_required
def view_mission_log(mission_id):
    logs = Log.query.filter(Log.mission_id == mission_id).all()
    mission = Mission.query.filter(Mission.id == mission_id).first()
    return render_template('home/mission_log.html', logs=logs, mission=mission)




