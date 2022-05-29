import praw
import time
import os
import webbrowser
import math
from plyer import notification
import telegram_send as tg

#Script to check for new posts of reddit.com/r/CryptoCurrency. When new posts are found, sends notifications via Telegram.

reddit = praw.Reddit(
    client_id = "",
    client_secret = "",
    user_agent = "",
)

subreddit = reddit.subreddit("CryptoCurrency")

already_seen = [] # for storing the ids of posts already seen
newPost = False #Checks if the last element checked was a new post
minuteTracker = 0
truncator = 0

while(1):
    anyNewPosts = False #Tracks if any new posts were found in this iteration.

    newPostTime = [] #Stores the amount of time since each new post was published.
    newPostTitles = [] #Stores the titles of new posts found in this iteration.
    webpage_links = [] #Stores the links of new posts found in this iteration.
    newPostUrls = [] #Stores the urls of new posts found in this iteration.
    pushMessages = [] #Stores each push notification message.

    os.system("cls") #Clears command line
    for submission in subreddit.new(limit=3):
        if (submission.id not in already_seen): #For new posts
            newPosts = True
            anyNewPosts = True
            minuteTracker = 0 #Tracks how many minutes the script has ran since a new post.

            newPostUrls.append(submission.url)
            newPostTitles.append(submission.title[:45])
            print(submission.title) #Prints title

            timeDiff = int(time.time())  - submission.created_utc #Subtracts time of post from current time
            timeDiff = math.trunc(timeDiff / 60) #Converts timeDiff to minutes.
            newPostTime.append(timeDiff) 
            print(f"Posted {timeDiff} minutes ago.") #Prints how long ago the post was published

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
                timeout = 10, #Notification stays for 10 seconds
            )

        postIndex = 0 #Index element for accessing array of new posts
        for new_post_url in newPostUrls:
            curPostTitle = newPostTitles[postIndex]
            if "reddit" in new_post_url: #If the url of the post is to reddit
                pushMessage = f"T({newPostTime[postIndex]}):{curPostTitle}\n{webpage_links[postIndex]}" 
            elif "jpg" in new_post_url: #If the post is just a picture:
                pushMessage = f"I({newPostTime[postIndex]}):{curPostTitle}\n{webpage_links[postIndex]}" 
            else: #If the url of the post is to an external website
                pushMessage = f"A({newPostTime[postIndex]}):{curPostTitle}\n{webpage_links[postIndex]}" 
            
            #push = pushB.push_note(pushTitle, webpage_links[postIndex]) #Sends mobile notification to PushBullet app
            pushMessages.append(pushMessage)

            postIndex += 1
        tg.send(messages=pushMessages)

        #Clears already_seen when 250 posts are found to free up memory
        if (len(already_seen) > 250){
            already_seen = []
            tg.send(messages=["CLEAR"])
        }
    
    time.sleep(60) #Waits 60 seconds
    minuteTracker += 1