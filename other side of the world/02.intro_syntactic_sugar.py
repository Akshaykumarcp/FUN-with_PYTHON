from folium import Map
# get latitude and longitude values
latitude = 40.09
longitude = 3.47

antipode_latitude = latitude * (-1)

# add 180 for negative longitude
# subtract 180 for positive longitude
if longitude <= 0: 
    antipode_longitude = longitude + 180
else:
    antipode_longitude = longitude - 180

location = [antipode_latitude, antipode_longitude]
mymap = Map(location)
mymap.save("other side of the world/antipode.html")

print(antipode_latitude)
print(antipode_longitude)
