from app import app


@app.route('/')
def index():
    return '<h1>WASSUPPP</h1>'


@app.route('/help')
def help():
    return '<h1>HEARD YOU NEEDED SOME HELP</h1>'


@app.route('/additionalhelp')
def more_help():
    return '<h1>DAMN HOW MUCH HELP YOU NEED</h1>'


@app.route('/item/<int:id>')
def item(id):
    if(id > 0 and id < 100):
        return f'<h1>Heres some stuff</h1><h2>Item {id}</h2>'
    else:
        return 'THAT DONT EXIST'
