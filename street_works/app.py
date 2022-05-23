import streamlit as st
import pandas as pd
import numpy as np

import json

st.title("City works in Nancy")

with open('./data.json', 'r', encoding='utf-8') as f:
    j = json.load(f)

dfs = []

dict_df = {
    'short_desc': [],
    'street': [],
    'coords': []
}

for item in j["incidents"]:
    s_desc = item["short_description"]
    street = item['location']['street']
    coords = (item['location']['polyline'].split(' ')[0], item['location']['polyline'].split(' ')[1])
    dict_df['short_desc'].append(s_desc)
    dict_df['street'].append(street)
    dict_df['coords'].append(coords)

df = pd.DataFrame().from_dict(dict_df)

df