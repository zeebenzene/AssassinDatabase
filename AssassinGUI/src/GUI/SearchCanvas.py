import tkinter as tk
import sqlite3
from tkinter import *
from components.SearchButton import button
from components.TextLabel import label
from components.TextBox import text 
from components.DropDownMenu import dropMenu



class searchCanvas(tk.Canvas):    
    conn = sqlite3.connect("C:\\Users\\Kit\\workspace\\NewAssassinProject\\src\\startup\\AssassinMingle") #DATA BASE FILE GOES HERE
    cur = conn.cursor()

    def __init__(self, master, profileCanvas):
        tk.Canvas.__init__(self, master, bg="black")
        Grid.rowconfigure(master,0,weight=1)
        self.grid(row=0, column=0, sticky=("n","s","w"))
        self.createWidgets(profileCanvas)    
    
    def createWidgets(self, profileCanvas):
        self.createHeader()
        self.createNameSearch()
        self.createAgeSearch()
        self.createHeightSearch()
        self.createWeightSearch()
        self.createNationalitySearch()
        self.createHeader()
        self.createEmployerSearch()
        self.createSuccessSearch()
        self.createMissionSearch()
        self.createSuccessMissions()
#         self.createFailedMissions()
        self.createRatingSearch()
        b1 = button(self, 12, 0, "SEARCH", profileCanvas)
    
    def createHeader(self):
        header = label(self, 0, 0, "Search Assassins")
        header.setSize(20)
        header.setSpan("column", 2)
        
    def createNameSearch(self):
        nameLabel = label(self, 1, 0, "Name:")
        self.nameText = text(self, 1, 1, "w")
        self.nameText.setText("name")
          
    def createAgeSearch(self): 
        ageLabel = label(self, 2, 0, "Age:")
        self.ageMin = text(self, 2, 1, "w")
        self.ageMin.setText("min")
        self.ageMin.setWidth(9)
        
        self.ageMax = text(self, 2, 1, "e")
        self.ageMax.setText("max")
        self.ageMax.setWidth(9)
    
    def createHeightSearch(self):
        heightLabel = label(self, 3, 0, "Height:")
        
        self.heightMin = text(self, 3, 1, "w")
        self.heightMin.setText("min(cm)")
        self.heightMin.setWidth(9)
        
        self.heightMax = text(self, 3, 1, "e")
        self.heightMax.setText("max(cm)")
        self.heightMax.setWidth(9)
    
    def createWeightSearch(self):
        weightLabel = label(self, 4, 0, "Weight:")
        self.weightMin = text(self, 4, 1, "w")
        self.weightMin.setText("min(lbs)")
        self.weightMin.setWidth(9)
        
        self.weightMax = text(self, 4, 1, "e")
        self.weightMax.setText("max(lbs)")
        self.weightMax.setWidth(9)
        
    def createNationalitySearch(self):
        rawResult = self.cur.execute("SELECT nationality FROM AMBasicInfo GROUP BY nationality").fetchall()
        options = []
        for r in rawResult:
            options.append(r[0])
        self.nationalityMenu = dropMenu(self, 5, 1, options)
        nationalityLabel = label(self, 5, 0, "Nationality:")
    
    def createEmployerSearch(self):
        rawResult = self.cur.execute("SELECT past_employers FROM AMEmployment GROUP BY past_employers").fetchall()
        options = []
        for r in rawResult:
            options.append(r[0])
        self.employerMenu= dropMenu(self, 6, 1, options)
        employerLabel = label(self, 6, 0, "Employer:")
    
    def createRatingSearch(self):
        options = []
        for i in range(0, 6):
            options.append(i)
        self.ratingMenu = dropMenu(self, 7, 1, options)
        employerLabel = label(self, 7, 0, "Avg. Rating:")  
    
    def createSuccessSearch(self):
        successLabel = label(self, 8, 0, "Successes:")
        self.successText = text(self, 8, 1, "w")
        self.successText.setText("min(%)")

    def createMissionSearch(self):
        missionLabel = label(self, 9, 0, "# of Missions:")
        self.missionMin = text(self, 9, 1, "w")
        self.missionMin.setText("min")
        self.missionMin.setWidth(9)
        
        self.missionMax = text(self, 9, 1, "e")
        self.missionMax.setText("max")
        self.missionMax.setWidth(9)    
    
    def createSuccessMissions(self):
        SMissionLabel = label(self, 10, 0, "# of Successes:")
        self.SmissionMin = text(self, 10, 1, "w")
        self.SmissionMin.setText("min")
        self.SmissionMin.setWidth(9)
        
        self.SmissionMax = text(self, 10, 1, "e")
        self.SmissionMax.setText("max")
        self.SmissionMax.setWidth(9)
    
#     def createFailedMissions(self):
#         FMissionLabel = label(self, 11, 0, "# of Failed Missions:")
#         self.FmissionMin = text(self, 11, 1, "w")
#         self.FmissionMin.setText("min")
#         self.FmissionMin.setWidth(9)
#     
#         self.FmissionMax = text(self, 11, 1, "e")
#         self.FmissionMax.setText("max")
#         self.FmissionMax.setWidth(9)      
    
    def getFields(self):
        return{"name" : self.nameText.getText(), 
               "minAge" : self.ageMin.getText(),
               "maxAge" : self.ageMax.getText(),
               "minHeight" : self.heightMin.getText(),
               "maxHeight" : self.heightMax.getText(),
               "minWeight" : self.weightMin.getText(),
               "maxWeight" : self.weightMax.getText(),
               "nationality" : self.nationalityMenu.getText(),
               "employer" : self.employerMenu.getText(),
               "avgRating" : self.ratingMenu.getText(),
               "successes" : self.successText.getText(),
               "minMission" : self.missionMin.getText(),
               "maxMission" : self.missionMax.getText(),
               "SmissionMin" : self.SmissionMin.getText(),
               "SmissionMax" : self.SmissionMax.getText(),
#                "FmissionMin" : self.FmissionMin.getText(),
#                "FmissionMax" : self.FmissionMax.getText()
               }