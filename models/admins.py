from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Admin(Base):

    __tablename__ = "admins"
     
    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String, nullable=True)
    email = Column(String, nullable=True)
    password = Column(String, nullable=True)
    role = Column(Integer, default=0)
    status = Column(SmallInteger, default=0)
    created_by = Column(BigInteger, default=0)
    date_created = Column(TIMESTAMP(timezone=True), nullable=True)

def create_admin(db: Session, username: str=None, email: str=None, password: str=None, role: int=0, status: int=0, created_by: int=0):
    admin = Admin(username=username, email=email, password=password, role=role, status=status, date_created=get_laravel_datetime())
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin

def update_admin(db: Session, id: int=0, values: Dict={}):
    db.query(Admin).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_admins(db: Session):
    return db.query(Admin).all()

def get_admin_by_id(db: Session, id: int=0):
    return db.query(Admin).filter(Admin.id==id).first()
    
def count_admin(db: Session):
    return db.query(Admin).count()
    