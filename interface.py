import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import pystray
from PIL import Image
import threading
from charts import create_charts

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Аналитика экранного времени")
app.geometry("500x500")

conn = sqlite3.connect('data/screen_time.db')
df = pd.read_sql('SELECT * FROM screen_time_log', conn)
conn.close()

fig = create_charts(df)

# canvas_frame = ctk.CTkFrame(app)
# canvas_frame.pack()
# ROW = ctk.CTkFrame(canvas_frame)
# canvas = FigureCanvasTkAgg(fig, master=app)
# canvas.draw()

# f = canvas.get_tk_widget()
# ctk.CTkButton(ROW, 140, 28, text='button', command=f.pack)
app.mainloop()