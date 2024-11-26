import re
import requests
from fuzzywuzzy import fuzz
from dns.resolver import Resolver, NoAnswer, NXDOMAIN

# List of phishing domains to compare
phishing_domains = ["google.com", "yahoo.com", "paypal.com"]

# List of phishing-related keywords
phishing_keywords = ["urgent", "suspended", "bank account", "verify your account", "click here", "free gift", "security alert"]

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, email))

def check_for_keywords(email_body):
    for keyword in phishing_keywords:
        if keyword.lower() in email_body.lower():
            return True
    return False

def compare_domains(email):
    try:
        domain = email.split('@')[1]
        for phish_domain in phishing_domains:
            similarity_score = fuzz.ratio(domain.lower(), phish_domain.lower())
            if similarity_score > 80:
                return True
        return False
    except Exception:
        return False

def check_domain_reputation(domain):
    api_key = "YOUR_GOOGLE_SAFE_BROWSING_API_KEY"
    url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"

    request_body = {
        "client": {
            "clientId": "your-app",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": f"http://{domain}"}]
        }
    }

    try:
        response = requests.post(url, json=request_body)
        response.raise_for_status()
        data = response.json()
        if "matches" in data:
            return True
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error checking domain reputation: {e}")
        return False

def is_domain_valid(domain):
    try:
        resolver = Resolver()
        resolver.resolve(domain, 'A')
        return True
    except (NoAnswer, NXDOMAIN):
        return False
