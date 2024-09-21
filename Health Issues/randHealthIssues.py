# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:35:56 2024

@author: connr
"""

import pandas as pd
import random
from tqdm import tqdm
import time
import os

sag_file = "Database-Fields-n-Tables-Recommended.xlsx"

export = []
#opens va claim sheet
va_claim_sheet = pd.read_excel(sag_file, sheet_name="VA_Claim")
va_claim = va_claim_sheet.values.tolist()

def randHealthIssue(pk):
    #opesn health issues sheet
    health_issues_sheet = pd.read_excel(sag_file, sheet_name="Health_Issues")
    health_issues = health_issues_sheet.values.tolist()
    
    for x in range(1):
        print("Starting process: " + str(x))
        for i in tqdm(range(500)):
            #lists used to store random data
            info = []
            #random primary key
            info.append(pk)
            #add claim status
            info.append(va_claim[random.randint(0, len(va_claim) - 1)])
            
            twoOptions = ["yes", "no"]
            #va diability y/n
            info.append(twoOptions[random.randint(0, 1)])
            #p1.start()
            #p1.join()
            pk += 1
            #opesn health issues sheet
            health_issues_sheet = pd.read_excel(sag_file, sheet_name="Health_Issues")
            health_issues = health_issues_sheet.values.tolist()
            rand_health_issue = random.randint(0, 72)
            #random health issue
            info.append(str(health_issues[rand_health_issue][0]))
            info.append(str(health_issues[rand_health_issue][1]))
            info.append(str(health_issues[rand_health_issue][2]))
            export.append(info)
        #os.system('cls' if os.name == 'nt' else 'clear')

    print("Exporting to XLSX...")
    print("Takes a bit so be patient")
    #send data to xlsx
    health_issues = pd.DataFrame(export)
    health_issues.to_excel("heath_issues_hipaa.xlsx")
start_time = time.time()
randHealthIssue(93547)
print("--- %s seconds ---" % (time.time() - start_time)) 
