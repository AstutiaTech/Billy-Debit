from typing import List, Dict
import requests
from settings.config import load_env_config
from sqlalchemy.orm import Session
from database.model import create_provider_token_store, get_pts_by_provider_id_and_status
import time
from datetime import datetime
import dateparser
import hashlib
import random
from modules.utils.tools import json_loader

config = load_env_config()

# def send_to_remita(endpoint=None, data={}, request_type=1, headers={}):
#     url = config['remita_url'] + str(endpoint)
#     headers['Content-Type'] = 'application/json'
#     if request_type == 1:
#         response = requests.get(url=url, params=data, headers=headers)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return None
#     elif request_type == 2:
#         response = requests.post(url=url, data=data, headers=headers)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return None
#     else:
#         return None

# def generate_remita_token():
#     endpoint = "remita/exapp/api/v1/send/api/uaasvc/uaa/token"
#     data = {
#         'username': config['remita_username'],
#         'password': config['remita_password'],
#     }
#     return send_to_remita(endpoint=endpoint, data=data, request_type=2)

# def manage_new_remita_token(db: Session):
#     token_req = generate_remita_token()
#     if token_req is None:
#         return {
#             'status': False,
#             'message': 'Failed Request',
#             'data': None
#         }
#     else:
#         if 'status' not in token_req:
#             return {
#                 'status': False,
#                 'message': 'Unknown reponse format',
#                 'data': None
#             }
#         else:
#             if token_req['status'] != "00": 
#                 return {
#                     'status': False,
#                     'message': 'Failed',
#                     'data': None
#                 }
#             else:
#                 token_data = token_req['data']
#                 data = token_data[0]['accessToken']
#                 expr = token_data[0]['expiresIn']
#                 expiry_date = datetime.fromtimestamp(expr).strftime("%Y-%m-%d %H:%M:%S")
#                 create_provider_token_store(db=db, provider_id=3, token=data, expiry_date=expiry_date, status=1)
#                 return {
#                     'status': True,
#                     'message': 'Success',
#                     'data': data
#                 }


# def get_remita_token(db: Session):
#     pts = get_pts_by_provider_id_and_status()
#     if pts is None:
#         val_dat = manage_new_remita_token(db=db)
#         if val_dat['status'] == False:
#             return {
#                 'status': False,
#                 'message': val_dat['message'],
#                 'token': None
#             }
#         else:
#             return {
#                 'status': True,
#                 'message': 'Success',
#                 'token': val_dat['data'],
#             }
#     else:
#         currtime = int(time.time)
#         pts_expiry = pts.expiry_date
#         expiry_date = dateparser.parse(pts_expiry, settings={'TIMEZONE': 'Africa/Lagos'})
#         expr = int(expiry_date.timestamp())
#         if currtime > expr:
#             val_dat = manage_new_remita_token(db=db)
#             if val_dat['status'] == False:
#                 return {
#                     'status': False,
#                     'message': val_dat['message'],
#                     'token': None
#                 }
#             else:
#                 return {
#                     'status': True,
#                     'message': 'Success',
#                     'token': val_dat['data'],
#                 }
#         else:
#             return {
#                 'status': True,
#                 'message': 'Success',
#                 'token': pts.token
#             }

# def make_remita_request(db: Session, endpoint=None, data={}, request_type=1):
#     token_gen = get_remita_token(db=db)
#     if token_gen['status'] == False:
#         return {
#             'status': False,
#             'message': 'Reason: ' + token_gen['message'],
#             'data': None,
#         }
#     else:
#         token = token_gen['token']
#         headers = {

#         }

def generate_request_id():
    return str(random.randint(1111111111111, 9999999999999))

def generate_request_timestamp():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S+%f")

def remita_generate_mandate(payer_name: str=None, payer_email: str=None, payer_phone_number: str=None, payer_bank_code: str=None, payer_account_number: str=None, amount: float=0, start_date: str=None, end_date: str=None, mandate_type: str=None, max_no_of_debit: int=0):
    request_id = generate_request_id()
    raw_hash_str = config['remita_merchant_id'] + config['remita_service_type'] + request_id + str(amount) + config['remita_api_key']
    mandate_hash = hashlib.sha512(str(raw_hash_str).encode('utf-8')).hexdigest()
    data = {
        "merchantId": config['remita_merchant_id'],
        "serviceTypeId": config['remita_service_type'],
        "requestId": request_id,
        "hash": mandate_hash,
        "payerName": payer_name,
        "payerEmail": payer_email,
        "payerPhone": payer_phone_number,
        "payerBankCode": payer_bank_code,
        "payerAccount": payer_account_number,
        "amount": str(amount),
        "startDate": start_date,
        "endDate": end_date,
        "mandateType": mandate_type,
        "maxNoOfDebits": max_no_of_debit,
    }
    headers = {
        'Content-Type': 'application/json'
    }
    url = config['remita_url'] + 'remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/setup'
    response = requests.post(url=url, json=data, headers=headers)
    return {
        'status_code': response.status_code,
        'data': json_loader(jstr=response.text)
    }

def remita_print_mandate(mandate_id: str=None, request_id: str=None):
    # request_id = generate_request_id()
    raw_hash_str = config['remita_merchant_id'] + config["remita_api_key"] + request_id
    api_hash = hashlib.sha512(str(raw_hash_str).encode('utf-8')).hexdigest()
    headers = {
        'Content-Type': 'application/json'
    }
    url = config['remita_url'] + 'ecomm/mandate/form/27768931/' + str(api_hash) +"/" + str(mandate_id) + "/" + str(request_id) + "/rest.reg"
    response = requests.get(url=url, headers=headers)
    return {
        'status_code': response.status_code,
        'data': response.text
    }

def remita_otp_mandate_activation_request(mandate_id: str=None):
    request_id = generate_request_id()
    request_timestamp = generate_request_timestamp()
    raw_hash_str = config["remita_api_key"] + request_id + config['remita_token']
    api_hash = hashlib.sha512(str(raw_hash_str).encode('utf-8')).hexdigest()
    data = {
        'mandateId': mandate_id,
        'requestId': request_id,
    }
    headers = {
        'Content-Type': 'application/json',
        'MERCHANT_ID': config['remita_merchant_id'],
        'API_KEY': config['remita_api_key'],
        'REQUEST_ID': request_id,
        'REQUEST_TS': request_timestamp,
        'API_DETAILS_HASH': api_hash,
    }
    print(headers)
    url = config['remita_url'] + 'remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/requestAuthorization'
    response = requests.post(url=url, data=data, headers=headers)
    return {
        'status_code': response.status_code,
        'data': json_loader(jstr=response.text)
    }

def remita_otp_mandate_activation_validate(trans_ref: str=None, auth_params: List=[]):
    request_id = generate_request_id()
    request_timestamp = generate_request_timestamp()
    raw_hash_str = config["remita_api_key"] + request_id + config['remita_token']
    api_hash = hashlib.sha512(str(raw_hash_str).encode('utf-8')).hexdigest()
    data = {
        'remitaTransRef': trans_ref,
        'authParams': auth_params,
    }
    headers = {
        'Content-Type': 'application/json',
        'MERCHANT_ID': config['remita_merchant_id'],
        'API_KEY': config['remita_api_key'],
        'REQUEST_ID': request_id,
        'REQUEST_TS': request_timestamp,
        'API_DETAILS_HASH': api_hash,
    }
    url = config['remita_url'] + 'remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/validateAuthorization'
    response = requests.post(url=url, data=data, headers=headers)
    return {
        'status_code': response.status_code,
        'data': json_loader(jstr=response.text)
    }

def remita_mandate_status(mandate_id: str=None):
    request_id = generate_request_id()
    raw_hash_str = mandate_id + config['remita_merchant_id'] + request_id + config['remita_api_key']
    api_hash = hashlib.sha512(str(raw_hash_str).encode('utf-8')).hexdigest()
    data = {
        'merchantId': config['remita_merchant_id'],
        'mandateId': mandate_id,
        'hash': api_hash,
        'requestId': request_id,
    }
    headers = {
        'Content-Type': 'application/json',
    }
    url = config['remita_url'] + 'remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/status'
    response = requests.post(url=url, data=data, headers=headers)
    return {
        'status_code': response.status_code,
        'data': json_loader(jstr=response.text)
    }

def remita_mandate_payment_history(mandate_id: str=None):
    request_id = generate_request_id()
    raw_hash_str = mandate_id + config['remita_merchant_id'] + request_id + config['remita_api_key']
    api_hash = hashlib.sha512(str(raw_hash_str).encode('utf-8')).hexdigest()
    data = {
        'merchantId': config['remita_merchant_id'],
        'mandateId': mandate_id,
        'hash': api_hash,
        'requestId': request_id,
    }
    headers = {
        'Content-Type': 'application/json',
    }
    url = config['remita_url'] + 'remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/payment/history'
    response = requests.post(url=url, data=data, headers=headers)
    return {
        'status_code': response.status_code,
        'data': json_loader(jstr=response.text)
    }

def remita_stop_mandate(mandate_id: str):
    request_id = generate_request_id()
    raw_hash_str = mandate_id + config['remita_merchant_id'] + request_id + config['remita_api_key']
    api_hash = hashlib.sha512(str(raw_hash_str).encode('utf-8')).hexdigest()
    data = {
        'merchantId': config['remita_merchant_id'],
        'mandateId': mandate_id,
        'hash': api_hash,
        'requestId': request_id,
    }
    headers = {
        'Content-Type': 'application/json',
    }
    url = config['remita_url'] + 'remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/stop'
    response = requests.post(url=url, data=data, headers=headers)
    return {
        'status_code': response.status_code,
        'data': json_loader(jstr=response.text)
    }

def remita_send_debit_instruction(mandate_id: str=None, amount: float=0, account_number: str=None, bank_code: str=None):
    request_id = generate_request_id()
    raw_hash_str = config['remita_merchant_id'] + config['remita_service_type'] + request_id + str(amount) + config['remita_api_key']
    api_hash = hashlib.sha512(str(raw_hash_str).encode('utf-8')).hexdigest()
    data = {
        'merchantId': config['remita_merchant_id'],
        'serviceTypeId': config['remita_service_type'],
        'mandateId': mandate_id,
        'hash': api_hash,
        'requestId': request_id,
        'totalAmount': str(amount),
        'fundingAccount': account_number,
        'fundingBankCode': bank_code,
    }
    headers = {
        'Content-Type': 'application/json',
    }
    url = config['remita_url'] + 'remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/payment/send'
    response = requests.post(url=url, data=data, headers=headers)
    return {
        'status_code': response.status_code,
        'data': json_loader(jstr=response.text)
    }

def remita_debit_status(mandate_id: str=None):
    request_id = generate_request_id()
    raw_hash_str = mandate_id + config['remita_merchant_id'] + request_id + config['remita_api_key']
    api_hash = hashlib.sha512(str(raw_hash_str).encode('utf-8')).hexdigest()
    data = {
        'merchantId': config['remita_merchant_id'],
        'mandateId': mandate_id,
        'hash': api_hash,
        'requestId': request_id,
    }
    headers = {
        'Content-Type': 'application/json',
    }
    url = config['remita_url'] + 'remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/payment/status'
    response = requests.post(url=url, data=data, headers=headers)
    return {
        'status_code': response.status_code,
        'data': json_loader(jstr=response.text)
    }