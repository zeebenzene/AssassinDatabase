import tkinter as tk
#import GUI.AssassinSearch
from AssassinSearch import Search

class button(tk.Button):
    def __init__(self, master, xPos, yPos, title, profileCanvas):
        tk.Button.__init__(self, master)
        self.master = master
        self.profCanvas = profileCanvas
        self.conf(xPos, yPos, title)
#         self.place(x = xPos, y = yPos)
        
        
    def conf(self, x, y, title):
        self.grid(row=x, 
                  column=y, 
                  columnspan=2,
                  padx=5, 
                  pady=5)
        self.config(fg="green", 
                    bg="black",
                    activebackground="black",
                    activeforeground="green",  
                    text=title, 
                    command=self.search,
                    font = ("Monospace", 16, "bold", "underline"))
    def search(self):
        a = Search()
        dict = self.master.getFields()
        choices = a.search(dict)
        self.profCanvas.setResultOptions(choices)