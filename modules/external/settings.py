from modules.utils.billy import send_to_setting

def get_TSS_bill():
    endpoint = "gl_bill"
    resp = send_to_setting(endpoint=endpoint)
    return resp
    
def get_TSS_bill_fee():
    endpoint = "gl_bill_fee"
    resp = send_to_setting(endpoint=endpoint)
    return resp