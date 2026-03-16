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
app.geometry("1000x700")
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
    
    app.quit()


fig = create_charts(df, size=(10,5))
top_apps = df.groupby('process_name_usable')['duration_seconds'].agg(['sum']).sort_values(by='sum', ascending=False)[-5:] / 60 / 60
top_apps_dict = top_apps.to_dict()['sum']
#Фрейм для топ приложений
top_frame = ctk.CTkFrame(app, 300, 300)
top_frame.place(x=0, y=0)
top_frame_title = ctk.CTkLabel(top_frame, text='Топ приложений', font=("Arial", 20, "bold"))
top_frame_title.pack(pady=10, padx=20)
c = 1
for i in top_apps_dict:
    # Название и время
    label = ctk.CTkLabel(
        top_frame,
        text=f"{c}. {i} - {round(top_apps_dict[i], 3)} ч.",
        font=("Arial", 17),
        anchor="w"
    )
    label.pack(pady=2, padx=10, fill="x")
    c += 1
# canvas = FigureCanvasTkAgg(fig, top_frame)
# canvas.draw()

# canvas_widget = canvas.get_tk_widget()
# canvas_widget.pack(fill=ctk.BOTH, expand=True)

app.protocol('WM_DELETE_WINDOW', on_close)
app.mainloop()