from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Industry(Base):

    __tablename__ = "industries"
     
    id = Column(BigInteger, primary_key=True, index=True)
    country_id = Column(BigInteger, default=0)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    industry_code = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    created_by = Column(BigInteger, default=0)
    date_created = Column(TIMESTAMP(timezone=True), nullable=True)


def create_industry(db: Session, country_id: int=0, name: str=None, description: str=None, industry_code: str=None, status: int=0, created_by: int=0):
    industry = Industry(country_id=country_id, name=name, description=description, industry_code=industry_code, status=status, created_by=created_by, date_created=get_laravel_datetime())
    db.add(industry)
    db.commit()
    db.refresh(industry)
    return industry

def update_industry(db: Session, id: int=0, values: Dict={}):
    db.query(Industry).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_industries(db: Session):
    return db.query(Industry).all()

def get_industry_by_id(db: Session, id: int=0):
    return db.query(Industry).filter(Industry.id==id).first()
    
def count_industries(db: Session):
    return db.query(Industry).count()
    