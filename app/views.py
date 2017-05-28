from app import app
from flask import render_template

from app.statics.tweet import TweetSearch


@app.route('/')
@app.route('/index')
def index():
    twitter_search = TweetSearch()
    tweets = twitter_search.get_tweets()
    return render_template("index.html",
                           title='Home',
                           hashtag=twitter_search.hashtag,
                           tweets=tweets)
