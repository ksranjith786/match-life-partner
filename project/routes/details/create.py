from flask import Blueprint, render_template, url_for, request, redirect, flash
from werkzeug.security import generate_password_hash

from database.useraccount import addUserAccount, queryUserAccount, deleteUserAccount
from database.userdetails import addUser

create_bp = Blueprint('create', __name__, url_prefix='/create')

@create_bp.route('', methods=['GET', 'POST'])
def create():
    email = request.form.get("email", type = str)

    if (email == ""):
        msg = "Please enter Email Address"
        return render_template('register.html', errorMessage=msg)

    if (request.form.get("pass", type = str) == ""):
        msg = "Please enter Password!"
        return render_template('register.html', errorMessage=msg, email=email)

    if (request.form.get("cpass", type = str) == ""):
        msg = "Please enter Confirm Password!"
        return render_template('register.html', errorMessage=msg, email=email)

    if request.form.get("pass", type = str) != request.form.get("cpass", type = str):
        msg = "Error: Password and Confirm Password do not match!"
        render_template('register.html', errorMessage=msg, email=email)

    fname = request.form.get("fname", type = str)
    lname = request.form.get("lname", type = str)
    age = request.form.get("age", type = int)
    gender = request.form.get("gender", default="Male", type = str)
    city = request.form.get("city", default="", type = str)
    state = request.form.get("state", default="", type = str)
    country = request.form.get("country", default="India", type = str)
    address = request.form.get("address", default="", type = str)

    password = generate_password_hash(request.form.get("pass", type = str), method='sha256', salt_length=16)

    retVal = addUserAccount(email=email, password=password)
    
    msg = ""
    if retVal == False:
        msg = "Unable to add User Account as caught an exception while performing operation on UserAccount Table"
        return render_template('register.html', errorMessage=msg, email=email)
    
    rs = queryUserAccount(colName='email', value=email)

    loginId = 0
    for result in rs:
        loginId = result.id

    if loginId == 0:
        deleteUserAccount(email=email)
        msg = "Unable to fetch the added User Account as caught an exception while performing operation on UserAccount Table"
        return render_template('register.html', errorMessage=msg, email=email)

    retVal = addUser(loginid=loginId, fname=fname, lname=lname, age=age, gender=gender, city=city, state=state, country=country)

    if retVal == False:
        msg = "Unable to create/add User as caught an excepting while adding User Details to Database"
        return render_template('register.html', errorMessage=msg, email=email)
    else:
        msg = "Successfully registered! Please login to browse."

    #flash(message="Successfully registered! Please login to browse.", category="info")

    return redirect(url_for('login.login', displayMessage=msg, email=email))
# end create
