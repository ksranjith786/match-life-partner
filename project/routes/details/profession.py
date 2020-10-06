from flask import Blueprint, render_template, url_for

profession_bp = Blueprint('profession', __name__, url_prefix='/profession')

@profession_bp.route('/', methods=['GET', 'POST'])
def profession():
    return render_template('details/profession.html')
# end profession