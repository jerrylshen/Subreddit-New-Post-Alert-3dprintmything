#Sensitive info removed, get this info from your Twilio account

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

phone_numbers = [""]

def send_alert():
    for number in phone_numbers:
        message = client.messages \
                    .create(
                         body="\t\t\n https://www.reddit.com/r/3Dprintmything/",
                         from_='',
                         to=number
                         )


#print(message.sid)
