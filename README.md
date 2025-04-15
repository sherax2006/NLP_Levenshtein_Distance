
# 🎭 Classical Pakistani Drama Archive
A Streamlit web app to explore, search, and rediscover the golden era of Pakistani television dramas. This archive provides an interactive interface to browse through timeless classics by filtering based on year, actor, producer, director, writer, and drama name — with support for typo-tolerant search using Levenshtein distance.

📌 Features
🔍 Advanced Search Filters
Filter dramas by year, actor, producer, director, and writer.

🧠 Typo-Tolerant Search
Use Levenshtein distance to correct user input when searching drama names.

🎞️ Thumbnail Display
Each drama is visually represented with a thumbnail (with fallback support for missing images).

📅 Comprehensive Metadata
Display full information for each drama: year, cast, production team, and category.

🖼️ Google Image Link Parser
Automatically extracts valid image URLs from Google image search links.



The app uses a custom-curated CSV dataset (pakistani_dramas.csv) that includes:

Drama Name

Year

Actors

Producer

Director

Writer

Category

Thumbnail Image Link



🚀 Getting Started
🔧 Prerequisites
Python 3.7+

streamlit, pandas, python-Levenshtein
