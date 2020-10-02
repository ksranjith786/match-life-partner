from flask import Blueprint, render_template, url_for, request
from werkzeug.security import generate_password_hash

from database.database import addUserDetailsToDB

create_bp = Blueprint('create', __name__, url_prefix='/create')

@create_bp.route('', methods=['GET', 'POST'])
def create():
    email = request.form.get("email", type = str)

    if request.form.get("pass", type = str) != request.form.get("cpass", type = str):
        return "Error: Password and Confirm Password do not match!"

    password = generate_password_hash(request.form.get("pass", type = str), method='sha256', salt_length=16)
    fname = request.form.get("fname", type = str)
    lname = request.form.get("lname", type = str)
    age = request.form.get("age", type = int)
    gender = request.form.get("gender", default="Male", type = str)
    city = request.form.get("city", default="", type = str)
    state = request.form.get("state", default="", type = str)
    country = request.form.get("country", default="India", type = str)
    address = request.form.get("address", default="", type = str)

    print(f'Ranjith | First Name {fname}; Last Name {lname}')

    retVal = addUserDetailsToDB(email=email, password=password, fname=fname, lname=lname, age=age, gender=gender, city=city, state=state, country=country)

    if retVal == False:
        print("Exception caught while creating and adding User Details to Database")
        return False

    return "Successfully added an User"
# end create