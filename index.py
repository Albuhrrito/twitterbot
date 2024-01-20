import tweepy
import os
from dotenv import load_dotenv

load_dotenv()  # This loads the .env file

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# OAuth 1.0a User Context authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
client = tweepy.Client(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET,access_token=ACCESS_KEY,access_token_secret=ACCESS_SECRET)
client.create_tweet(text="Hello World")


# Create API object
api = tweepy.API(auth)

# Function to tweet
def tweet_v2(message):
    try:
        api.update_status(status=message)
        print("Tweet posted successfully!")
    except Exception as e:
        print("An error occurred: {}".format(e))

# Tweet content
tweet = "It's Gym time, Sailers!"

# Posting the tweet
tweet_v2(tweet)
