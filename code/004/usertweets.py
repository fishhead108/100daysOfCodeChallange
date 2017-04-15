from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100

Tweet = namedtuple('Tweet', 'id_str created_at text')


class UserTweets(object):
    def __init__(self, handle, max_id=None):
        """Get handle and optional max_id.
        Use tweepy.OAuthHandler, set_access_token and tweepy.API
        to create api interface.
        Use _get_tweets() helper to get a list of tweets.
        Save the tweets as data/<handle>.csv"""

        if max_id:
            self.max_id = int(max_id)
        else:
            self.max_id = 9999999999999999999999999999999999999999999

        self.output_file = f'./{DEST_DIR}/test.{EXT}'

        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(self.auth)

        self.handle = handle
        self._tweets = list(self._get_tweets())
        self._save_tweets()

    def _get_tweets(self):
        """Hint: use the user_timeline() method on the api you defined in init.
        See tweepy API reference: http://docs.tweepy.org/en/v3.5.0/api.html
        Use a list comprehension / generator to filter out fields
        id_str created_at text (optionally use namedtuple)"""
        raw_tweets = [status for status in tweepy.Cursor(self.api.user_timeline, self.handle).items(NUM_TWEETS)]
        return [Tweet(tweet.id_str, tweet.created_at, (tweet.text).strip()) for tweet in raw_tweets if int(tweet.id_str) <= self.max_id]

    def _save_tweets(self):
        """Use the csv module (csv.writer) to write out the tweets.
        If you use a namedtuple get the column names with Tweet._fields.
        Otherwise define them as: id_str created_at text
        You can use writerow for the header, writerows for the rows"""
        with open(f'{self.output_file}', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(('id_str', 'created_at', 'text'))
            [writer.writerow(triple) for triple in self._tweets]

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, pos):
        return self._tweets[pos]


if __name__ == "__main__":
    USER = UserTweets('pybites')
    print(USER[0].id_str)
    print(USER[0].created_at)
    print(USER[0].text)
    #
    # for handle in ('pybites', 'techmoneykids', 'bbelderbos'):
    #     print('--- {} ---'.format(handle))
    #     user = UserTweets(handle)
    #     for tw in user[:5]:
    #         print(tw)
    #     print()
