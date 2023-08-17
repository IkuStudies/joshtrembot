import tweepy

# credentials to access Twitter API
API_KEY='0h10UOJ4PArnW2GbPdrztIhv9'
API_KEY_SECRET='HbHtWXoZC8JdczZuevFvPKotyl0f3Ot3sKxgvcxThdLB1WzLtR'
BEARER_TOKEN='AAAAAAAAAAAAAAAAAAAAAJSppQEAAAAAkPYZtNo7HFpaaqGZAWz9%2BTullRY%3DgfN00YXPCJVMltyuTcJUlgDIpqVbMd002ru88YI7j6PGIUjX8d'
ACCESS_TOKEN='1691533329957314561-txhcYusMW6DxRhZ5QeB5vyM3M4Us88'
ACCESS_TOKEN_SECRET='GHFxnRcUAt2TGHfEWldLpS4NzzwKzRzM5qKF9d8sm1Yh1'

# create an OAuthHandler instance
client = tweepy.Client(
    BEARER_TOKEN,
    API_KEY,
    API_KEY_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
)

# V1 Twitter API Authentication
auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


# Upload image to Twitter. Replace 'filename' your image filename.
media_id = api.media_upload(filename="halloween.mp4").media_id_string
print(media_id)

# Text to be Tweeted
text = "second test, Hello World! its the leprechauns in your computer.if you can see the halloween music video the test has passed.  congrats, text and image are connected"

# Send Tweet with Text and media ID
client.create_tweet(text=text, media_ids=[media_id])
print("Tweeted!")