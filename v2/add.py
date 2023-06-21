import revisionLib as rl
AllData = rl.Load('data.json')


while True:
    eng = rl.FormatStr(input('What is the English word/phrase?: '))
    spn = rl.FormatStr(input('What is the Spanish word/phrase?: '))
    AllData.append({"english": eng, "spanish": spn, "starsEnglish": 0, "starsSpanish": 0, "streakEnglish": 0, "streakSpanish": 0, "lastPracticed": 0})
    rl.Save(AllData, 'data.json')
    print(" Operation Sucessful\n---------------------")