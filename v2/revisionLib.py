
# JSON functions
import json

def Load(fileName, mode='r'):
    importedJson = open(fileName, mode)
    return json.loads(importedJson.read())
    importedJson.close()

def Save(data, fileName, mode='w'):
    importedJson=open(fileName, mode)
    importedJson.write(json.dumps(data))
    importedJson.close()


# String formating
def FormatStr(s:str,rs:bool=True,fc:bool=False,aa:bool=True):
    if s=="": #check if string is blank
        return s

    if rs: #Remove Start and End Spaces
        s = s.strip()
        
    if fc: #Fix Case
        s = s.capitalize()

    if aa: #Add Accents to the letter before
        accented = "áéíóúñÁÉÍÓÚÑ¿¡"
        notAccented = "aeiounAEIOUN?!"
        for letNo in range(len(notAccented)):
            s = s.replace(f'{notAccented[letNo]}`', f'{accented[letNo]}')

    return s