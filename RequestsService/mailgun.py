import requests
from ahora_API.settings import MAILGUN_AUTH, MAILGUN_DOMAIN

MAILGUN_URL_SEND = 'https://api.mailgun.net/v3/%s/messages' % (MAILGUN_DOMAIN)
MAILGUN_URL_VALIDATE = "https://api.mailgun.net/v4/address/validate"
def send_mail(subject, text, rcv):
    return requests.post(
        MAILGUN_URL_SEND,
        auth=('api', MAILGUN_AUTH),
        data={
            "from": "AHORA API <mailgun@%s>" % MAILGUN_DOMAIN,
            "to": [rcv, MAILGUN_DOMAIN],
            "subject": subject,
            "text": text
        }
    )

def validate_mail(email):
    return requests.post(
        MAILGUN_URL_VALIDATE,
        auth=('api', MAILGUN_AUTH),
        data={"address": email}
    )



# send_mail("aha", "aha2", "azare242@gmail.com")