import ephem
import tweepy
from datetime import datetime, timedelta
import time

# Twitter API credentials
consumer_key = "dOk1gvBUlvufOQB5rF8okn7TD"
consumer_secret = "iWQPg1CMRMCSr2t597PrpNqJQU6W1EuAPkhnkVyAgsZqbLIJpK"
access_token = "1691533329957314561-LV1aZUzYPXTCnwzBnanQmDDItU67Sn"
access_token_secret = "CJfOIr2ccPSKDRMbjYxXdBdQ7Ynv8FBt8MOvRmsCXvWaQ"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Calculate Chaldean planetary hour
def calculate_planetary_hour(current_hour):
    planetary_hours = [
        "Saturn", "Jupiter", "Mars", "Sun", "Venus", "Mercury", "Moon"
    ]
    index = (current_hour // 3) % len(planetary_hours)
    return planetary_hours[index]

# Get current UTC time
def get_utc_time():
    return datetime.utcnow().strftime("%H:%M:%S")

# Get planetary zodiac positions using emoji symbols
def get_planetary_positions():
    observer = ephem.Observer()
    planets = [
        ephem.Saturn(), ephem.Jupiter(), ephem.Mars(),
        ephem.Sun(), ephem.Venus(), ephem.Mercury(), ephem.Moon()
    ]
    
    positions = []
    for planet in planets:
        planet.compute(observer)
        planet_symbol = {
            "Saturn": "♄", "Jupiter": "♃", "Mars": "♂",
            "Sun": "☉", "Venus": "♀", "Mercury": "☿", "Moon": "☽"
        }
        zodiac_sign = ephem.constellation(planet)[1]
        zodiac_symbol = {
            "Aries": "♈", "Taurus": "♉", "Gemini": "♊", "Cancer": "♋",
            "Leo": "♌", "Virgo": "♍", "Libra": "♎", "Scorpio": "♏",
            "Sagittarius": "♐", "Capricorn": "♑", "Aquarius": "♒", "Pisces": "♓"
        }
        positions.append(f"{planet_symbol}{zodiac_symbol[zodiac_sign]}")
    
    return positions

# Major Tetramorph signs
tetramorph_signs = ["Leo", "Taurus", "Scorpio", "Aquarius"]

# Get predominant sign in the night sky
def get_predominant_tetramorph():
    # Perform actual sky observations or use your preferred method to determine
    # the predominant sign in the night sky at 10:30 pm.
    # For this example, we'll use a simplified method.
    
    current_hour = datetime.utcnow().hour
    index = (current_hour + 2) % len(tetramorph_signs)  # Assuming 10:30 pm corresponds to index 2
    
    return tetramorph_signs[index]

# Tweet information
def tweet_information():
    current_hour = datetime.utcnow().hour
    
    planetary_hour = calculate_planetary_hour(current_hour)
    utc_time = get_utc_time()
    planetary_positions = get_planetary_positions()
    tetramorph = get_predominant_tetramorph()
    
    tweet = (
        f"UTC time: {utc_time}\n"
        f"Chaldean planetary hour: {planetary_hour}\n"
        f"Planetary positions: {' '.join(planetary_positions)}\n"
        f"Upcoming morning stars: (stars heliacally rising in the coming week)\n"
        f"Major 10:30 pm Tetramorph: {tetramorph}"
    )
    
    # Check if the tweet length exceeds 280 characters
    if len(tweet) <= 280:
        api.update_status(status=tweet)
    else:
        print("Tweet length exceeds 280 characters.")

if __name__ == "__main__":
    tweet_information()