import tweepy 
import logging 
from config import create_api
import time
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#Like and Reply 
def random_reply(api, keywords, since_id):
    logger.info("Retrieving Tweets...")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.search,q=keywords,
        since_id= since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keywords):
            logger.info(f"Commenting and favoriting {tweet.user.name}")

            api.update_status(
                status= "@"+ tweet.user.name +" I like this tweet, very interesting, hope you have a great day!",
                in_reply_to_status_id = tweet.id,
                auto_populate_reply_metadata = True,
            )
            tweet.favorite()
        return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = random_reply(api, ["coffee", "crypto","happy"], since_id)
        logger.info("Searching...")
        time.sleep(10)

if __name__ == "__main__":
    main()