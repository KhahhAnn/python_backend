import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailService:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.smtp_username = "khanhanbui2003@gmail.com"
        self.smtp_password = "uiwhhvmlflxfqzic"

    def send_email(self, from_email: str, to_email: str, subject: str, body: str):
        # Create the MIME message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        # Connect to the SMTP server and send the email
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.sendmail(from_email, to_email, msg.as_string())
            print("Email sent successfully.")
        except smtplib.SMTPException as e:
            raise RuntimeError(f"Failed to send email: {str(e)}")
