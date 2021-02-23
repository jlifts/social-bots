from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome('/Users/Josh/Desktop/Drivers/chromedriver')

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login/')
        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=%23'+ hashtag +'&src=typed_query')
        time.sleep(5)
        for i in range (1,4):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('')



josh = TwitterBot('josh@victishealth.com', 'bluejay1')
josh.login()
josh.like_tweet('webdev')
