# Application settings and configuration
import os

# Streamlit page configuration
PAGE_CONFIG = {
    "page_title": "Task Machine Pro",
    "page_icon": "🛠️",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# API Keys (set these as environment variables)
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', 'your_twilio_account_sid_here')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN', 'your_twilio_auth_token_here')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER', 'your_twilio_phone_number_here')
GOOGLE_GEMINI_KEY = os.getenv('GOOGLE_GEMINI_KEY', 'your_google_gemini_key_here')

# Application paths
STATIC_PATH = "static"
DATA_PATH = "data"
MODULES_PATH = "modules"

# Default values
DEFAULT_LOAN_AMOUNT = 500000
DEFAULT_INTEREST_RATES = {
    "Home Loan": 8.5,
    "Car Loan": 9.5,
    "Personal Loan": 12.5
}
