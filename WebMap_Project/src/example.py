import folium

m = folium.Map([0,0], zoom_start=5, tiles="OpenStreetMap", attr='My Data Attribution')

# 'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png'

trail_coordinates = [
    (-71.351871840295871, -73.655963711222626),
    (-71.374144382613707, -73.719861619751498),
    (-71.391042575973145, -73.784922248007007),
    (-71.400964450973134, -73.851042243124397),
    (-71.402411391077322, -74.050048183880477),
]

folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(m)

group_1 = folium.FeatureGroup("first group").add_to(m)
folium.Marker((0, 0), 
    icon=folium.Icon("red")
).add_to(group_1)

folium.Marker((3, 0), 
    tooltip="Click me!",
    popup="Mt. Hood Meadows",
    icon=folium.Icon("red")
).add_to(group_1)

group_2 = folium.FeatureGroup("second group").add_to(m)
folium.Marker((0, 2),
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(icon="cloud", color="green")
).add_to(group_2)

m.save("index.html")