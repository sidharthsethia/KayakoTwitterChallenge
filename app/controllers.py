from flask import render_template

from app import app
from app.models.tweet import TweetSearch

#   The function which is called when the application url is hit
#   It returns the template after rendering which is then displayed
@app.route('/')
@app.route('/index')
def index():
    twitter_search = TweetSearch()
    tweets = twitter_search.get_tweets()
    return render_template("index.html",
                           title='Home',
                           hashtag=twitter_search.hashtag,
                           tweets=tweets)
