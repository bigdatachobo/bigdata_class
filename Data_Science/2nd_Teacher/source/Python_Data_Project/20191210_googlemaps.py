# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:37:32 2019

@author: sundooedu
"""

#%%
import googlemaps

gmaps_key="AIzaSyBKRq7_4cl5CG-p7rpn4jAAsayRK4qoWYc"
gmaps=googlemaps.Client(key=gmaps_key)

gmaps.geocode('서울중부경찰서', language='ko')
#%%

