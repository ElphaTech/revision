import json
import os
import time
import random


importedJson=open('data.json',"r")
AllData=json.loads(importedJson.read())
importedJson.close()

def SaveAllData():
    importedJson=open('data.json',"w")
    importedJson.write(json.dumps(AllData))
    importedJson.close()


def FormatStr(s:str,rs:bool=True,fc:bool=True,aa:bool=True):
    if s=="": #check if string is blank
        return s
    if rs: #Remove Start and End Spaces
        s = s.strip()
    if fc: #Fix Case
        for l in range(len(s)):
            if s[l-1].isalpha():
                s=s[:l].upper()+s[l:].lower()
                break

    if aa: #Add Accents
        accented="áéíóúñÁÉÍÓÚÑ¿¡"
        notAccented="aeiounAEIOUN?!"
        for l in range(len(s)):
            l-=1
            if s[l]=="`":
                if s[l-1] in notAccented:
                    s=s[:l-1]+accented[notAccented.find(s[l-1])]+s[l:]
        s=s.replace("`","")
    return s

#Choose translation direction
if input(f'What language do you want to translate TO?: ').lower() == 'english':
    langFrom = 'spanish'
    langTo = 'english'
else:
    langFrom = 'english'
    langTo = 'spanish'

#main "game" loop
while True:
    phraseIndex = random.randint(0,len(AllData)-1)
    phraseData = AllData[phraseIndex]
    answer = input(f'\nWhat does the following text translate to in {langTo}:\n-> {phraseData[langFrom]}\n-> ')
    if answer.strip() == phraseData[langTo]:
        correct = 'y'
    else:
        correct = input(f'Are you correct(y/n): \n-> Provided Answer: {phraseData[langTo]}\n->     Your Answer: {answer}\n-> ')
    
    if correct.strip() == 'y' or correct.strip() == '':
        AllData[phraseIndex]['stars'] += 1

    AllData[phraseIndex]['lastPracticed'] = int(time.time())
    SaveAllData()

    