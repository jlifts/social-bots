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

#replies function
def check_mentions(api, keywords, since_id):
    logger.info("Retrieving Btc mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id= since_id).items():
        new_since_id = max(tweet.id, new_since_id) #this may be where it keeps replying to same tweets
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keywords):
            logger.info(f"Answering to {tweet.user.name}")

            if not tweet.user.following:
                tweet.user.follow()

            if not tweet.in_reply_to_status_id:
                api.update_status(
                    status="@"+ tweet.user.screen_name + " it is at " + "$" + (data["bpi"]["USD"]["rate"]),
                    in_reply_to_status_id = tweet.id,
                    auto_populate_reply_metadata = True,
                )
        return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["BTC", "Bitcoin"], since_id)
        logger.info("Searching...")
        time.sleep(120)

if __name__ == "__main__":
    main()