import time
import tweepy

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

image_path = 'C:/Your_image_path/'

tweets = [
    ['image_one.jpg', 'Your_some_text_one.'],
    ['image_two.jpg', 'Your_some_text_two.']
]

for tweet in tweets:
    status = api.update_with_media(image_path + tweet[0], tweet[1])
    time.sleep(60)
