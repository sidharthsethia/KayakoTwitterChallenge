import json

from TwitterSearch import *

from app.models.authorise import Authorise


class TweetSearch:
    def __init__(self):
        self.no_of_tweets = 50
        self.hashtag = '#custserv'
        self.twitter_search = Authorise().get_twitter_search()
        self.twitter_search_order = TwitterSearchOrder()  # create a TwitterSearchOrder object
        self.twitter_search_order.set_keywords([self.hashtag])  # set the hashtag
        self.twitter_search_order.set_language('en')  # we want to see english tweets only
        self.twitter_search_order.set_include_entities(False)  # and don't give us all those entity information

    def set_tso(self, since_id, keywords="", include_entities=False, language='en'):
        if keywords == "":
            keywords = self.hashtag

        self.twitter_search_order.set_keywords(keywords)  # let's define all words we would like to have a look for
        self.twitter_search_order.set_language(language)  # we want to see english tweets only
        self.twitter_search_order.set_include_entities(
            include_entities)  # and don't give us all those entity information
        self.twitter_search_order.set_since_id(since_id)

    def get_tweets(self):
        retweets = {}

        try:

            actual_count = 0
            # this is where the fun actually starts :)
            for tweet in self.twitter_search.search_tweets_iterable(self.twitter_search_order):
                actual_count += 1
                if 'retweeted_status' in tweet and tweet['retweeted_status']['id_str'] not in retweets:
                    retweets[tweet['retweeted_status']['id_str']] = tweet['retweeted_status']
                if len(retweets) == self.no_of_tweets:
                    break

            results = []

            # For each tweet in the dictionary's Values,
            for tweet in retweets.values():
                # add the tweet to results
                tweet_url = "https://twitter.com/" + tweet['user']['screen_name'] + "/status/" + tweet['id_str']
                tweet['tweet_url'] = tweet_url
                results.append(tweet)

            # for tweet in results:
            #     print(tweet)

            # print(actual_count)
            # print(len(results))

        except TwitterSearchException as e:  # take care of all those ugly errors if there are some
            print(e)

        string_response = json.dumps(results)
        return json.loads(string_response)
