from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

database_connect ='mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (
    'root', #username
    '', #password
    'localhost', #host
    'py_web_app_sample',    #database name
)

engine = create_engine(database_connect,encoding="utf-8",echo=True)
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine   
    )
)

Base = declarative_base()
Base.query = db_session.query_property()
