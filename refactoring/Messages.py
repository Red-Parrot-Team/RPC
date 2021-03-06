import tkinter as tk

class Messages(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)
        
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self._text = tk.Text(self, state=tk.DISABLED, *args, **kwargs)
        self._text.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        scrollbar['command'] = self._text.yview
        self._text['yscrollcommand'] = scrollbar.set

    def write(self, text):
        self._text.configure(state=tk.NORMAL)
        self._text.insert(tk.END, text)
        self._text.configure(state=tk.DISABLED)
        self._text.yview_moveto('1.0')
    
    def clear(self):
        self._text.configure(state=tk.NORMAL)
        self._text.delete(0.0, tk.END)
        self._text.configure(state=tk.DISABLED)


    def flush(self):
        pass