#!/usr/bin/env python3

# PUBLIC VERSION, DO NOT ADD YOUR API KEYS TO THIS



'''
Soshii will be a social media bot made in Python, it's still being developed
You give it your content, usernames, passwords,
and it'll post your content on all your social media accounts so that
You don't have to manually post them to each platform.

There are paid for versions of this but I wanted a version that people could use for free!

Since API's and Social Media platforms get updated, this bot will need maintenance.
Outside contributions are welcomed so long as they conform to using FOSS & the purpose.
'''


# command is currently used to install modules with pip if not already installed
import subprocess, sys
command = subprocess.os.system

# asks the user if they want to install tweepy if it isn't already installed
# we need tweepy for Twitter
def ask_tweepy():
    # strip() will remove extra spaces, lower() will lower the cases
    answer = input("Do you want to install tweepy now? y/n?  ").strip().lower()
    # linux is for GNU/Linux
    if (answer == 'y') and (sys.platform == 'linux'):
        command("pip3 install tweepy")
    # win32 will work regardless if the windows is 32 or 64 bit
    elif (answer == 'y') and (sys.platform == 'win32'):
        command("pip install tweepy")
    # darwin is for mac
    elif (answer == 'y') and (sys.platform == 'darwin'):
        command("pip3 install tweepy")
    elif (answer == 'n'):
        print("You need tweepy to run this, exiting")
        quit()
    else:
        print("please use y/n")
        ask()
        

try:
    import tweepy
except(ImportError):
    print("You need the tweepy module to use this")
    ask_tweepy()
    

class Soshii(object):

    # Docstring that will show up in help(Socii)
    '''
    Before you can use Socii for social meda platforms like twitter, you will first have to make an access token.
    You can make an access token for twitter by going here: https://developer.twitter.com/en/apps
    
    Instagram API : https://developers.facebook.com/products/instagram/apis/
    '''
    def __init__(self, twitter_pass, twitter_handle, twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_token_secret):
        self.twitter_pass = twitter_pass
        self.twitter_handle = twitter_handle
        self.twitter_consumer_key = twitter_consumer_key
        self.twitter_consumer_secret = twitter_consumer_secret
        self.twitter_access_token = twitter_access_token
        self.twitter_access_token_secret = twitter_access_token_secret
        
    def login_to_twitter(self):
       auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
       auth.set_access_token(access_token, access_token_secret)
       api = tweepy.API(auth)
       
    def login_to_instagram(self):
        pass
        
        
    def post_to_twitter(self, text_content, images_or_videos):
        pass #pass for now, we'll fill this up later
        
    def login_to_all(self):
        pass
        
    def post_to_all(self):
        pass # 
