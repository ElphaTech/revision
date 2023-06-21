import time
import random

import revisionLib as rl
AllData = rl.Load('data.json')

# Choose translation direction
if input(f'What language do you want to translate TO?: ').lower() == 'english':
    langFrom = 'spanish'
    langTo = 'english'
else:
    langFrom = 'english'
    langTo = 'spanish'


# Main "game" loop
lastPracticedWeight = 0.3
correctTimesWeight = 0.2
streakWeight = 0.5

while True:
    # Choose phrase to practice
    # Calculate best choice
    choices = []
    for choiceNo in range(len(AllData)):
        daysLastPracticed = (time.time()-AllData[choiceNo]['lastPracticed']) / (60*60*24)
        # Time(Broken): (10/daysLastPracticed * lastPracticedWeight) + 
        choices.append(((100/(AllData[choiceNo][f'stars{langTo.capitalize()}']+0.01) * correctTimesWeight) + (100/(AllData[choiceNo][f'streak{langTo.capitalize()}']+1.01) * streakWeight))/3)
        print(AllData[choiceNo]['english'],':',choices[-1])

    phraseIndex = choices.index(max(choices))
    phraseData = AllData[phraseIndex]

    # Ask q&a
    answer = input(f'\nWhat does the following text translate to in {langTo}:\n-> {phraseData[langFrom]}\n-> ')

    # Check answer
    if answer.strip().lower() == phraseData[langTo].lower():
        correct = 'y'
        print('You are correct!')
    else:
        correct = input(f'Are you correct(y/n): \n-> Provided Answer: {phraseData[langTo]}\n->     Your Answer: {answer}\n-> ')
    
    if correct.strip() == 'y' or correct.strip() == '':
        AllData[phraseIndex][f'stars{langTo.capitalize()}'] += 1

    AllData[phraseIndex]['lastPracticed'] = int(time.time())
    rl.Save(AllData, 'data.json')