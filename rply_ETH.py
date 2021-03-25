import tweepy 
import logging 
from config import create_api
import time
import requests
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#add in Eth current price retrieval
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '46a72f6a-f9a2-4c34-800d-ec1d79f86e07',
}
try:
  response = response.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)

#replies function
def check_mention(api, keywords, since_ids):
    logger.info("Retrieving Eth mentions")
    new_since_ids = since_ids
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_ids= since_ids).items():
        new_since_ids = max(tweet.id, new_since_ids) #this may be where it keeps replying to same tweets
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keywords):
            logger.info(f"Answering to {tweet.user.name}")

            if not tweet.user.following:
                tweet.user.follow()

            if not tweet.in_reply_to_status_id:
                api.update_status(
                    status="@"+ tweet.user.name + " it is at " + "$" + (data["bpi"]["USD"]["rate"]) + " better go buy it!",
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
        time.sleep(120)

if __name__ == "__main__":
    main()