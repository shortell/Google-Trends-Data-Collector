from utils.data_collection import store_all_searches
from utils.email_sender import send_scan_emails, send_email

def store_and_send_searches():
    responses = store_all_searches()
    send_scan_emails(responses)

def send_diagnostic_email():
    send_email("DIAGNOSTIC", "server still running")


