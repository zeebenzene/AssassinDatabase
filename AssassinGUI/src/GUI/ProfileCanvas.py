import tkinter as tk
import PIL.ImageTk as im
import PIL
import os
import sqlite3
from tkinter import *
from components.SearchButton import button
from components.TextLabel import label
from components.TextBox import text 
from components.DropDownMenu import dropMenu
from components.DisplayButton import button as dButton


class profileCanvas(tk.Canvas):
    conn = sqlite3.connect("C:\\Users\\Kit\\workspace\\NewAssassinProject\\src\\startup\\AssassinMingle") #DATA BASE FILE GOES HERE
    cur = conn.cursor()    
    
    def __init__(self, master):
        tk.Canvas.__init__(self, master, bg="black")
        Grid.rowconfigure(master,0,weight=1)
        Grid.columnconfigure(master,1,weight=1)
        self.grid(row=0, column=1, sticky=("w","e","n","s"))
        self.openImage("chef.png")
        self.createResultOptions()
        self.createDisplayButton()
    
    def createBasicInfoHeader(self):
        basicHeader = label(self, 1, 0, "Basic Information:")
        basicHeader.setSize(20)
        basicHeader.setSpan("column", 1)
    
    def createEmploymentHeader(self):
        employmentHeader = label(self, 1, 1, "Employment:")
        employmentHeader.setSize(20)
        employmentHeader.setSpan("column", 1)
    
    def createFlavorHeader(self):
        flavorHeader = label(self, 1, 2, "Flavor:")
        flavorHeader.setSize(20)
        flavorHeader.setSpan("column", "1")
        
    
    def updateBasicInfo(self):
        self.createBasicInfoHeader()
        self.createNameLabel()
        self.createAgeLabel()
        self.createGenderLabel()
        self.createHeightLabel()
        self.createWeightLabel()
        self.createHairLabel()
        self.createEyeLabel()
        self.createNationalityLabel()
        self.createLanguageLabel()
    def createNameLabel(self):
        row = self.cur.execute("SELECT name FROM AMBasicInfo WHERE name = \"" + self.resultOptions.getText() + "\"")
        name = row.fetchone()[0]
        self.nameLabel = label(self, 2, 0, "Name: " + name)
        self.nameLabel.setSpan("column", 1)
    def createAgeLabel(self):
        row = self.cur.execute("SELECT age FROM AMBasicInfo WHERE name = \"" + self.resultOptions.getText() + "\"")
        age = row.fetchone()[0]
        self.ageLabel = label(self, 3, 0, "Age: " + str(age))
        self.ageLabel.setSpan("column", 1)
    def createGenderLabel(self):
        row = self.cur.execute("SELECT gender FROM AMBasicInfo WHERE name = \"" + self.resultOptions.getText() + "\"")
        gender = row.fetchone()[0]
        self.genderLabel = label(self, 4, 0, "Gender: " + gender)
        self.genderLabel.setSpan("column", 1)
    def createHeightLabel(self):
        row = self.cur.execute("SELECT height FROM AMBasicInfo WHERE name = \"" + self.resultOptions.getText() + "\"")
        height = row.fetchone()[0]
        self.heightLabel = label(self, 5, 0, "Height: " + str(height) + "cm")
        self.heightLabel.setSpan("column", 1)     
    def createWeightLabel(self):
        row = self.cur.execute("SELECT weight FROM AMBasicInfo WHERE name = \"" + self.resultOptions.getText() + "\"")
        weight = row.fetchone()[0]
        self.weightLabel = label(self, 6, 0, "Weight: " + str(weight) + "lbs")
        self.weightLabel.setSpan("column", 1)         
    def createHairLabel(self):
        row = self.cur.execute("SELECT hair_color FROM AMBasicInfo WHERE name = \"" + self.resultOptions.getText() + "\"")
        hair = row.fetchone()[0]
        self.hairLabel = label(self, 7, 0, "Hair Colour: " + hair)
        self.hairLabel.setSpan("column", 1)
    def createEyeLabel(self):
        row = self.cur.execute("SELECT eye_color FROM AMBasicInfo WHERE name = \"" + self.resultOptions.getText() + "\"")
        eye = row.fetchone()[0]
        self.eyeLabel = label(self, 8, 0, "Eye Colour: " + eye)
        self.eyeLabel.setSpan("column", 1)
    def createNationalityLabel(self):
        row = self.cur.execute("SELECT nationality FROM AMBasicInfo WHERE name = \"" + self.resultOptions.getText() + "\"")
        nationality = row.fetchone()[0]
        self.nationalityLabel = label(self, 9, 0, "Nationality: " + nationality)
        self.nationalityLabel.setSpan("column", 1)
    def createLanguageLabel(self):
        row = self.cur.execute("SELECT language FROM AMBasicInfo WHERE name = \"" + self.resultOptions.getText() + "\"")
        language = row.fetchone()[0]
        self.languageLabel = label(self, 10, 0, "Language: " + language)
        self.languageLabel.setSpan("column", 1)
        
    
    
    def updateEmployers(self):
        self.createEmploymentHeader()
        self.createPastEmployers()
        self.createNumJobs()
        self.createSuccessfulJobs()
        self.createAverageSuccesses()
    def createPastEmployers(self):
        row = self.cur.execute("SELECT past_employers FROM AMEmployment JOIN AMBasicInfo ON AMEmployment.id = AMBasicInfo.id WHERE name = \"" + self.resultOptions.getText() + "\"")
        employer = row.fetchone()[0]
        self.employerLabel = label(self, 2, 1, "Previous Employer: " + employer)
        self.employerLabel.setSpan("column", 1)
    def createNumJobs(self):
        row = self.cur.execute("SELECT num_jobs FROM AMEmployment JOIN AMBasicInfo ON AMEmployment.id = AMBasicInfo.id WHERE name = \"" + self.resultOptions.getText() + "\"")
        jobs = row.fetchone()[0]
        self.numJobsLabel = label(self, 3, 1, "# of Total Jobs: " + str(jobs))
        self.numJobsLabel.setSpan("column", 1)
    def createSuccessfulJobs(self):
        row = self.cur.execute("SELECT num_successful FROM AMEmployment JOIN AMBasicInfo ON AMEmployment.id = AMBasicInfo.id WHERE name = \"" + self.resultOptions.getText() + "\"")
        jobs = row.fetchone()[0]
        self.SjobsLabel = label(self, 4, 1, "# of Successful Jobs: " + str(jobs))
        self.SjobsLabel.setSpan("column", 1)
    def createAverageSuccesses(self):
        row = self.cur.execute("SELECT average_successes FROM AMEmployment JOIN AMBasicInfo ON AMEmployment.id = AMBasicInfo.id WHERE name = \"" + self.resultOptions.getText() + "\"")
        jobs = row.fetchone()[0]
        self.AjobsLabel = label(self, 5, 1, "Average Successes: " + str(jobs) + "%")
        self.AjobsLabel.setSpan("column", 1)
        
    
    def updateFlavor(self):
        self.createFlavorHeader()
        self.createWeaponChoice()
        self.createSupportSpecialty()
        self.createFlaw()
    def createWeaponChoice(self):
        row = self.cur.execute("SELECT weapon_choice FROM AMFlavor JOIN AMBasicInfo on AMFlavor.id = AMBasicInfo.id WHERE name = \"" + self.resultOptions.getText() + "\"")
        weapon = row.fetchone()[0]
        self.weaponLabel = label(self, 2, 2, "Weapon of Choice: " + weapon)
        self.weaponLabel.setSpan("column", 1)
    def createSupportSpecialty(self):
        row = self.cur.execute("SELECT support_specialty FROM AMFlavor JOIN AMBasicInfo on AMFlavor.id = AMBasicInfo.id WHERE name = \"" + self.resultOptions.getText() + "\"")
        specialty = row.fetchone()[0]
        self.specialtyLabel = label(self, 3, 2, "Support Specialty: " + specialty)
        self.specialtyLabel.setSpan("column", 1)
    def createFlaw(self):
        row = self.cur.execute("SELECT crippling_flaw FROM AMFlavor JOIN AMBasicInfo on AMFlavor.id = AMBasicInfo.id WHERE name = \"" + self.resultOptions.getText() + "\"")
        flaw = row.fetchone()[0]
        self.flawLabel = label(self, 4, 2, "Fatal Flaw: " + flaw)
        self.flawLabel.setSpan("column", 1)        
    
    def openImage(self, imageName):
        path = os.path.dirname(__file__) + "\\photos\\" + imageName
        photo = im.PhotoImage(PIL.Image.open(path))
        
        label = tk.Label(self,image=photo)
        label.image = photo
        label.grid(row=0, column=0)
    
    def createResultOptions(self):
        self.resultOptions = dropMenu(self, 0, 1, ["no results"])
        self.resultOptions.setSpan("column", 2)
#         self.resultOptions.grid(row=0, column=1, sticky="ne")
    
    def createDisplayButton(self):
        self.displayButton = dButton(self, 0, 1, self)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def setResultOptions(self, choices):
        names = []
        for c in choices:
            row = self.cur.execute("SELECT name FROM AMBasicInfo WHERE id = " + str(c))
            name = row.fetchone()[0]
            names.append(name)
        self.resultOptions.setChoices(names)
    
    def update(self):
        row = self.cur.execute("SELECT image FROM AMImages JOIN AMBasicInfo ON AMBasicInfo.id = AMImages.id WHERE AMBasicInfo.name = \"" + self.resultOptions.getText() + "\"")
        imageName = row.fetchone()[0]
        self.openImage(imageName)
        self.updateBasicInfo()
        self.updateEmployers()
        self.updateFlavor()

