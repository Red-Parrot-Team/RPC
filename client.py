import socket
import tkinter as tk
from Report import Report

root = tk.Tk()
root.title("RP Chat")

messages = Report(root)

f_bottom = tk.Frame(root)

input_str = tk.StringVar()
input_widget = tk.Entry(f_bottom, text=input_str)
btn_enter = tk.Button(f_bottom, text="Enter")

messages.pack(expand=True, side=tk.TOP, fill=tk.BOTH)

f_bottom.pack(side=tk.BOTTOM, fill=tk.X)
btn_enter.pack(side=tk.RIGHT)
input_widget.pack(expand=True, fill=tk.X)


root.mainloop()
