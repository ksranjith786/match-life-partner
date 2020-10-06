from flask import Blueprint, render_template, url_for

education_bp = Blueprint('education', __name__, url_prefix='/education')

@education_bp.route('/', methods=['GET', 'POST'])
def education():
    return render_template('details/education.html')
# end education