import tweepy
import logging
from config import create_api
import json
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def on_status(self, tweet):
    logger.info(f"The tweet ids {tweet.id}")
    #ignores replies and if I'm the author
    if api.get_user(screen_name='Algorand'):
    #Liking if not liked yet
        if not tweet.favorited:
            try:
                tweet.favorite()
                time.sleep(10)
            except Exception as e:
                logger.error("There was a fav error", exec_info=True)
        #Retweeting it for content
        if not tweet.retweeted:
            try:
                tweet.retweet()
                time.sleep(90)
            except Exception as e:
                logger.error("error on Retweet", exc_info=True)

    def on_error(self,status):
        logger.error(status)

def main(keywords):
    api = create_api()
    

if __name__ == "__main__":
    main([])
        