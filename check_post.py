#Sensitive data removed; get the client id and secret info from Reddit account

import praw
import send_sms

from spreadsheet import Spreadsheet

# Create the Reddit instance
reddit = praw.Reddit('bot1')

# and login
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='',
                     username='',
                     password='')

subreddit = reddit.subreddit('3dprintmything')

# Get the newest 6 values from the subreddit
for submission in subreddit.new(limit=6):
    #print(submission.title)
    spreadsheet = Spreadsheet(submission.id)
    seen_bool = spreadsheet.run()
    counter = 0
    # If we haven't seen this post before
    if not seen_bool:
        send_sms.send_alert()











