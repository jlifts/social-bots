# social-bots
Fun little experiement with Python, Tweepy, and Heroku to automate Social Media Interactions

<b> Twitter Bot </b>

*Username: @bluejay_mr*

https://twitter.com/bluejay_mr

This bot is designed to favorite keyword tweets, follow for a follow, like and retweet if mentioned in a tag,
and will provide you with the real time price of Ethereum or Bitcoin if you tag him and mention "BTC", "Bitcoin",
"Ethereum", "ETH", or "the best crypto".

<b>If you would like to try it out for yourself:</b>

First, you should create a Twitter Developer Account at: https://developer.twitter.com/
*The Documentation is important too: https://developer.twitter.com/en/docs*

Make sure to hide your API keys either in an .env file or refrence them in a config file,
and run `export MY_ACCESS_TOKEN=....(your token)...` in your terminal

I chose to then make a single function to call all the other functions, through imports, I would like to automate at once. This is the file I will make a worker on Heroku!

Next, take your newly made Twitter bot and bring them to life by deploying them! I chose to host mine with Heroku: https://www.heroku.com/

This is where you want to make sure your requirements.txt file, Procfile, and runtime.txt is up to date with your environment, Heroku will base how they handle   your bot with this.
You can then add your Tokens and APIs to in settings so that it will run!

Hope this helps and that you have fun!

*jlifts*


