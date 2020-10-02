from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Sequence, ForeignKey, String, and_, or_

engine = None
Base = declarative_base()
db_session = None

# Users Account Class
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

# User Details Class
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

Session = sessionmaker(bind=engine)
ses = Session()

def initDB(databaseURL):
    global engine, db_session

    if "postgresql" in databaseURL:
        engine = create_engine(databaseURL)
    elif "sqlite" in databaseURL:
        engine = create_engine(databaseURL, convert_unicode=True, connect_args={'check_same_thread': False})
    else:
        engine = create_engine(databaseURL)
    
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    return db_session
# end initDB

def createUserDB(databaseURL):
    initDB(databaseURL)
    global Base
    Base.metadata.bind = engine
    Base.metadata.create_all(bind=engine)
# end createUserDB

def addUserDetailsToDB(email="", password="", fname="", lname="", age=18, gender="Male", city="", state="", country=""):
    userAcc = UsersAccount(email=email, password=password)
    user = User(fname=fname, lname=lname, age=age, gender=gender, city=city, state=state, country=country)

    if db_session == None:
        initDB()
    try:
        db_session.add(userAcc)
        db_session.commit()

        rs = queryUserAccountFromDB(colName='email', value=email)
        loginId=0
        for result in rs:
            loginId=result.id
            print(f'UserAccount Table is added with {result.email} with returned loginid as {result.id}')

    except:
        print("Exception caught while adding user email and password to UsersAccount Table")
        return False

    try:
        user.loginid = loginId
        db_session.add(user)
        db_session.commit()
    except:
        print("Exception caught while adding user record to Users Table")
        return False

    return True
# end addUserToDB

def queryUserAccountFromDB(colName="", value=""):
    #print(name)
    if db_session == None:
        initDB()
    
    #noOfRecords = 0

    try:
        look_for = '%{0}%'.format(value)
        rs = None
        if colName == "email":
            rs = db_session.query(UsersAccount).filter(UsersAccount.email.ilike(look_for))
        else:
            pass

    except:
        print("Exception caught while querying UserAccount from Database")
        return None

    #print("No.of Records matched:", noOfRecords)
    return rs
# end queryUserAccountFromDB

def queryUserFromDB(colName="", value=""):
    #print(name)
    if db_session == None:
        initDB()
    
    #noOfRecords = 0

    try:
        look_for = '%{0}%'.format(value)
        rs = None
        if colName == "email":
            rs = db_session.query(User).filter(User.email.ilike(look_for))
        if colName == "loginid":
            rs = db_session.query(User).filter(User.loginid.ilike(look_for))
        if colName == "fname":
            rs = db_session.query(User).filter(User.fname.ilike(look_for))
        if colName == "lname":
            rs = db_session.query(User).filter(User.lname.ilike(look_for))
        if colName == "city":
            rs = db_session.query(User).filter(User.city.ilike(look_for))
        if colName == "state":
            rs = db_session.query(User).filter(User.state.ilike(look_for))
        if colName == "country":
            rs = db_session.query(User).filter(User.country.ilike(look_for))
        else:
            pass

    except:
        print("Exception caught while querying User from Database")
        return None

    #print("No.of Records matched:", noOfRecords)
    return rs
# end queryUserFromDB