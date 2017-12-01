#!/usr/bin/env python

import os
import logging
import urllib
import tweepy

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

# from twitter_client import TwitterClient

# Login credentials for user twansform.app account on Twitter,
# replace these with your own OAuth key credentials.  The easiest
# way to do this is to use the Python's tweepy API interactively.
CONSUMER_KEY = "xxxxxxxxxxxxxxxxxxxx"
CONSUMER_SECRET = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
ACCESS_TOKEN_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


class TextTransform(webapp.RequestHandler):
    def get(self, username, nitems=1):
        self.response.headers["Content-type"] = "text/plain"
        try:
            nitems = int(nitems)
        except Exception, e:
            raise Exception, "number of items must be an integer: %s" % (e)
        
        twitter_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        twitter_auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
        twitter_api = tweepy.API(twitter_auth)
        
        timeline = twitter_api.user_timeline(username, count=nitems)
        for status in timeline:
            text = str(status.text.encode('ascii', 'xmlcharrefreplace'))
            self.response.out.write(text + "\r\n")
                     
    def handle_exception(self, exception, debug_mode):
        self.response.headers["Content-type"] = "text/plain"
        self.response.out.write("twansform: an internal error has occurred (%s). Sorry!" % str(exception))
        

application = webapp.WSGIApplication(
                [('/(.*)/text', TextTransform),
                 ('/(.*)/text/(.*)', TextTransform)],
                debug=False)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
