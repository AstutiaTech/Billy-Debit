from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pyodbc
import sqlalchemy as sa

SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc://DESKTOP-6T5DDMB\OLUKEYE/BillsDB?driver=SQL+Server+Native+Client+11.0"
engine = sa.create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


 # Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()