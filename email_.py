

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase

def send_email():
    # Email account credentials
    from_email = "sendermail@gmail.com"
    password = "your app password"  
    # make changes here
    to_email = "receivermail@gmail.com"
    # Replace with your actual credentials (avoid putting them in code)

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Daily Report"

    # Email body
    body = "This is your daily report."

    msg.attach(MIMEText(body, "plain"))

    with open('data.xlsx', "rb") as attachment_file:
        attachment_part = MIMEBase("application", "octet-stream")
        attachment_part.set_payload(attachment_file.read())

    encoders.encode_base64(attachment_part)

    attachment_part.add_header("Content-Disposition", f"attachment; filename={'data.xlsx'.split('/')[-1]}")

    with open('stock_chart.png', "rb") as attachment_file:
        attachment_part2 = MIMEBase("application", "octet-stream")
        attachment_part2.set_payload(attachment_file.read())

    encoders.encode_base64(attachment_part2)

    attachment_part2.add_header("Content-Disposition", f"attachment; filename={'stock_chart.png'.split('/')[-1]}")

    msg.attach(attachment_part)
    msg.attach(attachment_part2)

    try:
        # Create server object with SSL option
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, password)
        
        # Send email
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {to_email}.")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

