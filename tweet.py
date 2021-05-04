import tweepy
import logging
from config import create_api
import time
import requests
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# Powered by CoinDesk
# BTC
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
print(data["bpi"]["USD"]["rate"])

# Powered by CoinGecko
# ETH
response_Eth = requests.get(
    'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
Eth = response_Eth.json()
print(Eth['ethereum']['usd'])
# DOGE
response_Doge = requests.get(
    'https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd')
Doge = response_Doge.json()
print(Doge['dogecoin']['usd'])


# Tweet a Crypto update


def crypto_updates(api):
    logger.info("Retrieving BTC, ETH, and DOGE updates")
    api.update_status('Daily Crypto Report: $BTC is at $' + (
        data["bpi"]["USD"]["rate"]) + ', $ETH is at $' + str((
            Eth['ethereum']['usd'])) + ', $DOGE is at $' + str((Doge['dogecoin']['usd'])) + '. That is the current pricing today, remember to HODL! Vires in Numeris')


def main():
    api = create_api()
    while True:
        crypto_updates(api)
        time.sleep(24 * 3600)


if __name__ == "__main__":
    main()
