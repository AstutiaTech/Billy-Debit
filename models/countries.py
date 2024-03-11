from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Country(Base):

    __tablename__ = "countries"
     
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String, nullable=True)
    language = Column(String, nullable=True)
    code = Column(String, nullable=True)
    code_two = Column(String, nullable=True)
    area_code = Column(String, nullable=True)
    currency = Column(String, nullable=True)
    currency_short_code = Column(String, nullable=True)
    currency_code = Column(String, nullable=True)
    base_timezone = Column(String, nullable=True)
    image = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    created_by = Column(BigInteger, default=0)
    date_created = Column(TIMESTAMP(timezone=True), nullable=True)


def create_country(db: Session, name: str=None, language: str=None, code: str=None, code_two: str=None, area_code: str=None, currency: str=None, currency_short_code: str=None, currency_code: str=None, base_timezone: str=None, image: str=None, status: int=0, created_by: int=0):
    country = Country(name=name, language=language, code=code, code_two=code_two, area_code=area_code, currency=currency, currency_short_code=currency_short_code, currency_code=currency_code, base_timezone=base_timezone, image=image, status=status, created_by=created_by, date_created=get_laravel_datetime())
    db.add(country)
    db.commit()
    db.refresh(country)
    return country

def update_country(db: Session, id: int=0, values: Dict={}):
    db.query(Country).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_countries(db: Session):
    return db.query(Country).all()

def get_country_by_id(db: Session, id: int=0):
    return db.query(Country).filter(Country.id==id).first()
    
def count_countries(db: Session):
    return db.query(Country).count()
    