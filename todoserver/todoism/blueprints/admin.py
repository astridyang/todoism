from flask import Blueprint, flash, redirect, url_for, render_template, request, current_app
from flask_login import login_required, current_user
from ..forms import CategoryForm, PlanForm, MissionForm
from ..models import Category, Plan, Mission
from ..extensions import db
from ..utils import redirect_back
import math

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/category/new', methods=['get', 'post'])
@login_required
def new_category():
    form = CategoryForm()
    if form.validate_on_submit():
        name = form.name.data
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        flash('Category created.', 'success')
        return redirect(url_for('.manage_category'))
    return render_template('admin/new_category.html', form=form, title="New Category")


@admin_bp.route('/category/manage')
@login_required
def manage_category():
    return render_template('admin/manage_category.html')


@admin_bp.route('/category/<int:category_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_category(category_id):
    form = CategoryForm()
    category = Category.query.get_or_404(category_id)
    if category.id == 1:
        flash('You can not edit the default category.', 'warning')
        return redirect(url_for('.manage_category'))
    if form.validate_on_submit():
        category.name = form.name.data
        db.session.commit()
        flash('Category updated.', 'success')
        return redirect(url_for('.manage_category'))
    form.name.data = category.name
    return render_template('admin/new_category.html', form=form, title="Edit Category")


@admin_bp.route('/category/<int:category_id>/delete', methods=['POST'])
@login_required
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    if category.id == 1:
        flash('You can not delete the default category.', 'warning')
        return redirect(url_for('blog.index'))
    category.delete()
    flash('Category deleted.', 'success')
    return redirect(url_for('.manage_category'))


@admin_bp.route('/plan/new', methods=['GET', 'POST'])
@login_required
def new_plan():
    form = PlanForm()
    if form.validate_on_submit():
        name = form.name.data
        category = Category.query.get(form.category.data)
        post = Plan(name=name, category=category)
        db.session.add(post)
        db.session.commit()
        flash('Plan created.', 'success')
        return redirect(url_for('.manage_plan'))
    return render_template('admin/new_plan.html', form=form, title='New Plan')


@admin_bp.route('/plan/manage')
@login_required
def manage_plan():
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['TODOISM_ITEM_PER_PAGE']
    pagination = Plan.query.order_by(Plan.created_at.desc()).paginate(page=page, per_page=per_page)
    plans = pagination.items
    return render_template('admin/manage_plan.html', plans=plans, pagination=pagination, page=page)


@admin_bp.route('/plan/<int:plan_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_plan(plan_id):
    form = PlanForm()
    plan = Plan.query.get_or_404(plan_id)
    if form.validate_on_submit():
        plan.name = form.name.data
        plan.category = Category.query.get(form.category.data)
        db.session.commit()
        flash('Plan updated.', 'success')
        return redirect(url_for('.manage_plan'))
    form.name.data = plan.name
    form.category.data = plan.category_id
    return render_template('admin/new_plan.html', form=form, title="Edit Plan")


@admin_bp.route('/plan/<int:plan_id>/delete', methods=['POST'])
@login_required
def delete_plan(plan_id):
    plan = Plan.query.get_or_404(plan_id)
    db.session.delete(plan)
    db.session.commit()
    flash('Plan deleted.', 'success')
    return redirect_back()


@admin_bp.route('/mission/new', methods=['GET', 'POST'])
@login_required
def new_mission():
    form = MissionForm()
    if form.validate_on_submit():
        name = form.name.data
        plan = Plan.query.get(form.plan.data)
        unit = form.unit.data
        total_missions = form.total_missions.data
        start_at = form.start_at.data
        end_at = form.end_at.data
        if end_at < start_at:
            flash('End at is invalid', 'warning')
        else:
            daily_hours = form.daily_hours.data
            total_days = (end_at - start_at).days
            daily_missions = math.ceil(total_missions / total_days)
            total_hours = daily_hours * total_days
            mission = Mission(name=name, plan=plan, unit=unit, total_missions=total_missions,
                              start_at=start_at, end_at=end_at, daily_hours=daily_hours,
                              daily_missions=daily_missions, total_hours=total_hours,
                              total_days=total_days)
            db.session.add(mission)
            db.session.commit()
            flash('Mission created.', 'success')
            return redirect(url_for('.manage_mission'))
    return render_template('admin/new_mission.html', form=form, title='New Mission')


@admin_bp.route('/mission/manage')
@login_required
def manage_mission():
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['TODOISM_ITEM_PER_PAGE']
    pagination = Mission.query.order_by(Mission.created_at.desc()).paginate(page=page, per_page=per_page)
    missions = pagination.items
    return render_template('admin/manage_mission.html', missions=missions, pagination=pagination, page=page)


@admin_bp.route('/mission/<int:mission_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_mission(mission_id):
    form = MissionForm()
    mission = Mission.query.get_or_404(mission_id)
    if form.validate_on_submit():
        mission.name = form.name.data
        mission.plan = Plan.query.get(form.plan.data)
        mission.unit = form.unit.data
        mission.total_missions = form.total_missions.data
        mission.start_at = form.start_at.data
        mission.end_at = form.end_at.data
        if mission.end_at < mission.start_at:
            flash("End at is invalid", 'warning')
        else:
            mission.daily_hours = form.daily_hours.data
            # recalculate
            mission.total_days = (mission.end_at - mission.start_at).days
            mission.daily_missions = math.ceil(mission.total_missions / mission.total_days)
            mission.total_hours = mission.daily_hours * mission.total_days
            db.session.commit()
            flash('Mission updated.', 'success')
            return redirect(url_for('.manage_mission'))
    form.name.data = mission.name
    form.plan.data = mission.plan_id
    form.unit.data = mission.unit
    form.total_missions.data = mission.total_missions
    form.start_at.data = mission.start_at
    form.end_at.data = mission.end_at
    form.daily_hours.data = mission.daily_hours
    return render_template('admin/new_plan.html', form=form, title="Edit Mission")


@admin_bp.route('/mission/<int:mission_id>/delete', methods=['POST'])
@login_required
def delete_mission(mission_id):
    mission = Mission.query.get_or_404(mission_id)
    db.session.delete(mission)
    db.session.commit()
    flash('Mission deleted.', 'success')
    return redirect_back()


@admin_bp.route('/mission/<int:mission_id>/delete', methods=['POST'])
@login_required
def complete_mission(mission_id):
    mission = Mission.query.get_or_404(mission_id)
    mission.is_completed = 1
    db.session.commit()
    flash('Mission completed.', 'success')
    return redirect_back()
