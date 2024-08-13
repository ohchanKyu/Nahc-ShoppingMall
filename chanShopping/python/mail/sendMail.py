import smtplib
import string
import random
import os

class SendMail:
    def __init__(self):
        self.user = os.getenv("ADMIN_EMAIL")
        self.password = os.getenv("ADMIN_PASSWORD")

    def sendMessage(self,email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=os.getenv("ADMIN_EMAIL"), password=os.getenv("ADMIN_PASSWORD"))

            generate_message = ""
            for i in range(10):
                generate_message += str(random.choice(string.ascii_uppercase+string.digits))
            connection.sendmail(from_addr=os.getenv("ADMIN_EMAIL"), to_addrs=email,
                msg=f"Subject:Thank you for Register our Shopping Web!\n\n This is Authentic Number : {generate_message}"
            )
            return generate_message
