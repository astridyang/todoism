from flask import Blueprint, flash, redirect, url_for, render_template, request, current_app
from flask_login import login_required, current_user
from ..forms import CategoryForm, PlanForm, MissionForm
from ..models import Category, Plan, Mission
from ..extensions import db
from ..utils import redirect_back

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


@admin_bp.route('/category/<int:category_id>', methods=['GET', 'POST'])
def show_category(category_id):
    category = Category.query.get_or_404(category_id)
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['TODOISM_ITEM_PER_PAGE']
    pagination = Plan.query.with_parent(category).order_by(Plan.timestamp.desc()).paginate(page, per_page)
    plans = pagination.items
    return render_template('admin/category.html', pagination=pagination, category=category, plans=plans)


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
    return render_template('admin/manage_plan.html')


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
        plan_time = form.plan_time.data
        mission = Mission(name=name, plan=plan, plan_time=plan_time)
        db.session.add(mission)
        db.session.commit()
        flash('Mission created.', 'success')
        return redirect(url_for('.manage_mission'))
    return render_template('admin/new_mission.html', form=form, title='New Mission')


@admin_bp.route('/mission/manage')
@login_required
def manage_mission():
    return render_template('admin/manage_mission.html')


@admin_bp.route('/mission/<int:mission_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_mission(mission_id):
    form = MissionForm()
    mission = Mission.query.get_or_404(mission_id)
    if form.validate_on_submit():
        mission.name = form.name.data
        mission.plan = Plan.query.get(form.plan.data)
        mission.plan_time = form.plan_time.data
        db.session.commit()
        flash('Mission updated.', 'success')
        return redirect(url_for('.manage_mission'))
    form.name.data = mission.name
    form.plan.data = mission.plan_id
    form.plan_time.data = mission.plan_time
    return render_template('admin/new_plan.html', form=form, title="New Mission")


@admin_bp.route('/mission/<int:mission_id>/delete', methods=['POST'])
@login_required
def delete_mission(mission_id):
    mission = Mission.query.get_or_404(mission_id)
    db.session.delete(mission)
    db.session.commit()
    flash('Mission deleted.', 'success')
    return redirect_back()
