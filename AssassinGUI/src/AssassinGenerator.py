import random
from sets import Set

'''
Attributes:
ID#
primary aliases
age
gender
weight
height
hair color
eye color
race
nationality
weapon proficiencies
support skills
weaknesses
kill count
successful missions
failed missions
aborted missions
total missions
success rate
past employers
languages
num ratings
average ratings


known accomplices
'''

first_names = ["White", "Black", "Red", "Yellow", "Blue", "Green", "Purple", "Orange", "Dark", "Light", "Noble", "Devious", "Fluffy", "Hell", "Silent", "Heavy", "Short", "Big", "Little", "Death", "Smelly", "Four-Finger", "One-Eye", "Oedipus", "Adamant", "Adroit", "Baleful", "Slow", "Hot", "Contemptuous", "Angry", "Loud", "Mean" ]
last_names = ["Mamba", "Snake", "Bear", "Leopard", "Tiger", "Eel", "Viper", "Goldfish", "Pixie", "Wolf", "Huskie", "Barber", "Chef", "Agent", "Mistress", "Stranger", "Loner", "Eagle", "Vulture", "Raven", "Angel", "Sally", "Bertha", "Papa", "Mama", "Kristi", "Swordfish", "Tuna", "Gator", "Tony", "Sister", "Vegan"]

hair_color = ["brown", "black", "blond", "red", "gray"]
eye_color = ["brown", "blue", "green", "hazel"]

race = ["caucasian", "black", "latino", "asian", "middle eastern", "pacific islander"]
nationality = ["American", "Russian", "Chinese", "Japanese", "Korean", "British", "Italian", "Saudi", "Dutch", "Mexican", "Cuban", "Brazilian", "Rwandan", "Israeli", "Moroccan", "Libyan"]
languages = ["English", "Spanish", "French", "German", "Polish", "Russian", "Japanese", "Chinese", "Thai", "Arabic", "Libyan"]

weapon_skills = ["knives", "swords", "guns", "staves", "explosives", "poisons", "hand-to-hand", "whip", "archery", "spears", "axes"]
support_skills = ["computer", "lock picking", "disguise", "mechinical", "hair dressing", "scuba", "piloting", "acrobat", "cryptography", "dancing", "singing", "knot tying", "con man"]
weaknesses = ["peanut allergy", "asthma", "mommy issues", "daddy issues", "fibromyalgia", "Tourettes", "crippling phobias", "total paralysis", "partial paralysis", "insanity", "PTSD", "alcoholism", "drug addiction", "restless leg syndrome", "prone to monologuing", "mute", "deaf", "near sighted", "far sighted", "short sighted", "ADHD", "antisocial"]

past_employers = ["Italian Mafia", "New York Mafia", "Yakuza", "Tijuana Cartel", "D-Company", "KGB", "CIA", "MI6"]

takenIDs = Set([])

def getNewID():
    idNum = random.randint(10000000, 99999999)
    if idNum in takenIDs:
        return getNewID()
    else:
        takenIDs.add(idNum)
        return idNum

def getAlias():
    return "'" + random.choice(first_names) + " " + random.choice(last_names) + "'"

def getAge():
    return str(random.randint(13, 107))

def getGender():
    return "'" + random.choice(["M", "F"]) + "'"

def getHeight():
    return str(random.randint(142, 206))

def getWeight():
    return str(random.randint(75, 400))

def getHairColor():
    return "'" + random.choice(hair_color) + "'"

def getEyeColor():
    return "'" + random.choice(eye_color) + "'"

def getNationality():
    return "'" + random.choice(nationality) + "'"

def getLanguage():
    return "'" + random.choice(languages) + "'"

def getPastEmployer():
    return "'" + random.choice(past_employers) + "'"

def getJobStats():
    numJobsTaken = random.randint(0, 999)
    numSuccessful = random.randint(0, numJobsTaken)
    
    if numJobsTaken == 0:
        successRate = -1
    else:
        successRate = numSuccessful*100/numJobsTaken
    
    jobStats = str(numJobsTaken) + ',' + str(numSuccessful) + ',' + str(successRate)
    return jobStats

def getWeapon():
    return "'" + random.choice(weapon_skills) + "'"

def getSupport():
    return "'" + random.choice(support_skills) + "'"

def getWeakness():
    return "'" + random.choice(weaknesses) + "'"

def getAverageRating():
    return random.randint(0, 50) / 10

def getNumReviews():
    return random.randint(0, 200)

def getBasicInfo():
    basicInfo = ""
    basicInfo += getAlias() + ','
    basicInfo += getAge() + ','
    basicInfo += getGender() + ','
    basicInfo += getHeight() + ','
    basicInfo += getWeight() + ','
    basicInfo += getHairColor() + ','
    basicInfo += getEyeColor() + ','
    basicInfo += getNationality() + ','
    basicInfo += getLanguage()
    return basicInfo

#past employers, # of Jobs, # of successful Jobs, average # of successes
def getWorkHistory():
    workHistory = ""
    workHistory += getPastEmployer() + ','
    workHistory += getJobStats()
    return workHistory

#Weapon of Choice, Support Specialty, Crippling Flaw
def getSkills():
    skillsInfo = ""
    skillsInfo += getWeapon() + ','
    skillsInfo += getSupport() + ','
    skillsInfo += getWeakness()
    return skillsInfo

def getReviews():
    numReviews = getNumReviews()
    reviewInfo = str(numReviews) + ','
    if (numReviews == 0):
        reviewInfo += str(-1)
    else:
        reviewInfo += str(getAverageRating())
    return reviewInfo
    
def writeBasicInfo(idNum, curFile):
    newEntry = idNum + ','
    newEntry += getBasicInfo()
    newEntry += "\n"
    curFile.write(newEntry)
    
def writeEmployment(idNum, curFile):
    newEntry = idNum + ','
    newEntry += getWorkHistory()
    newEntry += "\n"
    curFile.write(newEntry)
    
def writeFlavor(idNum, curFile):
    newEntry = idNum + ','
    newEntry += getSkills()
    newEntry += "\n"
    curFile.write(newEntry)
    
def writeReviews(idNum, curFile):
    newEntry = idNum + ','
    newEntry += getReviews()
    newEntry += "\n"
    curFile.write(newEntry)
    
def addNewAssassin(basicFile, employFile, flavorFile, reviewsFile):
    idNum = str(getNewID())
    writeBasicInfo(idNum, basicFile)
    writeEmployment(idNum, employFile)
    writeFlavor(idNum, flavorFile)
    writeReviews(idNum, reviewsFile)
    
def createAssassins(numAssassins):
    basicFile = open("AMBasicInfo.csv", 'w')
    employFile = open("AMEmployment.csv", 'w')
    flavorFile = open("AMFlavor.csv", 'w')
    reviewsFile = open("AMReviews.csv", 'w')
    
    for i in range(numAssassins):
        addNewAssassin(basicFile, employFile, flavorFile, reviewsFile)
        
    basicFile.close()
    employFile.close()
    flavorFile.close()
    reviewsFile.close()
    
createAssassins(500)
    
'''
BASIC_INFO( ID#, name, age, gender, height, weight, nationality, languages)
EMPLOYMENT_HISTORY( ID#, past employers, # of Jobs, # of successful Jobs, average # of successes)
FLAVOR( ID#, Weapon of Choice, Support Specialty, Crippling Flaw)
REVIEWS( ID#, current average rating, # of people who rated)
IMAGE_TABLE( ID#, Image blob)
'''