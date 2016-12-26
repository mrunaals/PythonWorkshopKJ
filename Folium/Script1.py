# Leaflet using Folium Package
# Author: Prashant Nair
# Install folium
#pip install folium
#While importing you may face error saying 'jinja2' is not installed. Thus you
# may also need to install jinja2
# pip install jinja2
# For Crime Report Viz Refer on the below link
# https://blog.dominodatalab.com/creating-interactive-crime-maps-with-folium/

import folium

# Use dir(folium) to figure out the methods and associated objects

map = folium.Map(location=[18.9220,72.8347],zoom_start=12)

# Gateway of India/Coordinates
# 18.9220 N, 72.8347 E
#45.372,-121.697

# Create a marker to the map help(folium.Map.simple_marker)
# https://mynasadata.larc.nasa.gov/latitudelongitude-finder/?lat=&lng=

map.simple_marker(location=[18.9220,72.8347],popup='Gateway of India',marker_color='red')


# Create html file dir(folium.map)

map.create_map(path='test.html')
