from flask import Blueprint, render_template, current_app, request, flash
from flask_login import login_required
from ..models import Mission, Category, Plan
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
        return render_template('home/index.html', missions=missions)


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
def show_plan(plan_id):
    plan = Plan.query.get_or_404(plan_id)
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['TODOISM_ITEM_PER_PAGE']
    pagination = Mission.query.with_parent(plan).order_by(Mission.created_at.desc()).paginate(page, per_page)
    items = pagination.items
    return render_template('home/plan.html', pagination=pagination, plan=plan, items=items)



