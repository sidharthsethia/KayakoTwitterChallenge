from TwitterSearch import *
from configparser import ConfigParser
from itertools import chain

# Parses the config.ini file and stores the keys in a dictionary named 'config'

parser = ConfigParser()
with open("config.ini") as lines:
    lines = chain(("[top]",), lines)
    parser.read_file(lines)
config = dict(parser.items('top'))


class Authorise:
    # It creates a TwitterSearch object with the secret tokens
    def __init__(self):
        self.twitter_search = TwitterSearch(
            consumer_key=config['consumer_key'],
            consumer_secret=config['consumer_secret'],
            access_token=config['access_token'],
            access_token_secret=config['access_token_secret']
        )

    # It returns the TwitterSearch object created
    def get_twitter_search(self):
        return self.twitter_search
