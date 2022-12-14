#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:05:00 2022

@author: elena
"""
import numpy as np
import geojson
from urllib.request import urlretrieve
import webbrowser
import os
from motionless import DecoratedMap, LatLonMarker
from tempfile import mkdtemp
import folium
from folium.features import DivIcon
from folium import plugins

url = 'https://static.avalanche.report/weather_stations/'
suffix = "_stations.geojson"
datetime = "2021-10-12_04-00"

GOOGLE_API_KEY = 'AIzaSyAjPH6t6Y2OnPDNHesGFvTaVzaaFWj_WCE'

def file_download(date):
    file_path = os.path.join('/Users/elena/programming/data/l/', date + suffix)
    file_url = url + date + suffix
    urlretrieve(file_url, file_path)
    return file_path



with open('/Users/elena/programming/data/l/2021-10-12_04-00_stations.geojson') as f:
    gj = geojson.load(f)
stations = gj['features']

variables = list()
for i in stations:
    variables = variables + list(i.properties.keys())

variables = np.unique(variables)

m = folium.Map(location=[47, 12])

variable = 'LT'

def temp_marker_color(temp):
    if temp < -15:
        color = '#A800FF'
    if temp >= -15 and temp < -10:
        color = '#0079FF'
    if temp >= -10 and temp < 0:
        color = 'cyan'
    if temp >= 0 and temp < 10:
        color = '#00F11D'
    if temp >= 10 and temp < 20:
        color = 'yellow'
    if temp >= 20 and temp <30:
        color = 'orange'
    if temp >= 30 and temp <35:
        color = 'red'
    if temp >= 35:
        color = '#c9241b'
    return color
    
def temperature_plot(station):
    value = round(station.properties[variable], 1)
    text = f'''Region: {i.properties["LWD-Region"]} <br>
            Station: {i.properties["name"]} <br>
            Elevation: {i.geometry.coordinates[2]} m <br>
            ''' 
    iframe = folium.IFrame(text, width=200, height=250)
    popup = folium.Popup(iframe, max_width=3000)
    folium.CircleMarker(location=station.geometry.coordinates[0:2][::-1],
                        radius=20,    
                        color=temp_marker_color(value),
                        opacity=0.7,
                        fill_color=temp_marker_color(value),
                        fill_opacity=0.7,
                        popup=popup,
                        tooltip='Click for details'
                        ).add_to(m)
    folium.map.Marker(station.geometry.coordinates[0:2][::-1],
                      icon=DivIcon(
                      #icon_size=(20,20),
                      icon_anchor=(10,10),
                      html=f'<div style="font-size: 8pt">{value}</div>',
                      )).add_to(m)




for i in stations:
    if variable in i.properties:
    # temperature_plot(i)

     # folium.Marker(
     #    location=i.geometry.coordinates[0:2][::-1], 
     #    icon=folium.features.CustomIcon('./data/arrow_icon.png', icon_size=(20,20))
     #    ).add_to(m)
     folium.Marker(
        location=i.geometry.coordinates[0:2][::-1], 
        icon=DivIcon(html = '<i class="glyphicon glyphicon-leaf gly-rotate-10"></i>', icon_size=(20,20))
        ).add_to(m)     
     
        
     
        # value = round(i.properties[variable], 1)
        # text = f'''Region: {i.properties["LWD-Region"]} <br>
        #         Station: {i.properties["name"]} <br>
        #         Elevation: {i.geometry.coordinates[2]} m <br>
        #         ''' 
        # iframe = folium.IFrame(text, width=200, height=250)
        # popup = folium.Popup(iframe, max_width=3000)
        # # icon_value = plugins.BeautifyIcon(
        # # border_color=temp_marker_color(value),
        # # text_color=temp_marker_color(value),
        # # number=value,
        # # inner_shape='circle',
        # # icon_size =(40,40))
        # # folium.Marker(
        # # location=i.geometry.coordinates[0:2][::-1],
        # # popup='nice place',
        # # icon=icon_value
        # # ).add_to(m)
        # folium.CircleMarker(location=i.geometry.coordinates[0:2][::-1],
        #                     radius=20,    
        #                     color=temp_marker_color(value),
        #                     opacity=0.7,
        #                     fill_color=temp_marker_color(value),
        #                     fill_opacity=0.7,
        #                     popup=popup,
        #                     tooltip='Click for details'
        #                     ).add_to(m)
        # folium.map.Marker(i.geometry.coordinates[0:2][::-1],
        #                   icon=DivIcon(
        #                   #icon_size=(20,20),
        #                   icon_anchor=(10,10),
        #                   html=f'<div style="font-size: 8pt">{value}</div>',
        #                   )).add_to(m)

   # print(i.geometry.coordinates[0:2])
    #print(marker)
   # m.add_child(marker)
m.save('map.html')
#webbrowser.open("map.html")
webbrowser.get().open_new_tab("file:///Users/elena/programming/climvis-master/climvis/map.html")

def get_googlemap_url(lon, lat, zoom=10):

    dmap = DecoratedMap(lat=lat, lon=lon, zoom=zoom,
                        size_x=640, size_y=640,
                        maptype='terrain', key=GOOGLE_API_KEY)
    dmap.add_marker(LatLonMarker(lat, lon))
    return dmap.generate_url()


# with open('/Users/elena/programming/climvis-master/climvis/data/template.html', 'r') as infile:
#     lines = infile.readlines()
#     out = []
#     url = get_googlemap_url(12, 47, zoom=8)
#     outpath = os.path.join(mkdtemp(), 'index.html')
#     with open(outpath, 'w') as outfile:
#         outfile.writelines(out)
        
# dmap = DecoratedMap(lat=47, lon=11.5, zoom=7.5,
#                     size_x=1920, size_y=1080,
#                     maptype='terrain', key=GOOGLE_API_KEY)
# for i in stations[0:200]:
#     dmap.add_marker(LatLonMarker(i.geometry.coordinates[1], i.geometry.coordinates[0], label='J'))
# dmap.add_marker(LatLonMarker(47.098, 11.87, label='B'))
# print(dmap.generate_url())


# dmap = DecoratedMap(lat=47, lon=12, zoom=8,
#                     size_x=640, size_y=640,
#                     maptype='terrain', key=GOOGLE_API_KEY)
# outpath = os.path.join(mkdtemp(), 'index.html')
# with open(outpath, 'w') as outfile:
#     outfile.writelines([])
    
# webbrowser.get().open_new_tab(dmap.generate_url())