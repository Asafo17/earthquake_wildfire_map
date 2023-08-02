import plotly.express as px
import csv

"""Get data from downloaded csv"""

with open("MODIS_C6_1_Global_24h.csv") as f:
    reader = csv.reader(f)
    next(reader, None)

    """Store wildfire data as variables"""

    lats, lons, brightness = [], [], []
    for row in reader:
        lats.append(row[0])
        lons.append(row[1])
        brightness.append(float(row[2]))


"""Plot data onto world map using scatter_geo function"""

title = "24Hr Wildfires"
fig = px.scatter_geo(lat=lats, lon=lons, title=title, projection='natural earth', color_discrete_sequence=['red'])
fig.show()