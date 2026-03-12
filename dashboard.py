#import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

#st.title("📊 Аналитика моего экранного времени")

conn = sqlite3.connect('data/screen_time.db')
df = pd.read_sql('SELECT * FROM screen_time_log', conn)
conn.close()

duration_sort = df.groupby('process_name_usable')['duration_seconds'].agg(['sum']).sort_values(by='sum') / 60

ds_pie = duration_sort.copy()
mask_pie = ds_pie['sum'] < ds_pie['sum'].median()
ds_pie.index = ds_pie.index.to_series().mask(mask_pie, 'other')
ds_pie = ds_pie.groupby(ds_pie.index).sum()

top_three = duration_sort['sum'][-3:].to_list()

colors = ['#ff9999' if i in top_three else '#66b3ff' for i in duration_sort['sum']]
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

ax[0].barh(duration_sort.index.to_list(), duration_sort['sum'], color=colors, edgecolor='black')
ax[0].set_title('Экранное время')
ax[0].set_ylabel('Программы')
ax[0].set_xlabel('Время в мин.')

ax[1].pie(data=ds_pie, x='sum',labels=ds_pie.index.to_list(), autopct='%1.0f%%')
ax[1].set_title('Экранное время')

fig.subplots_adjust(left=None,
    bottom=None,
    right=None,
    top=None,
    wspace=0.5,)

plt.show()

#st.pyplot(fig)