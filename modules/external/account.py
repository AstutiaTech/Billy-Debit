from modules.utils.billy import send_to_account

def get_account_by_account_number(account_number: str=None):
    endpoint = "account_by_account_number/" + str(account_number)
    resp = send_to_account(endpoint=endpoint)
    return resp

def fund_transfer_debit_customer_account(nuban: str=None, gl_tss_number: str=None, branch_id: int=0, channel_id: int=0, reference: str=None, narration: str=None, amount: float=0, value_date: str=None, ip_address: str=None, external_session_id: str=None, external_account_name: str=None, external_account_number: str=None, external_bvn: str=None, external_kyc_level: str=None, external_bank_code: str=None, external_location: str=None):
    data = {
        'from_account_number': nuban,
        'to_account_number': gl_tss_number,
        'branch_id': branch_id,
        'channel_id': channel_id,
        'reference': reference,
        'narration': narration,
        'amount': amount,
        'value_date': value_date,
        'ip_address': ip_address,
        'external_session_id': external_session_id,
        'external_account_name': external_account_name,
        'external_account_number': external_account_number,
        'external_bvn': external_bvn,
        'external_kyc_level': external_kyc_level,
        'external_bank_code': external_bank_code,
        'external_location': external_location,
        'is_external': 1,
    }
    endpoint = "debit"
    resp = send_to_account(endpoint=endpoint, data=data, request_type=2)
    return resp
        
def fund_transfer_debit_customer_account_external(nuban: str=None, channel_id: int=0, reference: str=None, narration: str=None, amount: float=0, commission: float=0, value_date: str=None, ip_address: str=None, external_biller_name: str=None, external_biller_customer_id: str=None, is_airtime_data: int=0):
    data = {
        'from_account_number': nuban,
        'channel_id': channel_id,
        'reference': reference,
        'narration': narration,
        'amount': amount,
        'transaction_commission': commission,
        'value_date': value_date,
        'ip_address': ip_address,
        'external_biller_name': external_biller_name,
        'external_biller_customer_id': external_biller_customer_id,
        'is_bills': 1,
        'is_airtime_data': is_airtime_data,
    }
    endpoint = "debit_external"
    resp = send_to_account(endpoint=endpoint, data=data, request_type=2)
    return resp