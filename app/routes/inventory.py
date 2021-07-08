from flask import Blueprint, render_template

bp = Blueprint('inventory', __name__, url_prefix='/inventory')


@bp.route('/item/<int:id>')
def item(id):
    if(id > 0 and id < 100):
        item = {
            'id': id,
            'name': f'BEST ITEM {id}',
            'description': "Coming soon!",
        }
        return render_template('item.html', item=item)

    else:
        return '<h1>THAT DONT EXIST</h1><h2>WHATS WRONG WITH YOU</h2>'
