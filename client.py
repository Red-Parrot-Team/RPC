import socket
import tkinter as tk
import gui_events as events
from classes.Info import Info

root = tk.Tk()
root.title("RP Chat")

messages = Info(root)

f_bottom = tk.Frame(root)

input_str = tk.StringVar()
input_widget = tk.Entry(f_bottom, text=input_str)
btn_enter = tk.Button(f_bottom, text="Enter")

messages.pack(expand=True, side=tk.TOP, fill=tk.BOTH)

f_bottom.pack(side=tk.BOTTOM, fill=tk.X)
btn_enter.pack(side=tk.RIGHT)
input_widget.pack(expand=True, fill=tk.X)

btn_enter.bind('<Button-1>', events.send_message)

root.mainloop()
