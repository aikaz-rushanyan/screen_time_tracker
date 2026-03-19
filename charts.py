import pandas as pd
import matplotlib.pyplot as plt

def create_barh(data, size=(10, 5), quality=200):
    duration_sort = data.groupby('process_name_usable')['duration_seconds'].agg(['sum']).sort_values(by='sum')[-5:] / 60 / 60
    top_three = duration_sort['sum'][-3:].to_list()

    colors = ['#ff9999' if i in top_three else '#66b3ff' for i in duration_sort['sum']]
    fig, ax = plt.subplots(figsize=size, dpi=quality)

    bars = ax.barh(
        duration_sort.index.to_list(), 
        duration_sort['sum'], 
        color=colors, 
        edgecolor='white',
        linewidth=1.5,
        height=0.6,
        )
    ax.bar_label(bars, fmt='%.1f ч.', color='white', fontsize=15, padding=5)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.set_facecolor('#2b2b2b')
    ax.tick_params(colors='white', labelsize=15)
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
    duration_sort = data.groupby('process_name_usable')['duration_seconds'].agg(['sum']).sort_values(by='sum')[-5:] / 60 / 60
    ds_pie = duration_sort.copy()
    mask_pie = ds_pie['sum'] <= ds_pie['sum'].iloc[-4]
    ds_pie.index = ds_pie.index.to_series().mask(mask_pie, 'Other')
    ds_pie = ds_pie.groupby(ds_pie.index).sum().sort_values(by='sum', ascending=False)

    fig, ax = plt.subplots(figsize=size, dpi=quality,constrained_layout=True)

    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc', '#c499ff']

    ax.pie(
        data=ds_pie,
        x='sum',
        labels=None,
        autopct='%1.0f%%',
        colors=colors,
        radius=1.1,
        wedgeprops={'edgecolor': 'white', 'linewidth': 2},
        pctdistance=0.75,
        textprops={'color': 'white', 'fontsize': 10, 'weight':'bold'},
        explode=[0.1, 0, 0, 0,],
        shadow=False
    )
    ax.set_title('Экранное время')
    ax.set_facecolor('#2b2b2b')
    ax.title.set_color('white')
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
