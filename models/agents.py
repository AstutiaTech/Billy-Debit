from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Agent(Base):

    __tablename__ = "agents"
     
    id = Column(BigInteger, primary_key=True, index=True)
    country_id = Column(BigInteger, default=0)
    username = Column(String, nullable=True)
    email = Column(String, nullable=True)
    password = Column(String, nullable=True)
    test_api_key = Column(String, nullable=True)
    live_api_key = Column(String, nullable=True)
    verified = Column(SmallInteger, default=0)
    status = Column(SmallInteger, default=0)
    created_by = Column(BigInteger, default=0)
    date_created = Column(TIMESTAMP(timezone=True), nullable=True)


def create_agents(db: Session, country_id: int=0, username: str=None, email: str=None, password: str=None, test_api_key: str=None, live_api_key: str=None, status: int=0, created_by: int=0):
    agent = Agent(country_id=country_id, username=username, email=email, password=password, test_api_key=test_api_key, live_api_key=live_api_key, status=status, date_created=get_laravel_datetime())
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent

def update_agent(db: Session, id: int=0, values: Dict={}):
    db.query(Agent).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_agents(db: Session):
    return db.query(Agent).all()

def get_agent_by_id(db: Session, id: int=0):
    return db.query(Agent).filter(Agent.id==id).first()
    
def count_agent(db: Session):
    return db.query(Agent).count()
    