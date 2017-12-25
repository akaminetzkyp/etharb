import requests
import json


class CryptoMKT:
    @staticmethod
    def get_prices():
        payload = {'market': 'ETHCLP'}
        response = requests.get('https://api.cryptomkt.com/v1/ticker',
                                params=payload)
        response_json = response.json()
        price_dict = {'bid': response_json['data'][0]['bid'],
                      'ask': response_json['data'][0]['ask']}
        return price_dict


class SurBTC:
    @staticmethod
    def get_prices():
        response = requests.get(
            'https://www.surbtc.com/api/v2/markets/eth-clp/ticker.json')
        response_json = response.json()
        price_dict = {'bid': response_json['ticker']['max_bid'][0],
                      'ask': response_json['ticker']['min_ask'][0]}
        return price_dict


class Pushbullet:
    def __init__(self, access_token):
        self.access_token = access_token

    def push_note(self, title, body, device_iden='ujBKQljDiTYsjAbxZrFbC8'):
        headers = {'Access-Token': self.access_token,
                   'Content-Type': 'application/json'}
        data = {'device_iden': device_iden,
                'title': title,
                'body': body,
                'type': 'note'}
        requests.post('https://api.pushbullet.com/v2/pushes', headers=headers,
                      data=json.dumps(data))
