import tkinter as tk
from tkinter import *


class profileCanvas(tk.Canvas):
    def __init__(self, master):
        tk.Canvas.__init__(self, master, bg="gray")
        Grid.rowconfigure(master,0,weight=2)
        Grid.columnconfigure(master,0,weight=2)
        self.grid(row=0, column=0, sticky=("n","w","s","e"))
      
        self.createWidgets()
        
    def createWidgets(self):
        photo = PhotoImage(file = 'C:\\Users\\Kit\\Pictures\\1CLfizu.gif')
        label = tk.Label(self,image=photo)
        label.image = photo
        label.pack()