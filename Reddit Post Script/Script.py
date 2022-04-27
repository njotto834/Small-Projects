import praw
import time
import os
import webbrowser
import math

reddit = praw.Reddit(
    client_id = "",
    client_secret = "",
    user_agent = "",
)

subreddit = reddit.subreddit("CryptoCurrency")

already_seen = [] # for storing the ids of posts already seen
webpage_links = [] # stores the links of webpages
newPosts = False

while(1):
    os.system("cls") #Clears command line
    for submission in subreddit.new(limit=5):
        if (submission.id not in already_seen): #For new posts
            newPosts = True
            print(submission.title) #Prints title

            timeDiff = int(time.time())  - submission.created_utc #Subtracts time of post from current time
            timeDiff = math.trunc(timeDiff / 60) #Converts timeDiff to minutes.
            print(f"Posted {timeDiff} minutes ago.")

            print(f"Upvotes: {submission.score}") #Prints upvotes
            print(f"Comments: {submission.num_comments}") #Prints the number of comments
            print(submission.url)
            print("-----------------------------------------------------------") #Spacer
            subString = "reddit"
            if subString in submission.url: #Checks if the post url is to reddit
                webpage_links.append(submission.url)
            already_seen.append(submission.id) #Appends post to already_seen
        else:
            newPosts = False
            print("No new posts.")

    if (newPosts):
        val = input("Enter 'y' to open webpage(s).")
        if (val == "y"):
            for link in webpage_links:
                webbrowser.open(link)
    
    time.sleep(60) #Waits 60 seconds