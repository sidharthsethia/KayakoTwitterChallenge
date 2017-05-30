import sqlite3 as sql

import os
from datetime import datetime

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

DATABASE = os.path.join(PROJECT_ROOT, 'database.db')


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def insert_tweet(tweet_id_str, tweet_text, tweet_url, tweet_user, tweet_user_handle, created_at, retweet_count):
    con = sql.connect(DATABASE)
    cur = con.cursor()
    cur.execute(
        "INSERT INTO tweets (id_str,text,tweet_url,tweet_user,tweet_user_handle,created_at,retweet_count,timestamp) VALUES (?,?,?,?,?,?,?,?)",
        (tweet_id_str, tweet_text, tweet_url, tweet_user, tweet_user_handle, created_at, retweet_count, datetime.now()))
    con.commit()
    con.close()


def retrieve_tweets():
    con = sql.connect(DATABASE)
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute("SELECT * FROM tweets")
    tweets = cur.fetchall()
    con.close()
    return tweets


def delete_tweets(no_of_rows=0):
    con = sql.connect(DATABASE)
    con.row_factory = dict_factory
    cur = con.cursor()

    if no_of_rows == 0:
        cur.execute("DELETE FROM tweets")
    else:
        cur.execute("DELETE FROM tweets WHERE id IN (SELECT id FROM tweets ORDER BY id LIMIT {limit})"\
                    .format(limit=no_of_rows))

    con.close()


def retrieve_last_tweet():
    con = sql.connect(DATABASE)
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute("SELECT * FROM tweets WHERE id = (SELECT MAX(id) FROM tweets)")
    tweet = cur.fetchone()
    con.close()
    return tweet


def get_max_id():
    last_tweet = retrieve_last_tweet()
    if last_tweet is None:
        return ""
    else:
        return last_tweet['id_str']


def save_tweets_to_database(tweets):
    for tweet in tweets:
        insert_tweet(tweet['id_str'], tweet['text'], tweet['tweet_url'], tweet['user']['name'],
                     tweet['user']['screen_name'], tweet['created_at'], tweet['retweet_count'])
