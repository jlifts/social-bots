import tweepy

#Auth

key = "c5paUrih3xjAuUmkB1K42E5EF"
seceret_key = "dI7JdZJnGBvDogx42n2cXykgIH8ANc3roEB9lOaQNCPkrHCme2"

bearerToken = "AAAAAAAAAAAAAAAAAAAAAKIuNAEAAAAAkmSHgkszVFrJ5vMtzd38%2Fm8O6dE%3DdBvBhshcNLP8OHVfsgnQaVS6zxK0mx8cepPdkHX11Zj8Ga7Rgy"

access = "1363168765295407106-KZxJIW5FYVz4lbA9wiTFORoHhYakcJ"
seceret_access = "C6gEElbjWGSM95isuOKeuloOUKLRV0p8cNaoyrTFnl7YP"

auth = tweepy.OAuthHandler(key, seceret_key)
auth.set_access_token(access, seceret_access)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#api.update_status('Spread your wings and fly sometimes') #To Post to Twitter


