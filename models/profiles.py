from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Profile(Base):

    __tablename__ = "profiles"
     
    id = Column(BigInteger, primary_key=True, index=True)
    agent_id = Column(BigInteger, default=0)
    first_name = Column(String, nullable=True)
    other_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    image = Column(String, nullable=True)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    phone_number_one = Column(String, nullable=True)
    phone_number_two = Column(String, nullable=True)
    date_created = Column(TIMESTAMP(timezone=True), nullable=True)


def create_profile(db: Session, agent_id: int=0, first_name: str=None, other_name: str=None, last_name: str=None, image: str=None, address: str=None, city: str=None, state: str=None, phone_number_one: str=None, phone_number_two: str=None):
    profile = Profile(first_name=first_name, other_name=other_name, last_name=last_name, image=image, address=address, city=city, state=state, phone_number_one=phone_number_one, phone_number_two=phone_number_two, date_created=get_laravel_datetime())
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile

def update_profile(db: Session, id: int=0, values: Dict={}):
    db.query(Profile).filter_by(id=id).update(values)
    db.commit()
    return True

    