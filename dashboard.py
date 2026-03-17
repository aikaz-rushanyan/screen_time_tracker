from charts import create_barh, create_pie
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import streamlit as st

st.title("📊 Аналитика моего экранного времени")

conn = sqlite3.connect('data/screen_time.db')
df = pd.read_sql('SELECT * FROM screen_time_log', conn)
conn.close()

fig_bar = create_barh(df, size=(8, 6), quality=300)
fig_pie = create_pie(df, size=(8, 6), quality=100)

st.pyplot(fig_bar)
st.pyplot(fig_pie)