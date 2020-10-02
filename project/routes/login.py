from flask import Blueprint, render_template, url_for

login_bp = Blueprint('login', __name__, url_prefix='/login')

@login_bp.route('', methods=['GET', 'POST'])
def login():
    
    return render_template('login.html')
# end login