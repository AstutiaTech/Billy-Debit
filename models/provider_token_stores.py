from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Provider_Token_Store(Base):

    __tablename__ = "provider_token_stores"
     
    id = Column(BigInteger, primary_key=True, index=True)
    provider_id = Column(BigInteger, default=0)
    token = Column(String, nullable=True)
    expiry_date = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    date_created = Column(TIMESTAMP(timezone=True), nullable=True)


def create_provider_token_store(db: Session, provider_id: int=0, token: str=None, expiry_date: str=None, status: int=0):
    pts = Provider_Token_Store(provider_id=provider_id, token=token, expiry_date=expiry_date, status=status, date_created=get_laravel_datetime())
    db.add(pts)
    db.commit()
    db.refresh(pts)
    return pts

def update_provider_token_store(db: Session, id: int=0, values: Dict={}):
    db.query(Provider_Token_Store).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_pts(db: Session):
    return db.query(Provider_Token_Store).all()

def get_pts_by_id(db: Session, id: int=0):
    return db.query(Provider_Token_Store).filter(Provider_Token_Store.id==id).first()
    
def get_pts_by_provider_id(db: Session, provider_id: int=0):
    return db.query(Provider_Token_Store).filter(Provider_Token_Store.provider_id==provider_id).all()

def get_pts_by_provider_id_and_status(db: Session, provider_id: int=0, status: int=0):
    return db.query(Provider_Token_Store).filter(and_(Provider_Token_Store.provider_id==provider_id, Provider_Token_Store.status==status)).order_by(desc(Provider_Token_Store.id)).first()

def count_pts(db: Session):
    return db.query(Provider_Token_Store).count()
    