# Application settings and configuration

# Streamlit page configuration
PAGE_CONFIG = {
    "page_title": "Task Machine Pro",
    "page_icon": "🛠️",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# API Keys (you should set these as environment variables in production)
TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_PHONE_NUMBER = ''
GOOGLE_GEMINI_KEY = "AIz"

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
