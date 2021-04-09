import tweepy
import time
from config import create_api
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

FILE_NAME = 'lastSeenId.txt'

def get_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id= int (f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def check_mentions(api):
    last_seen_id = get_last_seen_id(FILE_NAME)
    logger.info("Retrieving tagged mentions")
    mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')
    for tweet in reversed(mentions):
        last_seen_id = tweet.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any:
            logger.info(f"Like and retweet to {tweet.user.name}")
        #Liking Just to like
            if not tweet.favorited:
                try:
                    tweet.favorite()
                    time.sleep(2)
                except Exception as e:
                    logger.error("There was a fav error", exec_info=True)
        #Retweeting it for content
            if not tweet.retweeted:
                try:
                    tweet.retweet()
                    time.sleep(5)
                except Exception as e:
                    logger.error("error on Retweet", exc_info=True)

def main():
    api = create_api()
    while True:
        check_mentions(api)
        logger.info("Searching...")
        time.sleep(140)

if __name__ == "__main__":
    main()