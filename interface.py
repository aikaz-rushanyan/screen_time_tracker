import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import pystray
from PIL import Image
import threading
from charts import create_charts

app = ctk.CTk()
app.title("Аналитика экранного времени")
app.geometry("500x500")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

conn = sqlite3.connect('data/screen_time.db')
df = pd.read_sql('SELECT * FROM screen_time_log', conn)
conn.close()

def on_close():
    
    # Отменяем все отложенные задачи через after_info()
    for task_id in app.after_info():
        try:
            app.after_cancel(task_id)
        except:
            pass
    
    app.destroy()


fig = create_charts(df)

top_frame = ctk.CTkFrame(app, 100, 100)
top_frame.pack(side='bottom')

app.protocol('WM_DELETE_WINDOW', on_close)
app.mainloop()