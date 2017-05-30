from flask import render_template

from app import app
from app.models.tweet import TweetSearch
import schedule
import time
from threading import Thread


#   The function which is called when the application url is hit
#   It returns the template after rendering which is then displayed

@app.route('/')
@app.route('/index')
def index():
    tweet = TweetSearch()
    return render_template("index.html",
                           title='Home',
                           hashtag=tweet.hashtag,
                           tweets=tweet.get_tweets())


def run_schedule():
    while 1:
        schedule.run_pending()
        time.sleep(1)


# Scheduling background task to fetch and save tweets every hour
tweet_search = TweetSearch()
schedule.every(5).minutes.do(tweet_search.fetch_and_save_tweets)
t = Thread(target=run_schedule)
t.start()
