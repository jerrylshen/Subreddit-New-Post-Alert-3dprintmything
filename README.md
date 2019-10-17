This script checks for the newest 6 posts in subreddit r/3dprintmything via Praw, records/check their submission ID on a Google Sheet via gspread to make sure there's no false positives, then texts to my number when there's a new post via Twilio.

The code can be modified to check different subreddits and such, one would have to generate the client/keys info from Reddit, Google, and Twilio.

Reason: I have a 3D printer and am trying to sell my prints on the subreddit, so I want to know whenever there's a new post
