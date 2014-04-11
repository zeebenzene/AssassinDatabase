import sqlite3
from tkinter import *

class Search():
    added = False
    conn = sqlite3.connect("C:\\Users\\Kit\\workspace\\NewAssassinProject\\src\\startup\\AssassinMingle") #DATA BASE FILE GOES HERE
    cur = conn.cursor()
        
    def checkAdded(self, statement):
        if self.added == False:
            statement = statement + " WHERE "
            self.added = True
        return statement
    
        
    def appendName(self, diction):
        self.statement = self.checkAdded(self.statement)
        if diction['name'] != "name":
            self.statement += " AMBasicInfo.name = \"" + diction["name"]  + "\" AND "
      
    def appendNationality(self, diction):
        self.statement = self.checkAdded(self.statement)
        if diction['nationality'] != "select one":
            print(diction["nationality"])
            self.statement += "AMBasicInfo.nationality = \"" + diction['nationality'] + "\" AND "
   
    def appendEmployer(self, diction):
        self.statement = self.checkAdded(self.statement)
        if diction['employer'] != "select one":
            self.statement += "AMEmployment.past_employers = \"" + diction['employer'] + "\" AND "
   
    def appendAge(self, diction):
        self.statement = self.checkAdded(self.statement)
        if diction['minAge'] != "min":
            self.statement += "AMBasicInfo.age >= " + str(diction['minAge']) + " AND "
        if diction['maxAge'] != "max":
            self.statement += "AMBasicInfo.age <= " + str(diction['maxAge']) + " AND "
        
    def appendWeight(self, diction):
        self.statement = self.checkAdded(self.statement)
        if diction['minWeight'] != "min(lbs)":
            self.statement += "AMBasicInfo.weight >= " +  str(diction['minWeight']) + " AND "
        if diction['maxWeight'] != "max(lbs)":
            self.statement += "AMBasicInfo.weight <= " + str(diction['maxWeight']) + " AND "
        
    def appendHeight(self, diction):
        statement = self.checkAdded(self.statement)
        if diction['minHeight'] != "min(cm)":
            self.statement += "AMBasicInfo.height >= " + str(diction['minHeight']) + " AND "
        if diction['maxHeight'] != "max(cm)":
            self.statement += "AMBasicInfo.height <= " + str(diction['maxHeight']) + " AND "

    def appendNumSuccessful(self, diction):
        self.statement = self.checkAdded(self.statement)
        if diction['SmissionMin'] != "min":
            self.statement += "AMEmployment.num_successful >= " + str(diction['SmissionMin']) + " AND "
        if diction['SmissionMax'] != "max":
            self.statement += "AMEmployment.num_successful <= " + str(diction['SmissionMax']) + " AND "
    
#     def appendNumFailed(self, diction):
#         self.statement = self.checkAdded(self.statement)
#         if diction['FmissionMin'] != "min":
#             self.statement += "AMEmployment.numFailed >= " + diction['FmissionMin'] + " AND "
#         if diction['FmissionMax'] != "max":
#             self.statement += "AMEmployment.numFailed <= " + diction['FmissionMax'] + " AND "
    
    def appendTotalMissions(self, diction):
        self.statement = self.checkAdded(self.statement)
        if diction['minMission'] != "min":
            self.statement += "AMEmployment.num_jobs >= " + str(diction['minMission']) +  " AND "
        if diction['maxMission'] != "max":
            self.statement += "AMEmployment.num_jobs <= " + str(diction['maxMission']) + " AND "    
    
    def appendSuccessRate(self, diction):
        self.statement = self.checkAdded(self.statement)
        if diction['successes'] != "min(%)":
            self.statement += "AMEmployment.average_successes >= " + str(diction["successes"]) + " AND "
    
    def appendAverageReview(self, diction):
        self.statement = self.checkAdded(self.statement)
        if diction['avgRating'] != "select one":
            self.statement += "AMReviews.current_average >=" +  str(diction["avgRating"]) + " AND "
    
    def initializeStatement(self):
        self.statement = "SELECT AMBasicInfo.id FROM AMBasicInfo JOIN AMEmployment ON AMEmployment.id = AMBasicInfo.id "
        self.statement += "JOIN AMFlavor ON AMFlavor.id = AMEmployment.id "
        self.statement += "JOIN AMReviews ON AMReviews.id = AMFlavor.id "
        self.statement += "JOIN AMImages ON AMFlavor.id = AMImages.id"
    
    def finalizeStatement(self, dictionary):
        self.initializeStatement()

        self.appendName(dictionary)
        self.appendAge(dictionary)
        self.appendWeight(dictionary)
        self.appendHeight(dictionary)
        self.appendNationality(dictionary)
        self.appendEmployer(dictionary)
        self.appendTotalMissions(dictionary)
        self.appendNumSuccessful(dictionary)
#         self.appendNumFailed(dictionary)
        self.appendSuccessRate(dictionary)
        self.appendAverageReview(dictionary)
        
        self.statement = self.statement.rstrip(" WHERE ")
        self.statement = self.statement.rstrip(" AND ")
        self.statement += " GROUP BY AMBasicInfo.id"
        
    
    def getQuery(self, dictionary):
        self.finalizeStatement(dictionary)
        return self.statement
    
    def search(self, dictionary):
        
        self.finalizeStatement(dictionary)
        
        rows = self.cur.execute(self.statement).fetchall()
        IDS = []
        for r in rows:
            IDS.append(r[0])
        return IDS

