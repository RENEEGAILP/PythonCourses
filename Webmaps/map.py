import folium
import pandas


def get_color(elevation):
    if elevation < 1000:
        return 'cadetblue'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


MyMap = folium.Map(location=[38.58, -99.89], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

DataPoints = pandas.read_csv("MarkerPoints.txt")
lat = DataPoints["LAT"]
lon = DataPoints["LON"]
elev = DataPoints["ELEV"]
name = DataPoints["NAME"]

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=(lt, ln), radius=6, popup=folium.Popup(iframe, parse_html=True),
                                     fill_color=get_color(el), color='grey', fill=True, fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population Density")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
MyMap.add_child(fgv)
MyMap.add_child(fgp)
MyMap.add_child(folium.LayerControl())
MyMap.save("MyMap.html")
