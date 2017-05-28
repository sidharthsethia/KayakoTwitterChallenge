from TwitterSearch import *
from configparser import ConfigParser
from itertools import chain

#parser = ConfigParser()
# with open("config.ini") as lines:
#     lines = chain(("[top]",), lines)  # This line does the trick.
#     parser.read_file(lines)
# config = dict(parser.items('top'))

consumer_key = 'MDdLgmGiZOJORVcZpisrF1EzA'
consumer_secret = 'IamasD2Ze3hSyIksWYZNuHWqmkc8fGXaEDoNu1R90U6bZnHD2u'
access_token = '718172225-fc2ZFC9GCRuIEPv8Fv5RefC3CUUrtfaWLelhaMTL'
access_token_secret = 'WX1r0nueSxNF3kSv3K6n1AlRNqQzjxzH4EaM5vmfZV2If'

class Authorise:
    def __init__(self):
        # it's about time to create a TwitterSearch object with our secret tokens
        self.twitter_search = TwitterSearch(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )

    def get_twitter_search(self):
        return self.twitter_search
