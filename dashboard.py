#import streamlit as st
from charts import create_charts
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

#st.title("📊 Аналитика моего экранного времени")

conn = sqlite3.connect('data/screen_time.db')
df = pd.read_sql('SELECT * FROM screen_time_log', conn)
conn.close()

fig = create_charts(df)

plt.show()

#st.pyplot(fig)