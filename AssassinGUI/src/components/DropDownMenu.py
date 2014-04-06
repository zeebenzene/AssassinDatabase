import tkinter as tk
from tkinter import *

class dropMenu(tk.OptionMenu):
    def __init__(self, master, xPos, yPos, choices):
        var = StringVar(master)
        var.set("select one") # initial value
        tk.OptionMenu.__init__(self, master, var, *choices)
        
        self["menu"].config(bg="black",
                            fg="green")
        
        self.config(font=('Helvetica, 12'),
                    bg='black',
                    fg='green',
                    activebackground="black",
                    activeforeground="green",
                    justify="left",
                    relief="flat",
                    bd=0,
                    width=10)
        self.grid(row=xPos, 
                  column=yPos, 
                  sticky="w",
                  padx=5,
                  pady=5)