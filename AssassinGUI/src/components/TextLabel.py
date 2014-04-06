import tkinter as tk

class label(tk.Label):
    def __init__(self, master, xPos, yPos, text): 
        tk.Label.__init__(self, master)
        
        self.config(text = text, 
                    fg = "green",
                    bg = "black", 
                    font = ("Monospace",16))
        self.grid(row=xPos, 
                  column=yPos,
                  sticky="w",
                  padx=5,
                  pady=5)