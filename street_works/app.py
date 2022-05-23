import streamlit as st
import pandas as pd
import numpy as np

import json

st.title("City works in Nancy")

st.write('The streets of Nancy are often criticized for being congested and works are not helping with that.')
st.markdown('This representation of the current street works in Nancy shows us the current possible deviation and mostly the traffic congestion in Nancy\'s streets.')

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        j = json.load(f)
    
    return j

json_data = load_data('./data.json')

st.subheader("This DataFrame represents the raw data fetched from a JSON file.")

df_all = pd.read_json('./data.json')
df_all


def process_data(json_data):
    dict_df = {
        'short_desc': [],
        'street': [],
        'coords': []
    }

    for item in json_data["incidents"]:
        s_desc = item["short_description"]
        street = item['location']['street']
        coords = (item['location']['polyline'].split(' ')[0], item['location']['polyline'].split(' ')[1])
        dict_df['short_desc'].append(s_desc)
        dict_df['street'].append(street)
        dict_df['coords'].append(coords)

    df = pd.DataFrame().from_dict(dict_df)
    return df

st.subheader('Now, you can see the selected data with only information interesting us.')

df = process_data(json_data)
df

def get_locations(df):
    coord_dict = {
        "lat": [],
        "lon": []
    }

    for coord in df.coords:
        lat, lon = coord
        coord_dict['lat'].append(float(lat))
        coord_dict['lon'].append(float(lon))

    df_coord = pd.DataFrame().from_dict(coord_dict)
    return df_coord

st.subheader('Here is the processed data with latitude and longitude.')

df_coord = get_locations(df)
df_coord

st.subheader('Map of all the city works in Nancy')
st.map(df_coord)