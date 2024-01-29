import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
from dotenv import load_dotenv
import os
load_dotenv() 

def send_email(subject, openai_response, to_address, attachment_path=None):
    # Set up the email server
    smtp_server = "smtp.gmail.com"
    smtp_port = 465

    # Your Gmail credentials
    sender_email = os.getenv("GMAIL_USER")
    sender_password = os.getenv("GMAIL_PASS")

    # Create a MIME object for the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_address
    message["Subject"] = subject

    # Attach OpenAI response as text
    message.attach(MIMEText(openai_response, "plain"))

    # Attach attachment if provided
    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name="attachment")
            part["Content-Disposition"] = f'attachment; filename="{attachment_path}"'
            message.attach(part)

    # Establish a secure connection with the SMTP server
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        # Log in to the email server
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, to_address, message.as_string())
