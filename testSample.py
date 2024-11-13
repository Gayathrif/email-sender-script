import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email settings
sender_email = "gayathri22bcd11@iiitkottayam.ac.in"  # Your email address
receiver_email = "gayathricnair7314@gmail.com"  # Recipient's email address
password = "oytu jfpt pyby lovn"  # Your Gmail app password

# Email content
subject = "Auto Generated Email"
body = "This is an auto-generated email. Please do not reply."

# Create the email message
message = MIMEMultipart()
message["From"] = "gayathri22bcd11@iiitkottayam.ac.in"
message["To"] = "gayathricnair7314@gmail.com"
message["Subject"] = subject

# Add body to the email
message.attach(MIMEText(body, "plain"))

# Connect to Gmail's SMTP server and send the email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
