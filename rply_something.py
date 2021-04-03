import tweepy 
import logging 
from config import create_api
import time
import requests
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class CListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    #Like and Reply 
    def random_reply(self, tweet):
        logger.info("Retrieving Tweets...")

        #ignores replies and if I'm the author
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            return

        if not tweet:
            try:
                logger.info(f"Commenting and favoriting {tweet.user.name}")

                api.update_status(
                    status= "@" + tweet.user.screen_name + " I like this tweet, very interesting, hope you have a great day!",
                    in_reply_to_status_id = tweet.id,
                    auto_populate_reply_metadata = True,)
                tweet.favorite()
            except Exception as e:
                logger.error("There was a fav error", exec_info=True)
        

def main(keywords):
    api = create_api()
    tweets_listener = CListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])

if __name__ == "__main__":
    main(['DeFi', 'Chainlink','Ethereum','game','cool'])