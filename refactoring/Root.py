import tkinter as tk
from Messages import Messages
import socket

class Root(tk.Frame):

    def __init__(self, master=None, *cnf, **kw):
        super().__init__(master=master, *cnf, **kw)
        self.title = "RP Chat"

        self.socket = socket.socket()
        self.socket.connect(('localhost', 9999))

        self.messages = Messages(self)
        self.frame = tk.Frame(self)
        self.btn_send = tk.Button(self.frame, text="Enter")
        self.input_str = tk.StringVar()
        self.input_field = tk.Entry(self.frame, text=self.input_str)
        self.btn_quit = tk.Button(self.frame, text="Quit")
        
        self.configGUI()
        self.bindingEvents()

    def configGUI(self):
        self.pack(expand=True, fill=tk.BOTH)
        self.messages.pack(expand=True, side=tk.TOP, fill=tk.BOTH)
        self.frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.btn_send.pack(side=tk.RIGHT, anchor=tk.N)
        self.input_field.pack(expand=True, fill=tk.X)
        self.btn_quit.pack()

    def bindingEvents(self):
        self.btn_send.bind('<Button-1>', self.sendMsg)
        self.btn_quit.bind('<Button-1>', self.end)

    def sendMsg(self, event):
        print(self.input_str.get())
        self.socket.send(self.input_str.get().encode('utf-8'))
        data = self.socket.recv(1024).decode('utf-8')
        self.messages.write(data + '\n')

    def end(self, event):
        self.quit()