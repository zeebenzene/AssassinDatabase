import tkinter as tk
from tkinter import *

class dropMenu(tk.OptionMenu):
    def __init__(self, master, xPos, yPos, choices):
        self.xPos = xPos
        self.yPos = yPos
        self.var = StringVar(master)
        self.var.set("select one") # initial value
        tk.OptionMenu.__init__(self, master, self.var, *choices)
        
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
    def getText(self):
        return self.var.get()
    
    def setChoices(self, choices):
        self.var.set("Results")
        self["menu"].delete(0, "end")
        for c in choices:
            self["menu"].add_command(label=c, command=tk._setit(self.var, c))
            
    def setSpan(self, direction, size):
        if direction == "rows":
            self.grid(row=self.xPos, column=self.yPos, rowspan=size, sticky="nsew")
        else:
            self.grid(row=self.xPos, column=self.yPos, columnspan=size, sticky="new")
