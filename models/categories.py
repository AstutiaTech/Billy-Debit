from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Category(Base):

    __tablename__ = "categories"
     
    id = Column(BigInteger, primary_key=True, index=True)
    country_id = Column(BigInteger, default=0)
    industry_id = Column(BigInteger, default=0)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    category_code = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    created_by = Column(BigInteger, default=0)
    date_created = Column(TIMESTAMP(timezone=True), nullable=True)


def create_category(db: Session, country_id: int=0, industry_id: int=0, name: str=None, description: str=None, category_code: str=None, status: int=0, created_by: int=0):
    category = Category(country_id=country_id, industry_id=industry_id, name=name, description=description, category_code=category_code, status=status, created_by=created_by, date_created=get_laravel_datetime())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def update_category(db: Session, id: int=0, values: Dict={}):
    db.query(Category).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_categories(db: Session):
    return db.query(Category).all()

def get_category_by_id(db: Session, id: int=0):
    return db.query(Category).filter(Category.id==id).first()
    
def count_category(db: Session):
    return db.query(Category).count()
    