from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Transaction(Base):

    __tablename__ = "transactions"
     
    id = Column(BigInteger, primary_key=True, index=True)
    country_id = Column(BigInteger, default=0)
    agent_id = Column(BigInteger, default=0)
    provider_id = Column(BigInteger, default=0)
    account_id = Column(BigInteger, default=0)
    service_id = Column(BigInteger, default=0)
    reference = Column(String, nullable=True)
    external_reference = Column(String, nullable=True)
    external_session_id = Column(String, nullable=True)
    external_token = Column(String, nullable=True)
    transaction_type = Column(Integer, default=0)
    amount = Column(Float, default=0)
    fee = Column(Float, default=0)
    status = Column(SmallInteger, default=0)
    date_created = Column(TIMESTAMP(timezone=True), nullable=True)


def create_transaction(db: Session, country_id: int=0, agent_id: int=0, provider_id: int=0, account_id: int=0, service_id: int=0, reference: str=None, external_reference: str=None, external_session_id: str=None, external_token: str=None, transaction_type: int=0, amount: float=0, fee: float=0, status: int=0):
    transaction = Transaction(country_id=country_id, agent_id=agent_id, provider_id=provider_id, account_id=account_id, service_id=service_id, reference=reference, external_reference=external_reference, external_session_id=external_session_id, external_token=external_token, transaction_type=transaction_type, amount=amount, fee=fee, status=status,date_created=get_laravel_datetime())
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

def update_transaction(db: Session, id: int=0, values: Dict={}):
    db.query(Transaction).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_transactions(db: Session):
    return db.query(Transaction).all()

def get_transaction_by_id(db: Session, id: int=0):
    return db.query(Transaction).filter(Transaction.id==id).first()

def get_transaction_by_reference(db: Session, reference: str=None):
    return db.query(Transaction).filter(Transaction.reference==reference).first()
    
def count_transactions(db: Session):
    return db.query(Transaction).count()
    