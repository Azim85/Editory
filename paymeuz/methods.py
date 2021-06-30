import requests
from .keywords import *
import base64


class Paymeuz:

    def create_transaction(self, token, order_id, amount, order_type=None) -> dict:
        data = dict(
            method=RECEIPTS_CREATE,
            params=dict(
                amount=amount * 100,
                account={
                    KEY_1: order_id,
                    KEY_2: order_type
                }
            )
        )
        response = requests.post(
            url=URL,
            json=data,
            headers=AUTHORIZATION
        )
        result = response.json()

        if 'error' in result:
            return result

        data = dict(
            method=RECEIPTS_PAY,
            params=dict(
                id=result['result']['receipt']['_id'],
                token=token
            )
        )

        response = requests.post(url=URL, json=data, headers=AUTHORIZATION)
        return response.json()

    def create_cards(self, card_number, expire, amount, save=False) -> dict:
        data = dict(
            method=CARDS_CREATE,
            params=dict(
                card=dict(number=card_number, expire=expire),
                amount=amount,
                save=save
            )
        )

        response = requests.post(url=URL, json=data, headers=AUTHORIZATION)
        result = response.json()
        if 'error' in result:
            return result

        token = result['result']['card']['token']
        result = self.cards_get_verify_code(token=token)
        return result

    def cards_get_verify_code(self, token) -> dict:
        data = dict(
            method=CARDS_GET_VERIFY_CODE,
            params=dict(token=token)
        )
        response = requests.post(url=URL, json=data, headers=AUTHORIZATION)
        result = response.json()
        result.update(token=token)

        return result

    def cards_verify(self, code, token):
        data = dict(
            method=CARD_VERIFY,
            params=dict(
                token=token,
                code=code
            )
        )

        response = requests.post(url=URL, json=data, headers=AUTHORIZATION)
        return response.json()

    @staticmethod
    def create_initialization(amount, order_id, return_url, order_type=None):
        params = f"m={TOKEN};ac.{KEY_1}={order_id};a={amount};c={return_url}"
        if order_type:
            params += f"ac.{KEY_2}"
        encode_params = base64.b64encode(params.encode("utf-8"))
        encode_params = str(encode_params, 'utf-8')
        url = f"{LINK}/{encode_params}"
        return url

    def check_order(self, amount, account):
        raise NotImplemented
