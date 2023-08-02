import plotly.express as px
import requests

"""Get data from api"""

response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson")
all_eq_data = response.json()

"""Store earthquake data as variables"""

earthquakes = all_eq_data['features']
mags = [earthquake['properties']['mag'] for earthquake in earthquakes]
lons = [earthquake['geometry']['coordinates'][0] for earthquake in earthquakes]
lats = [earthquake['geometry']['coordinates'][1] for earthquake in earthquakes]
eq_titles = [earthquake['properties']['title'] for earthquake in earthquakes]

"""Plot data onto world map using scatter_geo function"""

title = all_eq_data['metadata']['title']
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles)
fig.show()