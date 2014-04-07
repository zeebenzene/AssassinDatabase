import tkinter as tk
from tkinter import *


class profileCanvas(tk.Canvas):
    def __init__(self, master):
        tk.Canvas.__init__(self, master, bg="gray")
        Grid.rowconfigure(master,0,weight=1)
        Grid.columnconfigure(master,1,weight=1)
        self.grid(row=0, column=1, sticky=("w","e","n","s"))
#         self.createWidgets()
        
    def createWidgets(self):
        photo = PhotoImage(file = '\\src\\1CLfizu.gif')
        label = tk.Label(self,image=photo)
        label.image = photo
        label.pack()