import json
import os
from random import randint
from time import time


importedJson=open('data.json',"r")
AllData=json.loads(importedJson.read())
importedJson.close()

def SaveAllData():
    importedJson=open('data.json',"w")
    importedJson.write(json.dumps(AllData))
    importedJson.close()


def FormatStr(s:str,rs:bool=True,fc:bool=False,aa:bool=True):
    if s=="": #check if string is blank
        return s
    if rs: #Remove Start and End Spaces
        s = s.strip()
    if fc: #Fix Case
        for l in range(len(s)):
            if s[l-1].isalpha():
                s=s[:l].upper()+s[l:].lower()
                break

    if aa: #Add Accents to the letter before
        accented="áéíóúñÁÉÍÓÚÑ¿¡"
        notAccented="aeiounAEIOUN?!"
        for l in range(len(s)):
            l-=1
            if s[l]=="`":
                if s[l-1] in notAccented:
                    s=s[:l-1]+accented[notAccented.find(s[l-1])]+s[l:]
        s=s.replace("`","")
    return s


while True:
    eng = FormatStr(input('What is the English word/phrase?: '))
    spn = FormatStr(input('What is the Spanish word/phrase?: '))
    AllData.append({"english": eng, "spanish": spn, "stars": 0, "lastPracticed": 0})
    SaveAllData()
    print(" Operation Sucessful\n---------------------")