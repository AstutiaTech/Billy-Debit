import requests
import dateparser
import time
from datetime import datetime, timedelta
from settings.config import load_env_config

config = load_env_config()

def send_to_flutterwave(endpoint=None, data={}, request_type=1):
    url = config['flutterwave_url'] + str(endpoint)
    headers = {
        'Authorization': 'Bearer ' + str(config['flutterwave_secret_key']),
        'Content-Type': 'application/json',
    }
    if request_type == 1:
        response = requests.get(url=url, params=data, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    elif request_type == 2:
        response = requests.post(url=url, data=data, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    else:
        return None

def flutterwave_get_bill_categories(airtime=0, data_bundle=0, power=0, internet=0, toll=0, biller_code='', cables=0):
    endpoint = "bill-categories"
    data = {
        'airtime': airtime,
        'data_bundle': data_bundle,
        'power': power,
        'internet': internet,
        'toll': toll,
        'biller_code': biller_code,
        'cables': cables
    }
    return send_to_flutterwave(endpoint=endpoint, data=data, request_type=1)

def flutterwave_validate_bill_service(item_code=None, code=None, customer=None):
    endpoint = "bill-items/" + str(item_code) + "/validate"
    data = {
        'code': code,
        'customer': customer,
    }
    return send_to_flutterwave(endpoint=endpoint, data=data, request_type=1)

def flutterwave_make_bill_payment(customer=None, amount=0, payment_type=None, reference=None, biller_name=None):
    endpoint = "bills"
    data = {
        'country': "NG",
        'recurrence': "ONCE",
        'customer': str(customer),
        'amount': amount,
        'type': payment_type,
        'reference': reference,
        'biller_name': biller_name
    }
    return send_to_flutterwave(endpoint=endpoint, data=data, request_type=2)

def flutterwave_get_bill_payment_status(reference=None, verbose=1):
    endpoint = "bills/" + str(reference)
    data = {
        'verbose': verbose
    }
    return send_to_flutterwave(endpoint=endpoint, data=data, request_type=1)

def flutterwave_get_all_payments(from_date=None, to_date=None, page=1, reference=None):
    str_format = "%Y-%m-%d"
    if from_date == None:
        d = datetime.today() - timedelta(days=14)
        from_date = d.strftime(str_format)
    if to_date == None:
        t = datetime.today()
        to_date = t.strftime(str_format)
    from_date_el = dateparser.parse(from_date, settings={'TIMEZONE': 'Africa/Lagos'})
    to_date_el = dateparser.parse(to_date, settings={'TIMEZONE': 'Africa/Lagos'})
    from_tuple = from_date_el.timetuple()
    to_tuple = to_date_el.timetuple()
    from_fin = time.strftime(str_format, from_tuple)
    to_fin = time.strftime(str_format, to_tuple)
    endpoint = "bills"
    data = {
        'from': from_fin,
        'to': to_fin,
        'page': page,
        'reference': reference,
    }
    return send_to_flutterwave(endpoint=endpoint, data=data, request_type=1)

def get_all_nigerian_banks():
    endpoint = "banks/NG"
    data = {}
    return send_to_flutterwave(endpoint=endpoint, data=data, request_type=1)

def resolve_account_details(account_number='', account_bank=''):
    endpoint = "accounts/resolve"
    data = {
        'account_number': account_number,
        'account_bank': account_bank
    }
    return send_to_flutterwave(endpoint=endpoint, data=data, request_type=2)

def initiate_flutterwave_transfer(account_bank='', account_number='', amount=0, narration='', beneficiary_name='', reference=''):
    endpoint = "transfers"
    data = {
        'account_bank': account_bank,
        'account_number': account_number,
        'amount': amount,
        'narration': narration,
        'currency': "NGN",
        'reference': reference,
        'beneficiary_name': beneficiary_name
    }
    return send_to_flutterwave(endpoint=endpoint, data=data, request_type=2)

def transfer_retry(transfer_id=0):
    endpoint = "transfers/" + str(transfer_id) + "/retries" 
    data = {}
    return send_to_flutterwave(endpoint=endpoint, data=data, request_type=2)

def initiate_bulk_transfer(title='', bulk_data=[]):
    endpoint = "bulk-transfers"
    data = {
        'title': title,
        'bulk_data': bulk_data
    }
    return send_to_flutterwave(endpoint=endpoint, data=data, request_type=2)

def get_transfer_fee(amount=0):
    endpoint = "transfers/fee"
    data = {
        'amount': amount,
        'currency': 'NGN',
        'type': 'account'
    }
    return send_to_flutterwave(endpoint=endpoint, data=data, request_type=1)

def get_all_transfers(page=1, status=''):
    endpoint = "transfers"
    data = {
        'page': page,
        'status': status
    }
    return send_to_flutterwave(endpoint=endpoint, data=data, request_type=1)

def get_single_transfer(transfer_id=0):
    endpoint = "transfers/" + str(transfer_id)
    data = {}
    return send_to_flutterwave(endpoint=endpoint, data=data, request_type=1)