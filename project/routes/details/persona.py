from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.security import check_password_hash

from database.useraccount import UsersAccount, queryUserAccount
from database.userdetails import User, queryUser

persona_bp = Blueprint('persona', __name__, url_prefix='/persona')

@persona_bp.route('', methods=['GET', 'POST'])
def persona():
    email = request.form.get("email", type = str)
    password = request.form.get("pass", type = str)

    if (email == ""):
        msg = "Please enter Email Address"
        return render_template('login.html', displayMessage=msg)

    if (password == ""):
        msg = "Please enter Password!"
        return render_template('login.html', displayMessage=msg, email=email)

    rs = queryUserAccount("email", email)
    if rs is None:
        msg = "Your email is not available! Please register!"
        return render_template('register.html', errorMessage=msg, email=email)
    
    loginId = 0
    for result in rs:
        if check_password_hash(result.password, request.form.get("pass", type = str)):
            loginId = result.id
            #print("Login granted", loginId)
        else:
            return "Invalid Credentials! Please try again."

    rs = queryUser("loginid", loginId)
    if rs is None:
        msg = "Unable to fetch User Details!"
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

    return render_template('details/basic.html', userFName=user['First Name'], userLName=user['Last Name'])
# end persona