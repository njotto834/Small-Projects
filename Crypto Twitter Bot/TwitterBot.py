import tweepy as tp
from configparser import ConfigParser
from datetime import datetime
import pytz
import time

config  = ConfigParser()
config.read('config.ini')

api_key = config['twitter']['API_Key']
api_key_secret = config['twitter']['API_Key_Secret']

access_token = config['twitter']['Access_Token']
access_token_secret = config['twitter']['Access_Token_Secret']

#authentication
auth = tp.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tp.API(auth)

elon_screen_name = "elonmusk"
elon_user_id = api.get_user(screen_name = elon_screen_name).id

while(1):
    #Gets current time in GMT
    tz_GMT = pytz.timezone('GMT') 
    now = datetime.now(tz_GMT)

    elonTweets = api.user_timeline(user_id=elon_user_id, count=5, tweet_mode='extended')

    for tweet in elonTweets:
        timePosted = (tweet.created_at) #GMT DateTime from when the tweet was posted
        timeDifference = now - timePosted #datetime.timedelta object
        seconds = timeDifference.total_seconds() #Amount of seconds between the current time and the time the tweet was posted.
        tweetText = tweet.full_text.lower() #Turns tweet text all lowercase.
        if (seconds < 60):
            print(tweetText)
            if ('doge' in tweetText) or ('shiba' in tweetText) or ('to the moon') in tweetText:
                print("Tweet Found")
                
    time.sleep(60) #Waits 60 seconds
    

