import requests
from ahora_API.settings import MAILGUN_AUTH, MAILGUN_DOMAIN

MAILGUN_URL = 'https://api.mailgun.net/v3/%s/messages' % (MAILGUN_DOMAIN)

def send_mail(subject, text, rcv):
    return requests.post(
        MAILGUN_URL,
        auth=('api', MAILGUN_AUTH),
        data={
            "from": "AHORA API <mailgun@%s>" % MAILGUN_DOMAIN,
            "to": [rcv, MAILGUN_DOMAIN],
            "subject": subject,
            "text": text
        }
    )





# send_mail("aha", "aha2", "azare242@gmail.com")