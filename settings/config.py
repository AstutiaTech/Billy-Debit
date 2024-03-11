from dotenv import load_dotenv
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

path = os.path.join(BASEDIR, '.env')

load_dotenv(path)

def load_env_config():
    return {
        'server': os.getenv("DATABASE_SERVER"),
        'database': os.getenv("DATABASE"),
        'database_user': os.getenv("DATABASE_USERNAME"),
        'database_pass': os.getenv("DATABASE_PASSWORD"),
        'cleardb_database_url': os.getenv("CLEARDB_DATABASE_URL"),
        'database_string': os.getenv("DATABASE_STRING"),
        'secret_key': os.getenv("ACCESS_SECRET_KEY"),
        'password_salt': os.getenv("ACCESS_SALT"),
        'vanso_username': os.getenv('VANSO_USERNAME'),
        'vanso_password': os.getenv('VANSO_PASSWORD'),
        'vanso_url': os.getenv('VANSO_URL'),
        'vanso_sender_id': os.getenv('VANSO_SENDER_ID'),
        'nip_server': os.getenv('NIP_SERVER'),
        'flutterwave_url': os.getenv('FLUTTERWAVE_URL'),
        'flutterwave_public_key': os.getenv('FLUTTERWAVE_PUBLIC_KEY'),
        'flutterwave_secret_key': os.getenv('FLUTTERWAVE_SECRET_KEY'),
        'flutterwave_encryption_key': os.getenv('FLUTTERWAVE_ENCRYPTION_KEY'),
        'remita_url': os.getenv('REMITA_URL'),
        'remita_username': os.getenv('REMITA_USERNAME'),
        'remita_password': os.getenv('REMITA_PASSWORD'),
        'remita_merchant_id': os.getenv('REMITA_MERCHANT_ID'),
        'remita_service_type': os.getenv('REMITA_SERVICE_TYPE'),
        'remita_api_key': os.getenv('REMITA_API_KEY'),
        'remita_token': os.getenv('REMITA_TOKEN'),
    }

