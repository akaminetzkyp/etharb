from api_wrappers import CryptoMKT, SurBTC, Pushbullet
import time

check_delay = 60
threshold = 0

pushbullet = Pushbullet('INSERT TOKEN')

while True:
    cryptomkt_prices = CryptoMKT.get_prices()
    surbtc_prices = SurBTC.get_prices()

    print(cryptomkt_prices)
    print(surbtc_prices)

    if cryptomkt_prices['bid'] - surbtc_prices['ask'] >= threshold:
        title = 'Arbitrage oportunity!'
        body = 'CryptoMKT\'s bid is {}CLP greater than SurBTC\'s ask.'.format(
            threshold)
        pushbullet.push_note(title, body)
    elif surbtc_prices['bid'] - cryptomkt_prices['ask'] >= threshold:
        title = 'Arbitrage oportunity!'
        body = 'SurBTC\'s bid is {}CLP greater than CryptoMKT\'s ask.'.format(
            threshold)
        pushbullet.push_note(title, body)
    time.sleep(check_delay)
