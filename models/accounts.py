from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Account(Base):

    __tablename__ = "accounts"
     
    id = Column(BigInteger, primary_key=True, index=True)
    agent_id = Column(BigInteger, default=0)
    provider_id = Column(BigInteger, default=0)
    account_type = Column(BigInteger, default=0)
    account_code = Column(String, nullable=True)
    bank_name = Column(String, nullable=True)
    bank_code = Column(String, nullable=True)
    account_name = Column(String, nullable=True)
    account_number = Column(String, nullable=True)
    balance = Column(Float, default=0)
    status = Column(SmallInteger, default=0)
    created_by = Column(BigInteger, default=0)
    date_created = Column(TIMESTAMP(timezone=True), nullable=True)


def create_account(db: Session, agent_id: int=0, provider_id: int=0, account_type: int=0, account_code: str=None, bank_name: str=None, bank_code: str=None, account_name: str=None, account_number: str=None, balance: float=0, status: int=0, created_by: int=0):
    account = Account(agent_id=agent_id, provider_id=provider_id, account_type=account_type, account_code=account_code, bank_name=bank_name, bank_code=bank_code, account_name=account_name, account_number=account_number, balance=balance, status=status, date_created=get_laravel_datetime())
    db.add(account)
    db.commit()
    db.refresh(account)
    return account

def update_account(db: Session, id: int=0, values: Dict={}):
    db.query(Account).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_accounts(db: Session):
    return db.query(Account).all()

def get_account_by_id(db: Session, id: int=0):
    return db.query(Account).filter(Account.id==id).first()
    
def count_account(db: Session):
    return db.query(Account).count()
    