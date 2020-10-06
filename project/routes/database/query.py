from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.security import check_password_hash

from database.useraccount import UsersAccount, queryUserAccount
from database.userdetails import User, queryUser

query_bp = Blueprint('query', __name__, url_prefix='/query')

@query_bp.route('', methods=['GET'])
def query():
    email = request.args.get("email", type = str)
    print(email)
    rs = queryUserAccount("email", email)
    if rs is None:
        msg = "No such Email to fetch an User"
        return msg

    loginIdFromDB = 0
    for result in rs:
        if result:
            loginIdFromDB = result.id
        else:
            return "Invalid Credentials! Please try again."

    rs = queryUser("loginid", loginIdFromDB)
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

@query_bp.route('/all', methods=['GET'])
def queryAll():
    rs = queryUserAccount("email", "@")
    if rs is None:
        msg = "No such Email to fetch an User"
        return msg

    users = []
    loginIdFromDB = 0
    for result in rs:
        if result:
            loginIdFromDB = result.id
            rssub = queryUser("loginid", loginIdFromDB)
            if rssub is None:
                msg = "No such Email to fetch an User"
                return msg
            for result in rssub:
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
        else:
            return "Invalid Credentials! Please try again."    
        
    return jsonify(users)
# end query