import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('data/screen_time.db')
df = pd.read_sql('SELECT * FROM screen_time_log', conn)
conn.close()

duration_sort = df.groupby('process_name_usable')['duration_seconds'].agg(['sum']).sort_values(by='sum')[-5:] / 60 / 60

ds_pie = duration_sort.copy()
mask_pie = ds_pie['sum'] <= ds_pie['sum'].iloc[-4]
ds_pie.index = ds_pie.index.to_series().mask(mask_pie, 'other')
ds_pie = ds_pie.groupby(ds_pie.index).sum()

def create_barh(data, size=(10, 5), quality=200):

    top_three = duration_sort['sum'][-3:].to_list()

    colors = ['#ff9999' if i in top_three else '#66b3ff' for i in duration_sort['sum']]
    fig, ax = plt.subplots(figsize=size, dpi=quality)

    ax.barh(duration_sort.index.to_list(), duration_sort['sum'], color=colors, edgecolor='white')
    ax.set_facecolor('#2b2b2b')
    ax.tick_params(colors='white')
    ax.set_title('Экранное время')
    ax.title.set_color('white')
    ax.set_ylabel('Программы')
    ax.yaxis.label.set_color('white')
    ax.set_xlabel('Время в час.')
    ax.xaxis.label.set_color('white')
     
    fig.patch.set_facecolor("#2b2b2b")
    fig.subplots_adjust(left=None,
        bottom=None,
        right=None,
        top=None,
        wspace=0.5,)
    
    return fig

def create_pie(data, size=(10, 5), quality=200):
    fig, ax = plt.subplots(figsize=size, dpi=quality)

    ax.pie(data=ds_pie, x='sum',labels=None, autopct='%1.0f%%')
    ax.set_title('Экранное время')
    ax.set_facecolor('#2b2b2b')
    ax.title.set_color('white')
    ax.pie(
        data=ds_pie, 
        x='sum',
        labels=None, 
        autopct='%1.0f%%',
        textprops={'color': 'white', 'fontsize': 10}  # цвет и размер текста
    )
    ax.legend(
        ds_pie.index.to_list(),
        loc='center left',
        bbox_to_anchor=(1, 0, 0.5, 1),
        labelcolor='white',
        facecolor='#2b2b2b',
        edgecolor='white',
        fontsize=9)
    
    fig.patch.set_facecolor("#2b2b2b")
    fig.subplots_adjust(left=None,
        bottom=None,
        right=None,
        top=None,
        wspace=0.1,)
    
    return fig
