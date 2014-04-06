import sqlite3

MAX_NUM = 99999999



'''
yesIDs = []
noIDs = []
yesNames = []
noNames = []

genderField = None
'''
nameField = ""
nationalityBox = ""
employerBox = ""


ageMin = 0
ageMax = MAX_NUM
weightMin = 0
weightMax = MAX_NUM
heightMin = 0
heightMax = MAX_NUM
killCountMin = 0
killCountMax = MAX_NUM
successMin = 0
failedMax = MAX_NUM
totalMin = 0
successRateMin = 0
ratingsMin = 0
'''
yesNations = []
noNations = []
yesLanguages = []
noLanguages = []
yesWeapons = []
noWeapons = []
yesSupport = []
noSupport = []
yesWeaknesses = []
noWeaknesses = []
yesEmployers = []
noEmployers = []

yesHairColors = []
noHairColors = []
yesEyeColors = []
noEyeColors = []
'''

conn = sqlite3.connect(database)
cur = conn.cursor()

def example():
    root = Tk()
    searchButton = Button(root, text="Search", command=search)
    searchButton.pack()
    root.mainLoop()
    
def appendName(statement):
    if nameField != "":
        statement += "AMBasicInfo.name LIKE '%nameField%' AND"
    return statement

def appendNationality(statement):
    if nationalityBox != "":
        statement += "AMBasicInfo.nationality = nationalityBox AND"
    return statement

def appendEmployer(statement):
    if employerBox != "":
        statement += "AMEmployment.past_employers = employerBox AND"
    return statement

def appendAge(statement):
    if ageMin != 0:
        statement += "AMBasicInfo.age >= ageMin AND"
    if ageMax != MAX_NUM:
        statement += "AMBasicInfo.age <= ageMax AND"
    return statement
    
def appendWeight(statement):
    if weightMin != 0:
        statement += "AMBasicInfo.weight >= weightMin AND"
    if weightMax != MAX_NUM:
        statement += "AMBasicInfo.weight <= weightMax AND"
    return statement  
    
def appendHeight(statement):
    if heightMin != 0:
        statement += "AMBasicInfo.height >= heightMin AND"
    if heightMax != MAX_NUM:
        statement += "AMBasicInfo.height <= heightMax AND"
    return statement
'''
def appendKillCount(statement):
    if killCountMin != 0:
        statement += "AMEmployment.killCount >= killCountMin AND"
    if killCountMax != MAX_NUM:
        statement += "AMEmployment.killCount <= killCountMax AND"
    return statement
'''
def appendNumSuccessful(statement):
    if successMin != 0:
        statement += "AMEmployment.numSuccessful >= successMin AND"
    return statement

def appendNumFailed(statement):
    if failedMax != MAX_NUM:
        statement += "AMEmployment.numFailed <= failedMax AND"
    return statement

def appendTotalMissions(statement):
    if totalMin != 0:
        statement += "AMEmployment.num_jobs >= totalMin AND"
    return statement

def appendSuccessRate(statement):
    if successRateMin != 0:
        statement += "AMEmployment.average_successes >= successRateMin AND"
    return statement

def appendAverageReview(statement):
    if ratingMin != 0:
        statement += "AMReviews.current_average >= ratingMin AND"
    return statement

def appendJoins(statement):
    statement += "AMBasicInfo.id = AMEmployment.id AND"
    statement += "AMBasicInfo.id = AMFlavor.id AND"
    statement += "AMBasicInfo.id = AMReviews.id"
'''
def appendJoins2(statement):
    statement += "JOIN id ON"
    statement += "AMBasicInfo.ID = AMEmployment.ID JOIN id ON"
    statement += "AMBasicInfo.ID = AMFlavor.ID AND"
    statement += "AMBasicInfo.ID = AMReviews.ID"
''' 
def search():
    statement = "SELECT * FROM AMBasicInfo, AMEmployment, AMFlavor, AMReviews WHERE"
    staetment = appendName(statement)
    statement = appendAge(statement)
    statement = appendWeight(statement)
    statement = appendHeight(statement)
    statement = appendNationality(statement)
    statement = appendEmployer(statement)
    #statement = appendKillCount(statement)
    statement = appendTotalMissions(statement)
    statement = appendNumSuccessful(statement)
    statement = appendNumFailed(statement)
    statement = appendSuccessRate(statement)
    statement = appendAverageReview(statement)
    
    statement = appendJoins(statement)

    cur.execute(statement)