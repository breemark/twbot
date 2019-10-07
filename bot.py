import tweepy
import secrets

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

tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')

for tweet in tweets:
    if '#testing' in tweet.full_text.lower():
        print(str(tweet.id) + ' - ' + tweet.full_text)
        api.update_status("@" + tweet.user.screen_name + " Hola, this is a reply", tweet.id)
        store_last_seen(FILE_NAME, tweet.id)
