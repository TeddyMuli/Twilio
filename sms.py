# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

os.environ['TWILIO_ACCOUNT_SID'] = 'ACb05108e6556d6e8ee68685c398f6ed67'
os.environ['TWILIO_AUTH_TOKEN'] = '578d0cf6fb9ea124a55d54327431eb46'

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+13157400764',
         to='+254799957459'
     )

print(message.sid)
