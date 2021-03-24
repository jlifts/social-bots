import tweepy
import time
import logging
import json
import requests
from config import create_api
from follow import follow_followers
from justlk import TListener
from rply_BTC import check_mentions
from rply_ETH import check_mention

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#add in bitcoin current price retrieval
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
print(data["bpi"]["USD"]["rate"])

def main(keywords):
    api = create_api()
    tweets_listener = TListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])
    while True:
        follow_followers(api)
        logger.info("Sleeping...")
        time.sleep(40)
    since_id = 1
    while True:
        since_id = check_mentions(api, ["BTC", "Bitcoin"], since_id)
        logger.info("Searching...")
        time.sleep(60)


if __name__ == "__main__":
    main(["crypto", "ethereum", "DeFi", "science","covid","coffee", "bankless", "love"])
