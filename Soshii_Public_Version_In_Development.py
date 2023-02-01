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
import json, requests

try:
    import tweepy
except(ImportError):
    print("You need tweepy to use this\nConsider installing with pip")

try:
    import requests-oauthlib
except(ImportError)
    print("You need requests-oathlib to use this\nConsider installing with pip")

try:
    import pandas as pd
except(ImportError)
    print("You need pands to use this\nConsider installing with pip")

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
