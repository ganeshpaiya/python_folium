
# %%


import folium

# initialize a map with center and zoom
mapObj = folium.Map(location=[21.437730075416685, 77.255859375],
                     zoom_start=4, tiles=None)

# add tile layers
folium.TileLayer('openstreetmap').add_to(mapObj)
folium.TileLayer('stamenterrain', attr="stamenterrain").add_to(mapObj)
folium.TileLayer('stamenwatercolor', attr="stamenwatercolor").add_to(mapObj)
folium.TileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', name='CartoDB.DarkMatter', attr="CartoDB.DarkMatter").add_to(mapObj)

# add layers control over the map
folium.LayerControl().add_to(mapObj)

# save the map as html file
mapObj.save('folium_intro.html')

# initialize a map with center and zoom
mapObj = folium.Map(location=[22.167057857886153, 82.44140625000001],
                    zoom_start=5)

# https://leafletjs.com/reference-1.7.1.html#path
# border styles dictionary
bordersStyle = {
    'color': 'green',
    'weight': 2,
    'fillColor': 'blue',
    'fillOpacity': 0.2
}

folium.GeoJson(
    data=(open("states_india.geojson", 'r').read()),
    name="India",
    style_function=lambda x: bordersStyle).add_to(mapObj)

folium.GeoJson(
    data=(open("srilanka.geojson", 'r').read()),
    name="Srilanka",
    style_function=lambda x: bordersStyle).add_to(mapObj)

# add layer control over the map
folium.LayerControl().add_to(mapObj)

# save the map as html file
mapObj.save('GeoJSON.html')


mapObj1 = folium.Map(location=[29.36003483162285, 47.92613983154297], zoom_start=5,loc='en',tiles='CartoDB Positron')


folium.Circle(location=[29.36003483162285, 47.92613983154297],
              radius=50000
              ).add_to(mapObj1)

# add tile layers
folium.TileLayer('openstreetmap').add_to(mapObj1)
folium.TileLayer('stamenterrain', attr="stamenterrain").add_to(mapObj)
folium.TileLayer('stamenwatercolor', attr="stamenwatercolor").add_to(mapObj)
folium.TileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', name='CartoDB.DarkMatter', attr="CartoDB.DarkMatter").add_to(mapObj)

# add layers control over the map
folium.LayerControl().add_to(mapObj1)
             

mapObj1.save('circlemarkers.html')



mapObj = folium.Map(location=[29.36003483162285, 47.92613983154297],
                    zoom_start=5,tiles='CartoDB Positron')

folium.Marker(location=[29.36003483162285, 47.92613983154297],
              popup=folium.Popup('<i>The center of map</i>'),
              tooltip='Center'
              ).add_to(mapObj)

# https://lab.artlung.com/font-awesome-sample/
# remember to use prefix='fa'
folium.Marker(location=[29, 47],
              icon=folium.Icon(icon='magnet', prefix='fa', color='red'),
              popup=folium.Popup(
                  """Using the magnet icon from font-awesome.<br/>
                  Check out more <a href="https://lab.artlung.com/font-awesome-sample/" target="_blank">here</a><br/>
                  """, max_width=500),
              tooltip='Font awesome example'
              ).add_to(mapObj)

# https://getbootstrap.com/docs/3.3/components/
folium.Marker(location=[29, 46],
              icon=folium.Icon(icon='glyphicon-plane', color='green'),
              popup=folium.Popup(
                  """
                  <img src="https://avatars.githubusercontent.com/u/2918581?v=4" alt="Bootstrap" style="max-width:100%;max-height:100%"><br/>
                  <h4>
                  glyphicon-plane icon from bootstrap.<br/>
                  </h4>
                  <h5>Check out more <a href="https://getbootstrap.com/docs/3.3/components/" target="_blank">here</a></h5>
                  """, max_width=300),
              tooltip='Bootstrap example'
              ).add_to(mapObj)

mapObj.save('Drawmarkers.html')




# %%
