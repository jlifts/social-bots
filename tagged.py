import tweepy
import time
from config import create_api
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mention(api, since_ids):
    logger.info("Retrieving tagged mentions")
    new_since_ids = since_ids
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_ids= since_ids).items():
        new_since_ids = max(tweet.id, new_since_ids)
        if tweet.in_reply_to_status_id is not None:
            continue
            logger.info(f"Like and reply to {tweet.user.name}")

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
                    time.sleep(10)
                except Exception as e:
                    logger.error("error on Retweet", exc_info=True)

        return new_since_ids

def main():
    api = create_api()
    since_ids = 1
    while True:
        since_ids = check_mention(api, since_ids)
        logger.info("Searching...")
        time.sleep(20)

if __name__ == "__main__":
    main()