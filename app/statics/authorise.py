from TwitterSearch import *
from configparser import ConfigParser
from itertools import chain

parser = ConfigParser()
with open("config.ini") as lines:
    lines = chain(("[top]",), lines)  # This line does the trick.
    parser.read_file(lines)
config = dict(parser.items('top'))


class Authorise:
    def __init__(self):
        # it's about time to create a TwitterSearch object with our secret tokens
        self.twitter_search = TwitterSearch(
            consumer_key=config['consumer_key'],
            consumer_secret=config['consumer_secret'],
            access_token=config['access_token'],
            access_token_secret=config['access_token_secret']
        )

    def get_twitter_search(self):
        return self.twitter_search
