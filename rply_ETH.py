import tweepy 
import logging 
from config import create_api
import time
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#add in bitcoin current price retrieval
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
print(data["bpi"]["USD"]["rate"])

#replies function
def check_mention(api, keywords, since_ids):
    logger.info("Retrieving mentions")
    new_since_ids = since_ids
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_ids= since_ids).items():
        new_since_ids = max(tweet.id, new_since_ids)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keywords):
            logger.info(f"Answering to {tweet.user.name}")

            if not tweet.user.following:
                tweet.user.follow()

            api.update_status(
                status="$" + (data["bpi"]["USD"]["rate"]),
                in_reply_to_status_id = tweet.id,
                auto_populate_reply_metadata = True,
            )
        return new_since_ids

def main():
    api = create_api()
    since_ids = 1
    while True:
        since_ids = check_mention(api, ["ETH", "Etherium", "Ether"], since_ids)
        logger.info("Searching...")
        time.sleep(60)

if __name__ == "__main__":
    main()