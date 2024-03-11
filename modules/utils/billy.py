from typing import Dict
import random
import string
import requests
from settings.config import load_env_config
import json
from constant import SETTING_URL, CUSTOMER_URL, ACCOUNT_URL, TRANSACTION_URL

def send_to_account(endpoint: str=None, data: Dict={}, headers: Dict={}, request_type=1):
    if request_type == 1:
        url = ACCOUNT_URL + endpoint
        resp = requests.get(url=url, params=data, headers=headers)
        return resp.json()
    if request_type == 2:
        url = ACCOUNT_URL + endpoint
        resp = requests.post(url=url, json=data, headers=headers)
        return resp.json()
    return {
        'status_code': None,
        'data': None
    }

def send_to_customer(endpoint: str=None, data: Dict={}, headers: Dict={}, request_type=1):
    if request_type == 1:
        url = CUSTOMER_URL + endpoint
        resp = requests.get(url=url, params=data, headers=headers)
        return resp.json()
    if request_type == 2:
        url = CUSTOMER_URL + endpoint
        resp = requests.post(url=url, json=data, headers=headers)
        return resp.json()
    return {
        'status_code': None,
        'data': None
    }

def send_to_setting(endpoint: str=None, data: Dict={}, headers: Dict={}, request_type=1):
    if request_type == 1:
        url = SETTING_URL + endpoint
        resp = requests.get(url=url, params=data, headers=headers)
        return resp.json()
    if request_type == 2:
        url = SETTING_URL + endpoint
        resp = requests.post(url=url, json=data, headers=headers)
        return resp.json()
    return {
        'status_code': None,
        'data': None
    }

def send_to_transaction(endpoint: str=None, data: Dict={}, headers: Dict={}, request_type=1):
    if request_type == 1:
        url = TRANSACTION_URL + endpoint
        resp = requests.get(url=url, params=data, headers=headers)
        return resp.json()
    if request_type == 2:
        url = TRANSACTION_URL + endpoint
        resp = requests.post(url=url, json=data, headers=headers)
        return resp.json()
    return {
        'status_code': None,
        'data': None
    }