from flask import Blueprint, render_template, url_for

basic_additional_bp = Blueprint('basic_additional', __name__, url_prefix='/basic_additional')

@basic_additional_bp.route('/', methods=['GET', 'POST'])
def basic_additional():
    return render_template('details/basic_additional.html')
# end basic_additional