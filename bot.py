import tweepy
import secrets
import time
import dialogues
import random


consumer_key = secrets.consumer_key
consumer_secret = secrets.consumer_secret
access_token = secrets.access_token
access_token_secret = secrets.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        print("Replied to tweet: " + str(tweet.id))
        api.update_status("Hola  ""@" + tweet.user.screen_name + dialogues.say_what[random.randint(0, 5)] , tweet.id)
        api.create_favorite(tweet.id)
        api.retweet(tweet.id)
        store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(15)