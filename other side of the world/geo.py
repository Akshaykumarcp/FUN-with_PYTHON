# pip install pytz for timezones subclass to pass for datetime module
# pip install timezonefinder for getting timezone based on latitude and longitude
# pip install sunnyday for weather

from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import random, uniform
from folium import Marker

class Geopoint(Marker): # parent/super class Marker for inheritance

    latitude_range = (-90,90) # class variable, used to provide info in general
    longitude_range = (-180,180)
    # pi = 3.14

    def __init__(self, latitude, longitude, popup=None):
        super().__init__(location= [latitude,longitude], popup = popup)
        self.latitude = latitude # instance variables created using self
        self.longitude = longitude

    def closest_parallel(self):
        return round(self.latitude)

    def get_time(self):
        timezone_string = TimezoneFinder().timezone_at(lat = self.latitude, lng = self.longitude)
        time_now = datetime.now(timezone(timezone_string))
        return time_now

    # instance method
    def get_weather(self):
        weather = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", lat = self.latitude, lon  = self.longitude)
        return weather.next_12h_simplified()

    # class method
    @classmethod
    def random(cls):
        return cls(latitude = uniform(-90,90), longitude = uniform(-180,180))

tokyo = Geopoint(latitude = 35.7,longitude = 139.7)

print(tokyo.latitude, tokyo.longitude) # instance evariable
# 35.7 139.7

print(Geopoint.latitude_range, Geopoint.longitude_range) # class variable
# (-90, 90) (-180, 180)

print(tokyo.closest_parallel())
print(tokyo.get_time())
print(tokyo.get_weather())
print(Geopoint.random())
""" 
36
2022-05-03 14:37:03.964479+09:00 
[('2022-05-03 06:00:00', 67.69, 'few clouds', '02d'), ('2022-05-03 09:00:00', 65.84, 'few clouds', '02d'), ('2022-05-03 12:00:00', 61.9, 'few clouds', '02n'), ('2022-05-03 15:00:00', 58.84, 'clear sky', '01n')]
<__main__.Geopoint object at 0x00000173940D2E08>
"""

random_point = Geopoint.random()

print(random_point.latitude)
print(random_point.longitude)
print(random_point.get_weather())
""" 
89.58223371027546
119.33828310285821
[('2022-05-03 06:00:00', 11.23, 'overcast clouds', '04d'), ('2022-05-03 09:00:00', 10.29, 'overcast clouds', '04d'), ('2022-05-03 12:00:00', 7.3, 'overcast clouds', '04d'), ('2022-05-03 15:00:00', 4.46, 'broken clouds', '04d')] """
