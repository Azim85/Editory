import base64
import json
from threading import Thread

import requests
from django.conf import settings
from django.core.mail import send_mail as _send_mail


def thread(function):
    def decorator(*args, **kwargs):
        t = Thread(target=function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    return decorator


@thread
def send_mail(order):
    subject = 'Status of your order'
    text = 'The delivery status of your order is ' + order.get_delivery_status_display()
    _send_mail(subject, text, 'ziyamovamaftuna0202@gmail.com', [order.email])


def get_sms_json_template(phone, text, sms_id):
    data = {
        'messages': [
            {
                'recipient': phone,
                'message-id': phone + str(sms_id),
                'sms': {
                    'originator': '3700',
                    'content': {
                        'text': text,
                    }
                }
            }
        ]
    }
    return json.dumps(data)


def _send_sms(data):
    text = settings.SMS_LOGIN + ':' + settings.SMS_PASS
    text = text.encode('utf-8')
    encoded = base64.b64encode(text)
    encoded = encoded.decode('utf-8')

    headers = {
        'Content-Type': "application/json",
        'Authorization': "Basic " + encoded,
        'cache-control': "no-cache",
        'Postman-Token': "effa6d6c-01b4-475c-8094-78b1f49c8282"
    }
    r = requests.post(settings.SMS_URL, data=data, headers=headers)
    print(r.text)


@thread
def send_sms(order, sms_id):
    subject = 'Status of your order'
    text = 'The delivery status of your order is ' + order.get_delivery_status_display()
    text = f'{subject}\n\n{text}'

    data = get_sms_json_template(order.phone, text, sms_id)
    _send_sms(data)
