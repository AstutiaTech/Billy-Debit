from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Name_Enquiry(Base):

    __tablename__ = "name_enquiries"
     
    id = Column(BigInteger, primary_key=True, index=True)
    reference = Column(String, nullable=True)
    session_id = Column(String, nullable=True)
    account_number = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    date_created = Column(TIMESTAMP(timezone=True), nullable=True)


def create_name_enq(db: Session, reference: str=None, session_id: str=None, account_number: str=None, status: int=0):
    name_enq = Name_Enquiry(reference=reference, session_id=session_id, account_number=account_number, status=status, date_created=get_laravel_datetime())
    db.add(name_enq)
    db.commit()
    db.refresh(name_enq)
    return name_enq

def update_name_enq(db: Session, id: int=0, values: Dict={}):
    db.query(Name_Enquiry).filter_by(id=id).update(values)
    db.commit()
    return True

def update_name_enq_by_reference(db: Session, reference: str=None, values: Dict={}):
    db.query(Name_Enquiry).filter_by(reference=reference).update(values)
    db.commit()
    return True

def update_name_enq_by_session_id(db: Session, session_id: str=None, values: Dict={}):
    db.query(Name_Enquiry).filter_by(session_id=session_id).update(values)
    db.commit()
    return True

def update_name_enq_by_account_number(db: Session, account_number: str=None, values: Dict={}):
    db.query(Name_Enquiry).filter_by(account_number=account_number).update(values)
    db.commit()
    return True

def get_all_name_enq(db: Session):
    return db.query(Name_Enquiry).all()

def get_name_enq_by_id(db: Session, id: int=0):
    return db.query(Name_Enquiry).filter(Name_Enquiry.id==id).first()

def get_name_enq_by_reference(db: Session, reference: str=None):
    return db.query(Name_Enquiry).filter(Name_Enquiry.reference==reference).first()

def get_name_enq_by_account_number(db: Session, account_number: str=None):
    return db.query(Name_Enquiry).filter(Name_Enquiry.account_number==account_number).first()

def get_last_account_number_name_enq(db: Session, account_number: str=None):
    return db.query(Name_Enquiry).filter(and_(Name_Enquiry.account_number==account_number, Name_Enquiry.status == 0)).order_by(desc(Name_Enquiry.id)).first()
    
def count_name_enq(db: Session):
    return db.query(Name_Enquiry).count()
    
def count_name_enq_by_account_number(db: Session, account_number: str=None):
    return db.query(Name_Enquiry).filter(Name_Enquiry.account_number==account_number).count()
    