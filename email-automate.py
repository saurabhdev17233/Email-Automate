import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(message, 'plain'))
        
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# saurabhdev17233
if __name__ == "__main__":
    sender = "aastra05.in@gmail.com"
    password = "------"  # Use an app password for security
    recipient = "saurabhdev17233@gmail.com"
    subject = "Test Email"
    message = "Hello! This is an automated email."
    
    send_email(sender, password, recipient, subject, message)
