from SearchCanvas import searchCanvas
from ProfileCanvas import profileCanvas
from tkinter import *
import tkinter as tk
import os


        
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title("Sample Application")
        self.createWidgets()
        self.pack(fill = "both", expand = 1)

    def createWidgets(self):
        pr = profileCanvas(self)
        cv = searchCanvas(self, pr)

app = Application()
app.mainloop()

#AMImages