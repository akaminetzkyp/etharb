from api_wrappers import CryptoMKT, SurBTC, Pushbullet
import time

check_delay = 60
pushbullet = Pushbullet('')

while True:
    cryptomkt_prices = CryptoMKT.get_prices()
    surbtc_prices = SurBTC.get_prices()
    time.sleep(check_delay)