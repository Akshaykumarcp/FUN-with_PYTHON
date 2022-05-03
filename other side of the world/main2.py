from folium import Map, Marker, Popup
from geo import Geopoint

# get latitude and longitude values
latitude = 13.03
longitude = 77.54

locations = [[41,-1],[40,2],[39,5],[42,6]]

# folium map instance
mymap = Map(location = [40,2])

""" # Create a Marker instance and add to map
madrid = Marker(location = [latitude, longitude], popup = "Hi there!")
madrid.add_to(mymap) """

for lat, lon in locations:
    # Create a Geopoint instance
    geopoint = Geopoint(latitude=lat,longitude=lon) 
    # geopoint = Geopoint(latitude=latitude,longitude=longitude, popup = geopoint.get_weather()) # not a good practise to create object twice
    # so create a instance for Popup and assign value

    forecast = geopoint.get_weather()

    popup_content = f"""
    {forecast[0][0][-8:-6]}h: {round(forecast[0][1])}F <img src="https://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[1][0][-8:-6]}h: {round(forecast[1][1])}F <img src="https://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[2][0][-8:-6]}h: {round(forecast[2][1])}F <img src="https://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[3][0][-8:-6]}h: {round(forecast[3][1])}F <img src="https://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png" width=35>
    """

    popup = Popup(popup_content, max_width=400)
    popup.add_to(geopoint)
    geopoint.add_to(mymap)

# save the map instance into a HTML file
mymap.save("other side of the world/map.html")
