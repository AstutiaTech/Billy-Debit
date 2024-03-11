from modules.utils.billy import send_to_customer

def get_customer_info_by_id(id: int=0):
    endpoint = "info/" + str(id)
    resp = send_to_customer(endpoint=endpoint)
    return resp