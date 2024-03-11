from database.model import create_name_enq, update_name_enq, update_name_enq_by_account_number, get_name_enq_by_account_number, get_last_account_number_name_enq, id_generator
from modules.utils.nibss import do_bank_list, do_name_enquiry, do_fund_transfer_credit, do_transaction_status
from modules.external.account import get_account_by_account_number, fund_transfer_debit_customer_account
from modules.external.settings import get_TSS_credit, get_TSS_debit
from modules.external.customer import get_customer_info_by_id
from sqlalchemy.orm import Session

from modules.utils.tools import generate_external_ref

def do_list_of_finanacial_institutions():
    resp = do_bank_list()
    if resp is None:
        return []
    else:
        if resp['status'] == True:
            data = resp['data']
            neresp = []
            if len(data) > 0:
                for i in range(len(data)):
                    val = {
                        'institution_name': data[i]['institution_name'],
                        'institution_code': data[i]['institution_code'],
                    }
                    neresp.append(val)
            return neresp
        else:
            []

def send_name_enquiry(db: Session, nuban: str=None, bank_code: str=None, channel: str=None):
    resp = do_name_enquiry(nuban=nuban, bank_code=bank_code, channel=channel)
    if resp is None:
        return {
            'status': False,
            'message': 'Unknow Error',
            'data': None
        }
    else:
        neresp = resp['data']
        if neresp['status'] == True:
            update_name_enq_by_account_number(db=db, account_number=nuban, values={'status': 1})
            reference = id_generator()
            create_name_enq(db=db, reference=reference, session_id=neresp['data']['SessionID'], account_number=nuban)
            neo = {
                'account_name': neresp['data']['AccountName'],
                'account_number': neresp['data']['AccountNumber'],
                'bvn': neresp['data']['BankVerificationNumber'],
                'kyc_level': neresp['data']['KYCLevel'],
            }
            return {
                'status': True,
                'message': 'Success',
                'data': neo
            }
        else:
            return {
                'status': False,
                'message': neresp['message'],
                'data': None
            }

def send_fund_transfer_direct_credit(db: Session, customer_id: int=0, branch_id: int=0, nuban: str=None, amount: float=0, channel_id: int=0, bank_code: str=None, narration: str=None, value_date: str=None, external_account_name: str=None, external_account_number: str=None, external_bvn: str=None, external_kyc_level: str=None, external_location: str=None, ip_address: str=None):
    ref = generate_external_ref()
    credit_account = get_TSS_debit()
    if credit_account == {}:
        return {
            'status': False,
            'message': 'TSS not found'
        }
    else:
        customer = get_customer_info_by_id(id=customer_id)
        if customer == {}:
            return {
                'status': False,
                'message': 'Customer not found',
            }
        else:
            account = get_account_by_account_number(account_number=nuban)
            if account == {}:
                return {
                    'status': False,
                    'message': 'Account not found'
                }
            else:
                available_balance = account['available_balance']
                if available_balance < amount:
                    return {
                        'status': False,
                        'message': 'Account balance is low'
                    }
                else:
                    name_enquiry = get_name_enq_by_account_number(db=db, account_number=external_account_number)
                    if name_enquiry is None:
                        return {
                            'status': False,
                            'message': 'Name Enquiry not found'
                        }
                    else:
                        account_name = account['account_name']
                        fund_transfer = do_fund_transfer_credit(name_enquiry_ref=name_enquiry.session_id, bank_code=bank_code, channel_code=str(channel_id), ben_account_name=external_account_name, ben_account_number=external_account_number, ben_bvn=external_bvn, ben_kyc=external_kyc_level, orig_account_name=account_name, orig_account_number=nuban, orig_account_bvn=customer['bvn'], orig_kyc_level="1", narration=narration, location=external_location, payment_ref=ref, amount=amount)
                        if fund_transfer is None:
                            return {
                                'status': False,
                                'message': 'Server not available'
                            }
                        else:
                            neresp = fund_transfer['data']
                            if neresp['status'] == False:
                                return {
                                    'status': False,
                                    'message': neresp['message']
                                }
                            else:
                                data = neresp['data']
                                respcode = data['ResponseCode']
                                if respcode != '00':
                                    return {
                                        'status': False,
                                        'message': 'Fund transfer failed'
                                    }
                                else:
                                    session_id = data['SessionID']
                                    ft = fund_transfer_debit_customer_account(nuban=nuban, gl_tss_number=credit_account['account_number'], branch_id=branch_id, channel_id=channel_id, reference=ref, narration=narration, amount=amount, value_date=value_date, ip_address=ip_address, external_session_id=session_id, external_account_name=external_account_name, external_account_number=external_account_number, external_bvn=external_bvn, external_kyc_level=external_kyc_level, external_bank_code=bank_code, external_location=external_location)
                                    if ft is None:
                                        return {
                                            'status': False,
                                            'message': 'Could not debit account'
                                        }
                                    else:
                                        if ft['status'] == False:
                                            return {
                                                'status': False,
                                                'message': ft['message']
                                            }
                                        else:
                                            return {
                                                'status': True,
                                                'message': 'Success'
                                            }

    