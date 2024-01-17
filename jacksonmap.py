import pandas as pd
from geopy.geocoders import Nominatim
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import folium
import webbrowser

geolocator = Nominatim(timeout=10, user_agent="PDS")


df = pd.DataFrame([
    dict(Name="Ann D. Godfrey", Loc="Godfrey's Ferry, SC", Start='1829', Finish='1832', Admin='Jackson Administration 1 ,Jackson Administration'),
    dict(Name="Ann H. Richards", Loc="Joanne Furnace, PA", Start='1833', Finish='1844', Admin='Jackson Administration,Harrison / Tyler Administration'),
    dict(Name="Betsy S. Wilson", Loc="Ten Mile Stand, TN", Start='1829', Finish='1832', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Catharine M. Browner", Loc="New Windsor, MD", Start='1833', Finish='1844', Admin='Jackson Administration,Harrison / Tyler Administration'),
    dict(Name="Catherine Ann Canfield", Loc="New Philadelphia, OH", Start='1829', Finish='1848', Admin='Jackson Administration,Polk Administration'),
    dict(Name="Catherine Graham", Loc="Port Republic, VA", Start='1833', Finish='1840', Admin='Jackson Administration,Van Buren Administration'),
    dict(Name="Elizabeth Coffin Hoggatt", Loc="Paoli, IN", Start='1833', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Elizabeth Meyers Lauman", Loc="Middletown, PA", Start='1833', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Freeborn Rider", Loc="Rice City, RI", Start='1833', Finish='1840', Admin='Jackson Administration,Van Buren Administration'),
    dict(Name="Jane Compton", Loc="Manchester, SC", Start='1833', Finish='1840', Admin='Jackson Administration,Van Buren Administration'),
    dict(Name="Jane Dick", Loc="Dicks Mills, OH", Start='1829', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Margaret J. Walters", Loc="Lewistown, PA", Start='1829', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Margaret Johnston", Loc="Michigantown, IN", Start='1833', Finish='1840', Admin='Jackson Administration,Van Buren Administration'),
    dict(Name="Margaret M. Reid", Loc="Cotocton, MD", Start='1833', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Mary Odenheimer Deshong", Loc="Chester, PA", Start='1829', Finish='1840', Admin='Jackson Administration,Van Buren Administration'),
    dict(Name="Mary Dickson", Loc="Lancaster, PA", Start='1829', Finish='1852', Admin='Jackson Administration,Taylor / Fillmore Administration'),
    dict(Name="Mary M. Hayes", Loc="Hayesville, NC", Start='1833', Finish='1844', Admin='Jackson Administration,Harrison/Tyler Administration'),
    dict(Name="Mary McKain", Loc="High Rock, NC", Start='1833', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Rebecca Jewett Gay", Loc="Washington Hollow, NY", Start='1833', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Rebecca Sanders", Loc="Leesburg, OH", Start='1833', Finish='1836', Admin='Jackson Administration,Jackson Administration'),
    dict(Name="Sarah A. Cunningham", Loc="New London Crossroads, PA", Start='1833', Finish='1844', Admin='Jackson Administration,Harrison/Tyler Administration'),
    dict(Name="Sarah Davis", Loc="Paoli, PA", Start='1833', Finish='1848', Admin='Jackson Administration,Polk Administration'),
    dict(Name="Sarah Pryor", Loc="Pryors Vale, VA", Start='1833', Finish='1840', Admin='Jackson Administration,Van Buren Administration')
])

df['geocode'] = df['Loc'].apply(geolocator.geocode)


print(df)

df = df.dropna(how='any',axis=0) 

print(df)


df['latitude'] = [g.latitude for g in df.geocode]
df['longitude'] = [g.longitude for g in df.geocode]

print(df)


street_map = gpd.read_file('shp/cb_2018_us_state_5m.shp')

crs = {'init':'espg:4326'}
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]

geo_df = gpd.GeoDataFrame(df, geometry = geometry)

fig, ax = plt.subplots(figsize=(15,15))
street_map.plot(ax=ax, alpha=0.3,color='grey')
                
geo_df.plot(ax=ax, alpha=0.5, legend=True,markersize=10)

plt.title('Postmaster Positions', fontsize=15,fontweight='bold')
          
plt.xlim(-90.284, -68.787)
plt.ylim(32.612, 43.368)

plt.show()

po_map = folium.Map(location=(37.7, -82.22), zoom_start=10)
for index,row in df.iterrows(): 
  folium.Marker(location=(row['latitude'], 
                          row['longitude']), 
                popup=row['Name']).add_to(po_map)

po_map.save("map.html")
webbrowser.open("map.html")