import json
from TwitterSearch import *
from app.models.authorise import Authorise


# TweetSearch class: endpoint for fetching the tweets using the twitter search API

class TweetSearch:
    # Constructor
    def __init__(self):
        self.max_tweets = 50  # no of tweets to be fetched
        self.hashtag = '#custserv'  # hastag to be searched
        self.twitter_search = Authorise().get_twitter_search()  # get twitter search object after authentication
        self.twitter_search_order = TwitterSearchOrder()  # create a TwitterSearchOrder object which will have all the search parameters
        self.twitter_search_order.set_keywords([self.hashtag])  # set the hashtag
        self.twitter_search_order.set_language('en')  # filter english tweets
        self.twitter_search_order.set_include_entities(False)  # Doesnt fetch extra information

    # Sets the search parameters to the twitter search order object
    # @param since_id - to fetch tweets after this id
    # @param keywords - keywords to be searched
    # @param include_entities - boolean flag to include extra information
    # @param language - filters tweets according to this language
    def set_twitter_search_order(self, since_id, keywords="", include_entities=False, language='en'):
        if keywords == "":
            keywords = self.hashtag

        self.twitter_search_order.set_keywords(keywords)  # let's define all words we would like to have a look for
        self.twitter_search_order.set_language(language)  # we want to see english tweets only
        self.twitter_search_order.set_include_entities(
            include_entities)  # and don't give us all those entity information
        self.twitter_search_order.set_since_id(since_id)

    # @return results - json array of tweets fetched
    def get_tweets(self):

        retweets = {}  # dictionary conatining tweet id as key and tweet json data as value

        try:

            actual_count = 0
            # tweets are fetched with
            for tweet in self.twitter_search.search_tweets_iterable(self.twitter_search_order):
                actual_count += 1

                # Each retweeted tweed has the 'retweeted status parameter' whereas other tweets dont have the parameter
                # The retweeted tweet's Id is checked for in the dictionary, if not found, tweet is added to dictionary

                if 'retweeted_status' in tweet and tweet['retweeted_status']['id_str'] not in retweets:
                    retweets[tweet['retweeted_status']['id_str']] = tweet['retweeted_status']

                # The size of the dictionary is checked to be within 'max_tweets' required
                if len(retweets) == self.max_tweets:
                    break

            results = []  # list of resultant tweets

            # For each tweet in the dictionary's Values,
            for tweet in retweets.values():
                # create tweet url to link each tweet with twitter
                tweet_url = "https://twitter.com/" + tweet['user']['screen_name'] + "/status/" + tweet['id_str']
                tweet['tweet_url'] = tweet_url

                # add the tweet to results
                results.append(tweet)

                # for tweet in results:
                #     print(tweet)

                # print(actual_count)
                # print(len(results))

        except TwitterSearchException as e:  # take care of all those ugly errors if there are some
            print(e)

        string_response = json.dumps(results)
        return json.loads(string_response)
