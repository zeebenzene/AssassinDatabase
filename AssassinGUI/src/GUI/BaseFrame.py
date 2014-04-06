from SearchCanvas import searchCanvas as search
from ProfileCanvas import profileCanvas as profile
from tkinter import *
import tkinter as tk


        
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title("Sample Application")
        self.createWidgets()
        self.pack(fill = "both", expand = 1)

    def createWidgets(self):
        cv = search(self)
        pr = profile(self)

app = Application()
app.mainloop()