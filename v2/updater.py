import revisionLib as rl
AllData = rl.Load('data.json')


for phrase in range(len(AllData)):
    AllData[phrase].pop('stars')
    AllData[phrase]['starsEnglish'] = 0
    AllData[phrase]['starsSpanish'] = 0
    AllData[phrase]['streakEnglish'] = 0
    AllData[phrase]['streakSpanish'] = 0


rl.Save(AllData, 'data.json')