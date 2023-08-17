import ephem
from datetime import datetime, timedelta
import time

# Planetary hours in Chaldean order
planetary_hours = [
    "Saturn", "Jupiter", "Mars", "Sun", "Venus", "Mercury", "Moon"
]

# Major Tetramorph signs
tetramorph_signs = ["Leo", "Taurus", "Scorpio", "Aquarius"]

# Calculate Chaldean planetary hour
def calculate_planetary_hour(sunset, current_time):
    time_diff = current_time - sunset
    hour_index = int((time_diff.total_seconds() / 3600) // 2)
    return planetary_hours[hour_index % len(planetary_hours)]

# Get sunrise and sunset times
def get_sun_times(observer):
    sun = ephem.Sun()
    sunrise = observer.next_rising(sun)
    sunset = observer.next_setting(sun)
    return sunrise, sunset

# Get UTC time
def get_utc_time():
    return datetime.utcnow().strftime("%H:%M:%S")

# get planetary positions
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
        positions.append(f"{planet_symbol[planet.name]}:{zodiac_symbol[zodiac_sign]}")
    
    return positions

# Get predominant sign in the night sky
def get_predominant_tetramorph():
    current_hour = datetime.utcnow().hour
    index = (current_hour + 2) % len(tetramorph_signs)  # Assuming 10:30 pm corresponds to index 2
    return tetramorph_signs[index]

if __name__ == "__main__":
    observer = ephem.Observer()
    observer.lat = "30.961428"  # Ancient Sumeria latitude
    observer.long = "46.103771"  # Ancient Sumeria longitude
    
    while True:
        current_time = datetime.utcnow()
        observer.date = current_time  # Set observer's date to current UTC time
        planetary_positions = get_planetary_positions()
                
        sunrise, sunset = get_sun_times(observer)
        chaldean_planetary_hour = calculate_planetary_hour(sunset.datetime(), current_time)
        utc_time = get_utc_time()
        tetramorph = get_predominant_tetramorph()
        
        print(f"Chaldean Planetary Hour: {chaldean_planetary_hour}")
        print(f"Time (in UTC): {utc_time}")
        print(f"Sunrise: {sunrise}")
        print(f"Sunset: {sunset}")
        print(f"Major Tetramorph: {tetramorph}")
        print("Planetary positions:", ", ".join(planetary_positions))
        print()  # Print an empty line for readability
        
        time.sleep(300)   # Wait for 5 minutes before generating the next printout
