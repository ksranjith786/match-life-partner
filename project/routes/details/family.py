from flask import Blueprint, render_template, url_for

family_bp = Blueprint('family', __name__, url_prefix='/family')

@family_bp.route('/', methods=['GET', 'POST'])
def family():
    return render_template('details/family.html')
# end family