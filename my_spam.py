import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def main():
    api = create_api()
    for tweet in api.user_timeline(user_id='@G11Begore',count= 100, include_rts= True):
        if not tweet.favorited:
            try:
                tweet.favorite()
                logger.info(f"Favorited id {tweet.id}")
                time.sleep(20)
            except Exception as e:
                logger.error("There was a fav error", exec_info=True)

if __name__ == "__main__":
    main()
        