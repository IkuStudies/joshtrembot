import tweepy

# Twitter API credentials for bot
consumer_key = "YOUR_BOT_CONSUMER_KEY"
consumer_secret = "YOUR_BOT_CONSUMER_SECRET"
access_token = "YOUR_BOT_ACCESS_TOKEN"
access_token_secret = "YOUR_BOT_ACCESS_TOKEN_SECRET"

# Authenticate w Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Screen name main account
main_account_screen_name = "YOUR_MAIN_ACCOUNT_SCREEN_NAME"

# Search tweets from main account
main_account_tweets = api.user_timeline(screen_name=main_account_screen_name, count=10)

# Loop through main account tweets and respond to comments
for tweet in main_account_tweets:
    comments = api.search(q=f"to:{main_account_screen_name}", since_id=tweet.id)
    
    for comment in comments:
        if comment.in_reply_to_status_id == tweet.id:
            user = comment.user.screen_name
            response = (
                f"behold I am josh trembot! I have detected you have commented on my master's post, "
                f"I commend your effort, stalrad! Would you like to go on an adventure? "
                f"If so, type 'yes'. If no, type 'gtfo bot boy'"
            )
            
            api.update_status(
                status=f"@{user} {response}",
                in_reply_to_status_id=comment.id
            )
