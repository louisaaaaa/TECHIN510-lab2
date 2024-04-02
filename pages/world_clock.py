import streamlit as st
from datetime import datetime
import pytz
import time

# Function to get current time in a specific timezone
def get_current_time(city):
    tz = pytz.timezone(city['timezone'])
    current_time = datetime.now(tz)
    return city['name'], current_time.strftime('%Y-%m-%d %H:%M:%S'), int(current_time.timestamp())

# Define a list of cities with their timezones
cities = [
    {"name": "New York", "timezone": "America/New_York"},
    {"name": "London", "timezone": "Europe/London"},
    {"name": "Tokyo", "timezone": "Asia/Tokyo"}
]

# Display the current time for all selected cities
st.title("World Clock")
city_outputs = {}
while True:
    for city in cities:
        city_name, current_time, unix_timestamp = get_current_time(city)
        if city_name not in city_outputs:
            city_outputs[city_name] = st.empty()
        with city_outputs[city_name]:
            st.text(f"{city_name}: {current_time} (Unix Timestamp: {unix_timestamp})")
        time.sleep(1)
