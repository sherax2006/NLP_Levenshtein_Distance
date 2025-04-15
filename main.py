# drama_archive_app.py

import streamlit as st
import pandas as pd
import os
import Levenshtein

# Load data
df = pd.read_csv('./pakistani_dramas.csv')

# Page settings
st.set_page_config(page_title="Classical Pakistani Drama Archive", layout="wide")
st.title("📺 Classical Pakistani Drama Archive")

# Sidebar filters
st.sidebar.header("🔎 Search Filters")
year_filter = st.sidebar.selectbox("Search by Year", ["All"] + sorted(df["year"].unique().tolist()))
actor_filter = st.sidebar.text_input("Search by Actor")
producer_filter = st.sidebar.text_input("Search by Producer")
director_filter = st.sidebar.text_input("Search by Director")
writer_filter = st.sidebar.text_input("Search by Writer")
drama_name_filter = st.sidebar.text_input("Search by Drama Name (Supports Typo Correction)")

# Apply filters
filtered_df = df.copy()

if year_filter != "All":
    filtered_df = filtered_df[filtered_df["year"] == year_filter]

if actor_filter:
    filtered_df = filtered_df[filtered_df["actors"].str.contains(actor_filter, case=False)]

if producer_filter:
    filtered_df = filtered_df[filtered_df["producer"].str.contains(producer_filter, case=False)]

if director_filter:
    filtered_df = filtered_df[filtered_df["director"].str.contains(director_filter, case=False)]

if writer_filter:
    filtered_df = filtered_df[filtered_df["writer"].str.contains(writer_filter, case=False)]

if drama_name_filter:
    filtered_df['levenshtein_distance'] = filtered_df['name'].apply(
        lambda x: Levenshtein.distance(x.lower(), drama_name_filter.lower()))
    threshold = 3
    filtered_df = filtered_df[filtered_df['levenshtein_distance'] <= threshold]
    filtered_df = filtered_df.sort_values(by='levenshtein_distance')

# Display results
st.markdown("### 🎞️ Drama Results")
cols = st.columns(3)

fallback_image_url = "https://via.placeholder.com/300x400?text=No+Image"

# Display each drama
for idx, row in filtered_df.iterrows():
    with cols[idx % 3]:
        image_url = row.get("thumbnail")
        if not image_url or pd.isna(image_url) or not image_url.startswith("https"):
            image_url = fallback_image_url
        
        st.image(image_url, caption=row["name"], use_column_width=True)
        st.write(f"📅 Year: {row['year']}")
        st.write(f"🎭 Actors: {row['actors']}")
        st.write(f"🧑‍💼 Producer: {row['producer']}")
        st.write(f"🎬 Director: {row['director']}")
        st.write(f"✍️ Writer: {row['writer']}")
        st.write(f"🏷️ Category: {row['category']}")
        if 'levenshtein_distance' in row:
            st.write(f"🔍 Levenshtein Distance: {row['levenshtein_distance']}")
