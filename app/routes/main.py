from flask import Blueprint, render_template, redirect
from app.forms.login import LoginForm

bp = Blueprint('', __name__)


@bp.route('/')
def index():
    return render_template('page.html', title='WASSUUUUUP')
    # return '<h1>WASSUPPP</h1>'


@bp.route('/help')
def help():
    return render_template('page.html', title='HEARD YOU NEEDED SOME HELP')


@bp.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@bp.route('/additionalhelp')
def more_help():
    return render_template('page.html', title='DAMN HOW MUCH HELP YOU NEED')
