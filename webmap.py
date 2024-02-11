# To install folium [in terminal]: pip3 install folium

import folium

# Create map object with location parameter and zoom parameter
lat, lon = 45.00151734710523, -50.89676158991404  # Latitude and longitude of starting coordinates
zoom_start = 3  # Starting zoom of map
my_map = folium.Map(location=[lat, lon], tiles="cartodbpositron", zoom_start=zoom_start)


# Add point markers on top of the base map
# marker with parameters location, popup, and icon(color)
# Places I have lived = blue
lived = folium.FeatureGroup(name="Places I have Lived")
lived.add_child(folium.Marker(location =[40.151548,-75.336974],popup="East Norriton,PA", icon=folium.Icon(color='blue')))
lived.add_child(folium.Marker(location =[39.747955162889156, -104.98095059112701],popup="Denver,CO", icon=folium.Icon(color='blue')))
lived.add_child(folium.Marker(location =[40.146670681543135, -75.33099043629173],popup="Horsham,PA", icon=folium.Icon(color='blue')))
lived.add_child(folium.Marker(location =[34.76866046555023, -84.76938089976325],popup="Chatsworth,GA", icon=folium.Icon(color='blue')))
lived.add_child(folium.Marker(location =[40.156426977195466, -75.09472889763887],popup="Hatboro,PA", icon=folium.Icon(color='blue')))
lived.add_child(folium.Marker(location =[26.048401509681646, -81.66554684545115],popup="Naples,FL", icon=folium.Icon(color='blue')))
lived.add_child(folium.Marker(location =[35.73336367403041, -78.84912806646683],popup="Apex, NC", icon=folium.Icon(color='blue')))
lived.add_child(folium.Marker(location =[34.90218546132974, -85.14530303385718],popup="Ringgold, GA", icon=folium.Icon(color='blue')))
lived.add_child(folium.Marker(location =[34.769726337816316, -84.97032636744872],popup="Dalton, GA", icon=folium.Icon(color='blue')))

# Places I have visited = green
visited = folium.FeatureGroup(name="Places I have Visited")
visited.add_child(folium.Marker(location =[45.508592531747624, -73.5546939030243],popup="Montreal, QC", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[42.36056493503479, -71.05916980477625],popup="Boston, MA", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[40.759923276275, -73.98562868758818],popup="New York, NY", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[34.062014417949534, -118.2510574480344],popup="Los Angeles, CA", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[34.02288881530071, -118.4958795395205],popup="Santa Monica, CA", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[34.133830483228714, -118.67575812994458],popup="Calabasas, CA", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[40.01381711463127, -105.27124883151734],popup="Boulder, CO", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[51.50710234552548, -0.13034637107382877],popup="London, UK", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[52.731431849998465, 15.23780484735478],popup="Gorzów Wielkopolski, PL", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[52.52291312443885, 13.418476819198158],popup="Berlin, DE", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[52.37284832286652, 4.894940418504577],popup="Amsterdam, NL", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[35.715430955437775, -83.51314013879222],popup="Gatlinburg, TN", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[35.789772817876155, -83.55932805732816],popup="Pigeon Forge, TN", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[35.83846075192259, -89.406736527897],popup="Gates, TN", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[38.044528923190335, -84.49261084624828],popup="Lexington, KY", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[36.16623518845187, -86.78119487686008],popup="Nashville, TN", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[35.14704299944772, -90.0539419697877],popup="Memphis, TN", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[35.0416225772001, -85.30919387828048],popup="Chattanooga, TN", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[53.797809878881274, -1.54877557228795],popup="Leeds, UK", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[25.79019918589062, -80.14163459020278],popup="Miami, FL", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[29.90043122911792, -81.31572979948434],popup="St. Augustine, FL", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[30.399901316302305, -86.49153545036081],popup="Destin, FL", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[28.530269109053155, -81.42536899574313],popup="Orlando, FL", icon=folium.Icon(color='green')))
visited.add_child(folium.Marker(location =[33.75501366167892, -84.39020921042525],popup="Atlanta, GA", icon=folium.Icon(color='green')))

# adds children to map
my_map.add_child(lived)
my_map.add_child(visited)

# saves the map as html file
my_map.save('map1.html')   # Needs to be at the end of the file


