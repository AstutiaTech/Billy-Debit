from modules.utils.billy import send_to_transaction

def approve_transaction(id: int=0, external_biller_token: str=None):
    data = {
        'id': id,
        'external_biller_token': external_biller_token,
    }
    endpoint = "approve_bill_transaction"
    resp = send_to_transaction(endpoint=endpoint, data=data, request_type=2)
    return resp

def cancel_transaction(id: int=0):
    data = {
        'id': id,
    }
    endpoint = "cancel_bill_transaction"
    resp = send_to_transaction(endpoint=endpoint, data=data, request_type=2)
    return resp