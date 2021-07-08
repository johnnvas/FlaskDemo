from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('page.html', title='WASSUUUUUP')
    # return '<h1>WASSUPPP</h1>'


@app.route('/help')
def help():
    return render_template('page.html', title='HEARD YOU NEEDED SOME HELP')


@app.route('/additionalhelp')
def more_help():
    return render_template('page.html', title='DAMN HOW MUCH HELP YOU NEED')
