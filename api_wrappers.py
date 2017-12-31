import requests
import json
import vars


class CryptoMKT:
    @staticmethod
    def get_prices():
        payload = {'market': 'ETHCLP'}
        response = requests.get('https://api.cryptomkt.com/v1/ticker',
                                params=payload)
        response_json = response.json()
        price_dict = {'bid': int(response_json['data'][0]['bid']),
                      'ask': int(response_json['data'][0]['ask'])}
        return price_dict


class SurBTC:
    @staticmethod
    def get_prices():
        response = requests.get(
            'https://www.surbtc.com/api/v2/markets/eth-clp/ticker.json')
        response_json = response.json()
        price_dict = {'bid': int(float(response_json['ticker']['max_bid'][0])),
                      'ask': int(float(response_json['ticker']['min_ask'][0]))}
        return price_dict


class Orionx:
    @staticmethod
    def get_prices():
        url = 'http://api.orionx.io/graphql'
        query = '''
        query getOrderBook($marketCode: ID!) {
            orderBook: marketOrderBook(marketCode: $marketCode) {
                spread
                mid
            }
        }
        '''
        request_json = {'query': query,
                        'operationName': 'getOrderBook',
                        'variables': {'marketCode': 'ETHCLP'}}

        response = requests.post(url=url, json=request_json)
        response_json = response.json()
        spread = response_json['data']['orderBook']['spread']
        mid = response_json['data']['orderBook']['mid']
        price_dict = {'bid': int(mid - spread / 2),
                      'ask': int(mid + spread / 2)}
        return price_dict


class Pushbullet:
    def __init__(self, access_token):
        self.access_token = access_token

    def push_note(self, title, body, device_iden=vars.device_iden):
        headers = {'Access-Token': self.access_token,
                   'Content-Type': 'application/json'}
        data = {'device_iden': device_iden,
                'title': title,
                'body': body,
                'type': 'note'}
        requests.post('https://api.pushbullet.com/v2/pushes', headers=headers,
                      data=json.dumps(data))
