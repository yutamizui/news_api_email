import smtplib
import os
from email.message import EmailMessage

def send_email(message):
    username = "futebol.de.salao10@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = username

    email = EmailMessage()
    email["From"] = username
    email["To"] = receiver
    email["Subject"] = "Today's news"
    email.set_content(message)  # EmailMessage handles UTF-8 automatically

    with smtplib.SMTP("smtp.gmail.com", port=587) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(email)  # <-- this handles Unicode correctly
