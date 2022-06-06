import praw
import time
import os
import webbrowser
import math
from plyer import notification
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

reddit = praw.Reddit(
    client_id = config['reddit']['client_id'],
    client_secret = config['reddit']['client_secret'],
    user_agent = config['reddit']['user_agent'],
)

subreddit = reddit.subreddit("CryptoCurrency")

already_seen = [] # for storing the ids of posts already seen
newPost = False #Checks if the last element checked was a new post
minuteTracker = 0
truncator = 0

while(1):
    anyNewPosts = False #Tracks if any new posts were found in this iteration.
    newPostTitles = []
    webpage_links = [] # stores the links of new posts found in this iteration
    os.system("cls") #Clears command line
    for submission in subreddit.new(limit=3):
        if (submission.id not in already_seen): #For new posts
            newPosts = True
            anyNewPosts = True
            minuteTracker = 0 #Tracks how many minutes the script has ran since a new post.

            newPostTitles.append(submission.title[:45])
            print(submission.title) #Prints title

            timeDiff = int(time.time())  - submission.created_utc #Subtracts time of post from current time
            timeDiff = math.trunc(timeDiff / 60) #Converts timeDiff to minutes.
            print(f"Posted {timeDiff} minutes ago.")

            print(f"Upvotes: {submission.score}") #Prints upvotes
            print(f"Comments: {submission.num_comments}") #Prints the number of comments
            print(submission.url)
            print("-----------------------------------------------------------") #Spacer

            postID = submission.id
            url = f"https://www.reddit.com/r/CryptoCurrency/comments/{postID}" #Creates a reddit url for each post.
            webpage_links.append(url)

            already_seen.append(submission.id) #Appends post to already_seen
        else:
            newPost = False
        
    if (newPost == False and anyNewPosts == False):
        print(f"No new posts.({minuteTracker})")

    if (anyNewPosts):
        postTitles = '\n'.join(newPostTitles) #Turns the elements of newPostTitles into a String.

        notification.notify( #Creates a desktop notification.
                title = "New post(s) on r/CryptoCurrency",
                message = postTitles,
                app_icon = None,
                timeout = 120, #Notification stays for 2 minutes
            )
    
    time.sleep(60) #Waits 60 seconds
    minuteTracker += 1