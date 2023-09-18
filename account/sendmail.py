import os
from email.message import EmailMessage
import ssl
import smtplib
from .models import Verification

def send_mail(to, subject, body):
    sender = "quizmeme2023@gmail.com"
    recipient = to
    password = "emdfdgwwljpvtfpf"

    mail = EmailMessage()
    mail["From"] = sender
    mail["To"] = recipient
    mail["Subject"] = subject

    mail.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, mail.as_string())

def send_verification(user, domain):
    # Get the verification object for the user
    verification = Verification.objects.get(user=user)

    # Build the verification URL
    url = f"{domain}/users/verify/{user.id}/{verification.token}"

    # Build the email body
    body = f"Hey, Welcome to Quizmeme.\n\nClick the link below to verify your account:\n\n{url}"

    # Send the email
    send_mail(user.email, "Verify your account", body)
