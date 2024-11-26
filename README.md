# Phishing Email Detection Project

## Overview
This project aims to detect phishing emails by analyzing the sender's email and message content. It utilizes a list of common phishing keywords to identify suspicious emails and presents a user-friendly interface for entering email details. This helps users protect themselves from phishing attacks.

## Features
- **Sender Email Validation**: Checks if the sender's email domain matches expected patterns for phishing.
- **Keyword Detection**: Scans the email body for common phishing keywords (e.g., "Verify your account", "Click here to update").
- **User Interface**: Simple and intuitive web interface for entering the sender's email and email message.
- **Phishing Alert**: Flags emails containing suspicious keywords and alerts the user.

## Tech Stack
- **Frontend**: HTML, CSS (for UI layout and styling)
- **Backend**: Python (for phishing keyword detection)
- **Libraries**: 
  - `re` (for regex matching of phishing keywords)
  - HTML for the user interface

##Phishing Keyword List
The following keywords are checked in the email body for phishing attempts:

"verify your account"
"urgent action required"
"account suspended"
"click here to update"
"reset your password"
"limited time offer"
"unusual activity detected"
"login to continue"
"secure your account"
"claim your reward"
"you have won"
"confirm your details"
"free trial ending"
"immediate payment required"
"unlock your account"

Thank you for exploring my Phishing Email Detection Project!

