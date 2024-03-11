from sender import send_to_astutia
from modules.utils.flutterwave import flutterwave_get_bill_categories, flutterwave_validate_bill_service, flutterwave_make_bill_payment, flutterwave_get_bill_payment_status, flutterwave_get_all_payments

def get_bill_categories(gateway=1, bill_type=0, biller_code=''):
    if gateway == 1:
        if bill_type == 0:
            return flutterwave_get_bill_categories(airtime=1, data_bundle=1, power=1, internet=1, toll=1, cables=1, biller_code=biller_code)
        elif bill_type == 1:
            return flutterwave_get_bill_categories(airtime=1)
        elif bill_type == 2:
            return flutterwave_get_bill_categories(data_bundle=1)
        elif bill_type == 3:
            return flutterwave_get_bill_categories(power=1)
        elif bill_type == 4:
            return flutterwave_get_bill_categories(internet=1)
        elif bill_type == 5:
            return flutterwave_get_bill_categories(toll=1)
        elif bill_type == 6:
            return flutterwave_get_bill_categories(cables=1, biller_code=biller_code)
        elif bill_type == 7:
            return flutterwave_get_bill_categories(biller_code=biller_code)
        else:
            return []

def validate_bill_service(item_code=None, code=None, customer=None):
    return flutterwave_validate_bill_service(item_code=item_code, code=code, customer=customer)

def make_bill_payment(customer=None, amount=0, payment_type=None, reference=None, biller_name=None):
    return flutterwave_make_bill_payment(customer=customer, amount=amount, payment_type=payment_type, reference=reference, biller_name=biller_name)

def get_bill_transaction_status(reference=None):
    return flutterwave_get_bill_payment_status(reference=reference)