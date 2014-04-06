import tkinter as tk
from tkinter import *
from components.Button import button
from components.TextLabel import label
from components.TextBox import text 
from components.DropDownMenu import dropMenu

class searchCanvas(tk.Canvas):
    def __init__(self, master):
        tk.Canvas.__init__(self, master, bg="black")
        
        self.createWidgets()
#         self.pack(fill = "y", expand = 1, anchor = "e")
        Grid.rowconfigure(master,0,weight=1)
#         Grid.columnconfigure(master,1,weight=1)
        self.grid(row=0, column=1, sticky=("n","s","e"))
        

    def createWidgets(self):
        self.createHeader()
        self.createNameSearch()
        self.createAgeSearch()
        self.createHeightSearch()
        self.createWeightSearch()
        self.createNationalitySearch()
        self.createHeader()
        self.createEmployerSearch()
        self.createSuccessSearch()
        self.createFlawSearch()
        self.createRatingSearch()
        b1 = button(self, 10, 0, "SEARCH")
    
    def createHeader(self):
        header = tk.Label(self)
        header.config(text="Basic Info",
                      font=("Helvetica",20,"bold"),
                      bg="black",
                      fg="green")
        header.grid(row=0, 
                    column=0, 
                    columnspan=2,
                    pady=10)
        
    def createNameSearch(self):
        nameLabel = label(self, 1, 0, "Name:")
        nameText = text(self, 1, 1)
        nameText.setText("name")
          
    def createAgeSearch(self): 
        ageOptions = []
        for i in range(100):
            ageOptions.append(i)
        ageMenu=dropMenu(self, 2, 1, ageOptions)
        ageLabel = label(self, 2, 0, "Age:")
    
    def createHeightSearch(self):
        heightLabel = label(self, 3, 0, "Height:")

        heightFeet = tk.Text(self, height=1, width=10)
        heightFeet.insert(0.0, "feet")

        heightFeet.grid(row=3, 
                        column=1, 
                        sticky="w", 
                        padx=5)

        heightInches  = tk.Text(self, height=1, width=10)
        heightInches.insert(0.0, "inches")
        heightInches.grid(row=3, 
                          column=1, 
                          sticky="e", 
                          padx=5)
    
    def createWeightSearch(self):
        weightLabel = label(self, 4, 0, "Weight:")
        weightText = tk.Text(self, 
                             height=1, 
                             width=10)
        weightText.insert(0.0, "lbs")
        weightText.grid(row=4, 
                        column=1, 
                        sticky="w", 
                        padx=5)
    
    def createNationalitySearch(self):
        options = ["American", "Russia", "Slovakia", "Bulgaria", "Lithuania", "Argentina", "Brazil", "Chile", "Columbia", "Djibouti", "Liberia", "South Africa"]
        nationalityMenu = dropMenu(self, 5, 1, options)
        nationalityLabel = label(self, 5, 0, "Nationality:")
    
    def createEmployerSearch(self):
        options = ["Independent", "Italian Mafia", "Russian Mafia", "Anonymous", "lulzsec", "Yakuza", "Triads", "CIA", "MI6"]
        employerMenu= dropMenu(self, 6, 1, options)
        employerLabel = label(self, 6, 0, "Employer:")
    
    def createSuccessSearch(self):
        options = []
        for i in range(0, 110, 10):
            options.append(i) 
        successMenu= dropMenu(self, 7, 1, options)
        successLabel = label(self, 7, 0, "Successes(%):")

    def createFlawSearch(self):
        options = ["garlic", "puppies", "one direction", "food", "pepper spray", "friendship", "teletubbies"]
        flawMenu = dropMenu(self, 8, 1, options)
        employerLabel = label(self, 8, 0, "Flaw:")
    
    def createRatingSearch(self):
        options = []
        for i in range(0, 11):
            options.append(i)
        ratingMenu = dropMenu(self, 9, 1, options)
        employerLabel = label(self, 9, 0, "Avg. Rating:")        