from email.policy import default
from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime
import decimal


class Provider(Base):

    __tablename__ = "providers"
     
    id = Column(BigInteger, primary_key=True, index=True)
    country_id = Column(BigInteger, default=0)
    name = Column(String, nullable=True)
    address = Column(String, nullable=True)
    description = Column(String, nullable=True)
    image = Column(String, nullable=True)
    provider_code = Column(String, nullable=True)
    test_api_key = Column(String, nullable=True)
    live_api_key = Column(String, nullable=True)
    test_base_url = Column(String, nullable=True)
    live_base_url = Column(String, nullable=True)
    test_login_username = Column(String, nullable=True)
    live_login_username = Column(String, nullable=True)
    test_login_password = Column(String, nullable=True)
    live_login_password = Column(String, nullable=True)
    test_secret_key = Column(String, nullable=True)
    live_secret_key = Column(String, nullable=True)
    test_public_key = Column(String, nullable=True)
    live_public_key = Column(String, nullable=True)
    auth_data = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    created_by = Column(BigInteger, default=0)
    date_created = Column(TIMESTAMP(timezone=True), nullable=True)


def create_provider(db: Session, country_id: int=0, name: str=None, address: str=None, description: str=None, image: str=None, provider_code: str=None, test_api_key: str=None, live_api_key: str=None, test_base_url: str=None, live_base_url: str=None, test_login_username: str=None, live_login_username: str=None, test_login_password: str=None, live_login_password: str=None, test_secret_key: str=None, live_secret_key: str=None, test_public_key: str=None, live_public_key: str=None, auth_data: str=None, status: int=0, created_by: int=0):
    provider = Provider(country_id=country_id, name=name, address=address, description=description, image=image, provider_code=provider_code, test_api_key=test_api_key, live_api_key=live_api_key, test_base_url=test_base_url, live_base_url=live_base_url, test_login_username=test_login_username, live_login_username=live_login_username, test_login_password=test_login_password, live_login_password=live_login_password, test_secret_key=test_secret_key, live_secret_key=live_secret_key, test_public_key=test_public_key, live_public_key=live_public_key, auth_data=auth_data, status=status, created_by=created_by, date_created=get_laravel_datetime())
    db.add(provider)
    db.commit()
    db.refresh(provider)
    return provider

def update_provider(db: Session, id: int=0, values: Dict={}):
    db.query(Provider).filter_by(id=id).update(values)
    db.commit()
    return True

def get_all_providers(db: Session):
    return db.query(Provider).all()

def get_single_porvider_by_id(db: Session, id: int=0):
    return db.query(Provider).filter(Provider.id == id).first()

def count_providers(db: Session):
    return db.query(Provider).count()