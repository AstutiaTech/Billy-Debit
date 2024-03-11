from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Company(Base):

    __tablename__ = "companies"
     
    id = Column(BigInteger, primary_key=True, index=True)
    country_id = Column(BigInteger, default=0)
    industry_id = Column(BigInteger, default=0)
    name = Column(String, nullable=True)
    address = Column(String, nullable=True)
    description = Column(String, nullable=True)
    company_code = Column(String, nullable=True)
    image = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    created_by = Column(BigInteger, default=0)
    date_created = Column(TIMESTAMP(timezone=True), nullable=True)


def create_company(db: Session, country_id: int=0, industry_id: int=0, name: str=None, address: str=None, description: str=None, company_code: str=None, image: str=None, status: int=0, created_by: int=0):
    company = Company(country_id=country_id, industry_id=industry_id, name=name, address=address, description=description, company_code=company_code, image=image, status=status, created_by=created_by, date_created=get_laravel_datetime())
    db.add(company)
    db.commit()
    db.refresh(company)
    return company

def update_company(db: Session, id: int=0, values: Dict={}):
    db.query(Company).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_companies(db: Session):
    return db.query(Company).all()

def get_company_by_id(db: Session, id: int=0):
    return db.query(Company).filter(Company.id==id).first()
    
def count_companies(db: Session):
    return db.query(Company).count()
    