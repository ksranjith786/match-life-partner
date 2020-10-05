from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.security import check_password_hash

from database.useraccount import UsersAccount, queryUserAccountFromDB
from database.userdetails import User, queryUserFromDB

query_bp = Blueprint('query', __name__, url_prefix='/query')

@query_bp.route('', methods=['GET'])
def query():
    email = request.args.get("email", type = str)
    print(email)
    rs = queryUserAccountFromDB("email", email)
    if rs is None:
        msg = "No such Email to fetch an User"
        return msg

    loginIdFromDB = 0
    for result in rs:
        if result:
            loginIdFromDB = result.id
        else:
            return "Invalid Credentials! Please try again."

    rs = queryUserFromDB("loginid", loginIdFromDB)
    if rs is None:
        msg = "No such Email to fetch an User"
        return msg
    
    users = []
    for result in rs:
        user = dict()
        user['First Name'] = result.fname
        user['Last Name'] = result.lname
        user['Age'] = result.age
        user['Gender'] = result.gender
        user['City'] = result.city
        user['State'] = result.state
        user['Country'] = result.country
        user['loginid'] = result.loginid
        users.append(user)

    return jsonify(users)
# end query