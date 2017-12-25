import requests


class CryptoMKT:
    @staticmethod
    def get_prices():
        payload = {'market': 'ETHCLP'}
        response = requests.get('https://api.cryptomkt.com/v1/ticker',
                                params=payload)
        json = response.json()
        price_dict = {'bid': json['data'][0]['bid'],
                      'ask': json['data'][0]['ask']}
        return price_dict


class SurBTC:
    @staticmethod
    def get_ticker():
        response = requests.get(
            'https://www.surbtc.com/api/v2/markets/eth-clp/ticker.json')
        json = response.json()
        price_dict = {'bid': json['ticker']['max_bid'][0],
                      'ask': json['ticker']['min_ask'][0]}
        return price_dict


if __name__ == '__main__':
    print(CryptoMKT.get_prices())
    print(SurBTC.get_ticker())
