from flask import Blueprint, render_template, url_for

vehicle_bp = Blueprint('vehicle', __name__, url_prefix='/vehicle')

@vehicle_bp.route('/', methods=['GET', 'POST'])
def vehicle():
    return render_template('details/vehicle.html')
# end vehicle