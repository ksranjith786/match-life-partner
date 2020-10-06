from database.database import *

class UsersAccount(Base):
    __tablename__ = 'usersaccount'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    def __init__(self, email="", password=""):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<UsersAccount %r>' % (self.email)

def queryUserAccount(colName="", value=""):
    db_session = getDBSession()
    
    try:
        look_for = '%{0}%'.format(value)
        #print(f'Debug | value={look_for} of column={colName}')
        rs = None
        if colName == "email":
            rs = db_session.query(UsersAccount).filter(UsersAccount.email.ilike(look_for))
        else:
            pass
        
        id = 0
        for result in rs:
            id = result.id
        # When the rs is empty, the id field is not updated; Hence, the database query did not result anything.
        if id == 0:
            return None
        
    except Exception as error:
        print("Exception caught while querying UserAccount from Database")
        print(str(error.orig) + " for parameters" + str(error.params))
        return None

    #print("No.of Records matched:", noOfRecords)
    return rs
# end queryUserAccount


def addUserAccount(email="", password=""):
    db_session = getDBSession()

    try:
        userAcc = UsersAccount(email=email, password=password)

        db_session.add(userAcc)
        db_session.commit()

    except Exception as error:
        print("Exception caught while adding user email and password to UsersAccount Table")
        print(str(error.orig) + " for parameters" + str(error.params))
        return False

    return True
# end addUserAccount

def deleteUserAccount(email=""):
    db_session = getDBSession()

    try:
        userAcc = queryUserAccount(colName='email', value=email)

        db_session.delete(userAcc)
        db_session.commit()

    except Exception as error:
        print("Exception caught while deleting user email and password to UsersAccount Table")
        print(str(error.orig) + " for parameters" + str(error.params))
        return False

    return True
# end deleteUserAccount
