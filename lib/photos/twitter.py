#################
#PHOTOBOOTH FILE#
#################
import twitter

def tweet(message):
    twitter_config = get_twitter_credentials()

    api = twitter.Api(consumer_key=twitter_config['consumer_key'],
                      consumer_secret=twitter_config['consumer_secret'],
                      access_token_key=twitter_config['access_token'],
                      access_token_secret=twitter_config['access_token_secret'],
                      tweet_mode='extended')

    api.PostUpdate(message);

def get_twitter_credentials():
    pass

