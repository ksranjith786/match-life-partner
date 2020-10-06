from flask import Blueprint, render_template, url_for

location_bp = Blueprint('location', __name__, url_prefix='/location')

@location_bp.route('/', methods=['GET', 'POST'])
def location():
    return render_template('details/location.html')
# end location