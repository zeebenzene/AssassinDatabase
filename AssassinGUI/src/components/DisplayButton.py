import tkinter as tk
#import GUI.AssassinSearch
from AssassinSearch import Search

class button(tk.Button):
    def __init__(self, master, xPos, yPos, profileCanvas):
        tk.Button.__init__(self, master)
        self.master = master
        self.profCanvas = profileCanvas
        self.conf(xPos, yPos)
        
        
    def conf(self, x, y):
        self.grid(row=x, 
                  column=y, 
                  columnspan=2,
                  padx=5, 
                  pady=5,
                  sticky="s")
        self.config(fg="green", 
                    bg="black",
                    activebackground="black",
                    activeforeground="green",  
                    text="DISPLAY", 
                    command=self.displayProfile,
                    font = ("Monospace", 16, "bold", "underline"))
    def displayProfile(self):
        self.profCanvas.update()