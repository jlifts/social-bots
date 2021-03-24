from multiprocessing import Process
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
#Powered by CoinDesk
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
#print(data["bpi"]["USD"]["rate"])
#If you want to see the price uncomment

#add in ethereum current price retrieval
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
#print(data["bpi"]["USD"]["rate"])
#If you want to see the price uncomment

def streamer():
    api = create_api()
    tweets_listener = TListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=["crypto", "ethereum", "DeFi", "science","covid","coffee", "bankless"], languages=["en"])

def follow():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Sleeping...")
        time.sleep(180)


def BTC():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["BTC", "Bitcoin"], since_id)
        logger.info("Searching...")
        time.sleep(1000)

def ETH():
    api = create_api()
    since_ids = 1
    while True:
        since_ids = check_mention(api, ["ETH", "Ethereum", "Ether", "the best crypto"], since_ids)
        logger.info("Searching...")
        time.sleep(1000)


if __name__ == "__main__":
    p1 = Process(target=streamer)
    p1.start()
    p2 = Process(target=follow)
    p2.start()
    #p3 = Process(target=tagged)
    #p3.start()
    #p4 = Process(target=reply)
    #p4.start()
    p5 = Process(target=BTC)
    p5.start()
    p6 = Process(target=ETH)
    p6.start()