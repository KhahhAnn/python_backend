    # import smtplib
    # from email.mime.multipart import MIMEMultipart
    # from email.mime.text import MIMEText
    #
    # # Hàm gửi email
    # def send_email(subject: str, body: str, to: str):
    #     smtp_server = "smtp.gmail.com"
    #     smtp_port = 587
    #     smtp_username = "khanhanbui2003@gmail.com"
    #     smtp_password = "uiwhhvmlflxfqzic"
    #
    #     # Thiết lập nội dung email
    #     msg = MIMEMultipart()
    #     msg['From'] = smtp_username
    #     msg['To'] = to
    #     msg['Subject'] = subject
    #     msg.attach(MIMEText(body, 'plain'))
    #
    #     # Kết nối và gửi email
    #     server = smtplib.SMTP(smtp_server, smtp_port)
    #     server.starttls()
    #     server.login(smtp_username, smtp_password)
    #     server.send_message(msg)
    #     server.quit()
