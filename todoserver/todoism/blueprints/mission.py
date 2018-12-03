from flask import Blueprint, render_template, current_app, request
from ..models import Category
mission_bg = Blueprint('mission', __name__)


@mission_bg.route('/')
def index():
    return render_template('mi')