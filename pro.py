from modules.utils.remita import remita_generate_mandate, remita_print_mandate, remita_otp_mandate_activation_request, remita_otp_mandate_activation_validate, remita_mandate_status, remita_mandate_payment_history, remita_stop_mandate, remita_send_debit_instruction, remita_debit_status

# print(remita_generate_mandate(payer_name="OBINNA OPARA", payer_email="nnaopara@gmail.com", payer_phone_number="08178666383", payer_bank_code="057", payer_account_number="2265470215", amount=1000, start_date="07/11/2022", end_date="07/11/2023", mandate_type="DD", max_no_of_debit=3))
# print(remita_print_mandate(mandate_id="350009236495", request_id="5822406095888"))
print(remita_otp_mandate_activation_request(mandate_id="350009236495"))