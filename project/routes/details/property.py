from flask import Blueprint, render_template, url_for

property_bp = Blueprint('property', __name__, url_prefix='/property')

@property_bp.route('/', methods=['GET', 'POST'])
def property():
    return render_template('details/property.html')
# end property