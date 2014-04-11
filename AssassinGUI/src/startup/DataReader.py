import sqlite3
from os import listdir
from random import choice

def load_data(cur, file):
    with open(file) as f:
        content = f.readlines()
    
    for line in content:
        data = line.split(",")
        statement = "INSERT INTO "+file+" VALUES ("
        for entry in data:
            statement = statement+entry+", "
        statement = statement.rstrip("\n, ")+")"
        try:
            cur.execute(statement)
        except:
            print("Could not execute statement "+statement)
            
def load_images(cur, file):
    with open(file) as f:
        content = f.readlines()
    
    for line in content:
        data = line.split(",")
        idNum = data[0]
        photo = data[1]
        if photo == "\'none\'\n":
            photo = "\'"+choice(listdir("random"))+"\'"
        statement = "INSERT INTO "+file+" VALUES ("+idNum+", "+photo+")"
        try:
            cur.execute(statement)
        except:
            print("Could not execute statement "+statement)
        
def create_table(c, f):
    if f == files[0]:
        statement = "CREATE TABLE "+f+" (id INTEGER, name TEXT, age INTEGER, gender TEXT, height INTEGER, weight INTEGER, hair_color TEXT, eye_color TEXT, nationality TEXT, language TEXT)"
        c.execute(statement)
        load_data(c, f)
    
    elif f == files[1]:
        statement = "CREATE TABLE "+f+" (id INTEGER, past_employers TEXT, num_jobs INTEGER, num_successful INTEGER, average_successes INTEGER)"
        c.execute(statement)
        load_data(c, f)
    
    elif f == files[2]:
        statement = "CREATE TABLE "+f+" (id INTEGER, weapon_choice TEXT, support_specialty TEXT, crippling_flaw TEXT)"
        c.execute(statement)
        load_data(c, f)
    
    elif f == files[3]:
        statement = "CREATE TABLE "+f+" (id INTEGER, num_ratings INTEGER, current_average INTEGER)"
        c.execute(statement)
        load_data(c, f)
    
    elif f == files[4]:
        statement = "CREATE TABLE "+f+" (id INTEGER, image BLOB)"
        c.execute(statement)
        load_images(c, f)

conn = sqlite3.connect("AssassinMingle")
cur = conn.cursor()
files = "AMBasicInfo", "AMEmployment", "AMFlavor", "AMReviews", "AMImages"
for file in files:
    statement = "SELECT * FROM "+file
    try:
        if not cur.execute(statement):
            print("Populating "+file)
            load_data(cur, file)
    except:
        print("Creating "+file)
        create_table(cur, file)
    
while True:
    statement = input("sqlite> ")
    if statement:
        try:
            result = cur.execute(statement)
            for row in result:
                print(row)
        except:
            print("Could not execute statement "+statement)
    else:
        conn.commit()
        cur.close()
        conn.close()
        break

#DROP TABLE AMBasicInfo
#DROP TABLE AMFlavor
#DROP TABLE AMEmployment
#DROP TABLE AMReviews
#DROP TABLE AMImages

#SELECT * FROM AMBasicInfo
#SELECT * FROM AMFlavor
#SELECT * FROM AMEmployment
#SELECT * FROM AMReviews
#SELECT * FROM AMImages