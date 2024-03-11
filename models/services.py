from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Service(Base):

    __tablename__ = "services"
     
    id = Column(BigInteger, primary_key=True, index=True)
    category_id = Column(BigInteger, default=0)
    company_id = Column(BigInteger, default=0)
    provider_id = Column(BigInteger, default=0)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    label_name = Column(String, nullable=True)
    service_code = Column(String, nullable=True)
    fw_biller_name = Column(String, nullable=True)
    fw_biller_code = Column(String, nullable=True)
    fw_item_code = Column(String, nullable=True)
    amount = Column(Float, default=0)
    is_flat = Column(SmallInteger, default=0)
    is_airtime = Column(SmallInteger, default=0)
    commision_on_fee = Column(SmallInteger, default=0)
    fee = Column(Float, default=0)
    commission = Column(Float, default=0)
    min_amount = Column(Float, default=0)
    max_amount = Column(Float, default=0)
    status = Column(SmallInteger, default=0)
    created_by = Column(BigInteger, default=0)
    date_created = Column(TIMESTAMP(timezone=True), nullable=True)


def create_services(db: Session, category_id: int=0, company_id: int=0, provider_id: int=0, name: str=None, description: str=None, label_name: str=None, service_code: str=None, fw_biller_name: str=None, fw_biller_code: str=None, fw_item_code: str=None, amount: float=0, is_flat: int=0, is_airtime: int=0, commision_on_fee: int=0, fee: float=0, commission: float=0, min_amount: float=0, max_amount: float=0, status: int=0, created_by: int=0):
    service = Service(category_id=category_id, company_id=company_id, provider_id=provider_id, name=name, description=description, label_name=label_name, service_code=service_code, fw_biller_name=fw_biller_name, fw_biller_code=fw_biller_code, fw_item_code=fw_item_code, amount=amount, is_flat=is_flat, is_airtime=is_airtime, commision_on_fee=commision_on_fee, fee=fee, commission=commission, min_amount=min_amount, max_amount=max_amount, status=status, created_by=created_by, date_created=get_laravel_datetime())
    db.add(service)
    db.commit()
    db.refresh(service)
    return service

def update_service(db: Session, id: int=0, values: Dict={}):
    db.query(Service).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_services(db: Session):
    return db.query(Service).all()

def get_services_by_category(db: Session, category_id: int=0):
    return db.query(Service).filter(Service.category_id==category_id).all()

def get_service_by_id(db: Session, id: int=0):
    return db.query(Service).filter(Service.id==id).first()

def get_service_by_code(db: Session, code: str=None):
    return db.query(Service).filter(Service.service_code==code).first()
    
def count_services(db: Session):
    return db.query(Service).count()
    