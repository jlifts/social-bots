import tweepy 
import logging 
from config import create_api
import time
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#add in bitcoin current price retrieval
#Powered by CoinDesk
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
print(data["bpi"]["USD"]["rate"])

FILE_NAME = 'lastSeenBTC.txt'

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

#replies function
def check_BTC(api, keywords):
    last_seen_id = get_last_seen_id(FILE_NAME)
    logger.info("Retrieving BTC mentions")
    for tweet in tweepy.Cursor(api.mentions_timeline,last_seen_id, tweet_mode = 'extended', q=keywords).items():
        last_seen_id = tweet.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keywords):
            logger.info(f"Answering to {tweet.user.name}")

            if not tweet.user.following:
                tweet.user.follow()

            if any(keywords) in tweet.full_text.lower():
                api.update_status(
                    status="@"+ tweet.user.screen_name + " it is at " + "$" + (data["bpi"]["USD"]["rate"]),
                    in_reply_to_status_id = tweet.id,
                    auto_populate_reply_metadata = True,
                )
        return

def main(keywords):
    api = create_api()
    while True:
        check_BTC(api, ["BTC", "Bitcoin"])
        logger.info("Searching...")
        time.sleep(120)

if __name__ == "__main__":
    main(["BTC", "Bitcoin"])