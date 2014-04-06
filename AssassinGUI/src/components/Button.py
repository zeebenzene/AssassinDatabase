import tkinter as tk

class button(tk.Button):
    def __init__(self, master,xPos, yPos, title):
        tk.Button.__init__(self, master)
        self.master = master
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
                    command=self.getName,
                    font = ("Monospace", 16, "bold", "underline"))
    
    def getName(self):
        for l in self.master.getFields():
            print(l.getText())
    
    def changeColour(self):
        if(self["bg"] == "black"):
            self.config(bg="blue")
        else: 
            self.config(bg="black")