import tkinter as tk

class text(tk.Text):
    def __init__(self, master, xPos, yPos, side):
        tk.Text.__init__(self, master)
        
        self.config(width = 20, 
                    height = 1)
        self.grid(row=xPos, 
                  column=yPos,
                  sticky=side,
                  padx=5,
                  pady=5)
        
    def setWidth(self, int):
        self.config(width = int)
    def setText(self, text):
        self.insert(0.0, text)
    def setSticky(self, side):
        self.config(sticky = text)
    def getText(self):
        return self.get(1.0, "end").rstrip("\n")