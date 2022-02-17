import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return '1- It is certain'
    elif answerNumber == 2:
        return '2- It is decidedly so'
    elif answerNumber == 3:
        return '3- Yes'
    elif answerNumber == 4:
        return '4- Reply hazy try again'
    elif answerNumber == 5:
        return '5- Ask again later'
    elif answerNumber == 6:
        return '6- Concentrate and ask again'
    elif answerNumber == 7:
        return '7- My reply is no'
    elif answerNumber == 8:
        return '8- Outlook not so good'
    elif answerNumber == 9:
        return '9- Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)