import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


def send_email(subject, body, to_email):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'akogachechiladze22@gmail.com'
    smtp_password = 'mjxc drxb vpsi nalq'

    from_email = 'akogachechiladze22@gmail.com'
    from_name = 'BTU Manager'
    to_email = to_email

    msg = MIMEMultipart()
    msg['From'] = formataddr((from_name, from_email))  # Use formataddr to set name and email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()


# Example usage
if __name__ == "__main__":
    send_email("Test Subject", "This is a test email body.", "recipient@example.com")