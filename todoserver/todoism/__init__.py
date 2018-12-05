# coding:utf-8
import os
import click
from flask import Flask
from todoism.settings import config
from todoism.extensions import db, migrate, bootstrap, login_manager, csrf
from todoism.blueprints.auth import auth_bp
from todoism.blueprints.mission import mission_bp
from todoism.blueprints.admin import admin_bp
from todoism.models import Admin, Category, Plan, Mission


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('todoism')
    app.config.from_object(config[config_name])
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_shell_context(app)
    register_template_context(app)
    return app


def register_template_context(app):
    @app.context_processor
    def make_template_context():
        admin = Admin.query.first()
        categories = Category.query.order_by(Category.name).all()
        plans = Plan.query.order_by(Plan.name).all()
        missions = Mission.query.order_by(Mission.name).all()
        return dict(admin=admin, categories=categories, plans=plans, missions=missions)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)


def register_blueprints(app):
    app.register_blueprint(mission_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(admin_bp, url_prefix="/admin")


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            db.drop_all()
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    @click.option('--username', prompt=True, help='The username used to login.')
    @click.option('--password', prompt=True, hide_input=True,
                  confirmation_prompt=True, help='The password used to login.')
    def init(username, password):
        click.echo('Initializing the database...')
        db.create_all()

        admin = Admin.query.first()
        if admin is not None:
            click.echo('The administrator already exists, updating...')
            admin.username = username
            admin.set_password(password)
        else:
            click.echo('Creating the temporary administrator account...')
            admin = Admin(username=username)
            admin.set_password(password)
            db.session.add(admin)
        db.session.commit()
        click.echo('Done.')

    @app.cli.command()
    @click.option('--category', default=12, help='Quantity of todo_lists, default is 12.')
    def forge(category):
        """Generate fake data."""
        # from todoism.fakes import fake_categorise
        #
        # db.drop_all()
        # db.create_all()
        #
        # click.echo('Generating %d categorise...' % category)
        # fake_categorise(category)
        #
        # click.echo('Done')


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, Admin=Admin)


