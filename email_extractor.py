import re

def extract_emails(text):
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

# Example
sample_text = "Contact us at info@example.com or support@mydomain.org"
print(extract_emails(sample_text))
