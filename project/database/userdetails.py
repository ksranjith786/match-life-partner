from database.database import *

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    loginid = Column(Integer, ForeignKey('usersaccount.id', onupdate='CASCADE', ondelete='CASCADE'))
    fname = Column(String)
    lname = Column(String)
    age = Column(Integer)
    gender = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)

    def __init__(self, loginid=0, fname="", lname="", age=18, gender="Male", city="", state="", country=""):
        self.loginid = loginid
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        self.city = city
        self.state = state
        self.country = country

    def __repr__(self):
        return '<User %r>' % (self.fname)


def queryUserFromDB(colName="", value=""):
    db_session = getDBSession()
    
    try:
        look_for = '%{0}%'.format(value)
        rs = None
        if colName == "loginid":
            rs = db_session.query(User).filter(User.loginid == value)
        elif colName == "fname":
            rs = db_session.query(User).filter(User.fname.ilike(look_for))
        elif colName == "lname":
            rs = db_session.query(User).filter(User.lname.ilike(look_for))
        elif colName == "city":
            rs = db_session .query(User).filter(User.city.ilike(look_for))
        elif colName == "state":
            rs = db_session.query(User).filter(User.state.ilike(look_for))
        elif colName == "country":
            rs = db_session.query(User).filter(User.country.ilike(look_for))
        else:
            pass

        for result in rs:
            if not result:
                return None

    except Exception as error:
        print("Exception caught while querying User from Database")
        print(str(error.orig) + " for parameters" + str(error.params))
        return None

    #print("No.of Records matched:", noOfRecords)
    return rs
# end queryUserFromDB


def addUserDetailsToDB(loginId=0, email="", fname="", lname="", age=18, gender="Male", city="", state="", country=""):
    db_session = getDBSession()
    
    try:
        user = User(loginid=loginId, fname=fname, lname=lname, age=age, gender=gender, city=city, state=state, country=country)

        db_session.add(user)
        db_session.commit()
    
    except Exception as error:
        print("Exception caught while adding user record to Users Table")
        print(str(error.orig) + " for parameters" + str(error.params))
        return False

    return True
# end addUserToDB
