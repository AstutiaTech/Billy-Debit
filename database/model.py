from models.accounts import Account, create_account, update_account, get_all_accounts, get_account_by_id, count_account
from models.admins import Admin, create_admin, update_admin, get_all_admins, get_admin_by_id, count_admin
from models.agents import Agent, create_agents, update_agent, get_all_agents, get_agent_by_id, count_agent
from models.categories import Category, create_category, update_category, get_all_categories, get_category_by_id, count_category
from models.companies import Company, create_company, update_company, get_all_companies, get_company_by_id, count_companies
from models.countries import Country, create_country, update_country, get_all_countries, get_country_by_id, count_countries
from models.customers import Customer, create_customer, update_customer, get_all_customers, get_customer_by_id, count_customers
from models.industries import Industry, create_industry, update_industry, get_all_industries, get_industry_by_id, count_industries
from models.name_enquiries import Name_Enquiry, create_name_enq, update_name_enq, update_name_enq_by_reference, update_name_enq_by_session_id, update_name_enq_by_account_number, get_all_name_enq, get_name_enq_by_id, get_name_enq_by_reference, get_name_enq_by_account_number, get_last_account_number_name_enq, count_name_enq, count_name_enq_by_account_number
from models.profiles import Profile, create_profile, update_profile
from models.provider_token_stores import Provider_Token_Store, create_provider_token_store, update_provider_token_store, get_all_pts, get_pts_by_id, get_pts_by_provider_id_and_status, get_pts_by_provider_id, count_pts
from models.providers import create_provider, update_provider, get_all_providers, get_single_porvider_by_id, count_providers
from models.services import Service, create_services, update_service, get_all_services, get_services_by_category, get_service_by_id, get_service_by_code, count_services
from models.transactions import Transaction, create_transaction, update_transaction, get_all_transactions, get_transaction_by_id, get_transaction_by_reference, count_transactions
import string
import random
from sqlalchemy.orm import Session

def id_generator(size=25, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
