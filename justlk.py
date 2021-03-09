import tweepy
import logging
from config import create_api
import json
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class TListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"The tweet ids {tweet.id}")
        #ignores replies and if I'm the author
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            return
        #Liking if not liked yet
        if not tweet.favorited:
            try:
                tweet.favorite()
                time.sleep(20)
            except Exception as e:
                logger.error("There was a fav error", exec_info=True)

    def on_error(self,status):
        logger.error(status)

def main(keywords):
    api = create_api()
    tweets_listener = TListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])

if __name__ == "__main__":
    main(["Crypto", "Ethereum", "DeFi", "science","covid","coffee", "bankless"])
        