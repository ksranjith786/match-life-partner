from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.security import check_password_hash

from database.database import UsersAccount, queryUserFromDB, queryUserAccountFromDB

persona_bp = Blueprint('persona', __name__, url_prefix='/persona')

@persona_bp.route('', methods=['GET', 'POST'])
def persona():
    email = request.form.get("email", type = str)
    password = request.form.get("pass", type = str)
    
    rs = queryUserAccountFromDB("email", email)
    if rs is None:
        msg = "No such Email to fetch an User"
        return msg
    
    for result in rs:
        print(f'Password Entered is {password} and stored in Database is {result.password}')
        if check_password_hash(result.password, request.form.get("pass", type = str)):
            msg = "Login granted"
        else:
            return "Invalid Credentials! Please try again."

    rs = queryUserFromDB("loginid", result.id)
    if rs is None:
        msg = "No such Email to fetch an User"
        return msg
    
    user = dict()
    for result in rs:
        user['First Name'] = result.fname
        user['Last Name'] = result.lname
        user['Age'] = result.age
        user['Gender'] = result.gender
        user['City'] = result.city
        user['State'] = result.state
        user['Country'] = result.country

    return jsonify(user)
# end persona