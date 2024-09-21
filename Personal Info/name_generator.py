# -*- coding: utf-8 -*-
"""
Author: Connor Ebert
Date: 9/3/24
Missing misc info and personal address
"""

import pandas as pd
import random
from tqdm import tqdm
import string

#Gets name and reads the file to df
#nameList converts to a list to manipulate
file_name = "test_names_raw.xlsx"
sag_file = "Database-Fields-n-Tables-Recommended.xlsx"




#Gloabal Variables
#Creates dataframe and gets info to store in global variable
df = pd.read_excel(file_name, sheet_name="Sheet2")
nameList = df.values.tolist()


#lists used
first_name_list = []
last_name_list = []


#Gets a random gender
def randGender():
    gender = ["male", "female", "other"]
    return gender[random.randint(0,2)]

#returns if they have a spouse or not or nothing
def randSpouse():
    spouse = ["Yes", "No", ""]
    return spouse[random.randint(0, 2)]


#generates random birthday
def randBday():
    month = random.randint(1, 12)
    if(month == 2):
        day = random.randint(0, 28)
    elif(month == 4 or month == 6 or month == 9 or month == 11):
        day = random.randint(0, 30)
    else:
        day = random.randint(0,31)
    year = random.randint(1941, 2002)
    birthday = str(month) + "/" + str(day) + "/" + str(year)
    return birthday


    

#Creates personal data table in xlsx
def createPersonalData(pk):
    export = []
    for i in tqdm(range(300000)):
        #lists used to store data
        info = []
        split_name = []
        #goes through and splits the data
        for item in nameList:
            split_name.append(item[0].split())
        #after data is split, make sure last name is not null
        x = 0
        while x < len(split_name):
            #if no last name, last name becomes first name
            if(len(split_name[x]) == 1):
                first_name_list.append(split_name[x])
                last_name_list.append(split_name[x])
            #if more than one word for last name, add it to last name
            else:
                first_name_list.append(split_name[x][0])
                last_name_list.append(split_name[x][1:])
            x += 1
        #Random int for first name and last name
        randName = random.randint(0, 2328)
        #format first and last name seperately
        formatFirstName = str(first_name_list[randName]).replace("'","").replace("[","").replace("]","")
        formatLastName = str(last_name_list[randName]).replace("'","").replace("[","").replace("]","")
        #random primary key
        info.append(pk)
        #random first name
        info.append(str(formatFirstName))
        #random letter for middle name
        info.append(str(random.choice(string.ascii_letters)))
        #random last name
        info.append(str(formatLastName)) 
        #random gender
        info.append(str(randGender()))
        #random birthday
        info.append(str(randBday()))
        #random spouse
        info.append(str(randSpouse()))
        pk += 1
        export.append(info)
    print("\nExporting to XLSX...")
    print("Takes a bit so be patient")
    peronal_data = pd.DataFrame(export)
    peronal_data.to_excel("personal_info.xlsx")

createPersonalData(93547)

