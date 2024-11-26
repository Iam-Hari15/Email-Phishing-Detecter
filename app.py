from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Updated function to check for phishing emails
def check_phishing_email(sender_email, email_content):
    # Expanded phishing keywords
    phishing_keywords = [
        "verify your account", "click here", "password", "urgent", "credit card",
        "login now", "update your account", "bank account", "reset your password",
        "your account is on hold", "unauthorized login detected", "congratulations! you've won",
        "verify now", "secure your account", "urgent response needed"
    ]

    # Known suspicious domains (expand this list as needed)
    suspicious_domains = ["phishing.com", "malicious.com", "fake.com", "paypal-secure.com"]
    
    # Regex to detect typosquatting (e.g., g0ogle.com)
    typosquatting_pattern = re.compile(r'[a-zA-Z0-9]+0[a-zA-Z]+\.com')

    # Regex to detect URLs in email content
    url_pattern = re.compile(r"https?://[^\s]+")

    # Step 1: Check sender's email domain
    sender_domain = sender_email.split('@')[-1]
    if any(domain in sender_domain for domain in suspicious_domains):
        return "The sender's email domain is suspicious and commonly used in phishing."

    # Step 2: Check for typosquatting in sender's domain
    if re.search(typosquatting_pattern, sender_domain):
        return "The sender's email domain appears to be typosquatting (e.g., g0ogle.com)."

    # Step 3: Check for phishing keywords in email content
    for keyword in phishing_keywords:
        if keyword.lower() in email_content.lower():
            return f"The email contains a phishing keyword: '{keyword}'."

    # Step 4: Check for suspicious links in email content
    urls = re.findall(url_pattern, email_content)
    for url in urls:
        # Check if the URL contains suspicious domains
        if any(domain in url for domain in suspicious_domains):
            return f"The email contains a suspicious link: {url}"

        # Check for typosquatting in URLs
        if re.search(typosquatting_pattern, url):
            return f"The email contains a typosquatted link: {url}"

    # If all checks are passed, the email is likely safe
    return "This email seems safe."

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        sender_email = request.form.get('senderEmail')
        email_content = request.form.get('emailInput')

        # Process the email to check if it's phishing
        result = check_phishing_email(sender_email, email_content)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
