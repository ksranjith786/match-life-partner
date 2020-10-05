from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Sequence, ForeignKey, String, and_, or_

engine = None
Base = declarative_base()
db_session = None

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

def createDB(databaseURL):
    initDB(databaseURL)
    global Base
    Base.metadata.bind = engine
    Base.metadata.create_all(bind=engine)
# end createDB

def getDBSession():
    return db_session
# end getDBSession
