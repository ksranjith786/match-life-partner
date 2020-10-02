from flask import Blueprint, render_template, url_for

register_bp = Blueprint('register', __name__, url_prefix='/register')

@register_bp.route('/', methods=['GET', 'POST'])
def register():
    return render_template('register.html')
# end register