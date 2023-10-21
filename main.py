import tweepy

# Set your Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create a Tweepy API object
api = tweepy.API(auth)

# Your tweet content
tweet_content = "Hello, Twitter! This is my first tweet from Python. #Python #Tweepy"

# Send the tweet
api.update_status(status=tweet_content)

print("Tweet sent successfully!")
