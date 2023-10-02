import random

score = 0
slot1=["♥", "♠", "♦", "♣"]

def playJackPot():
    global score
    global slot1
    

    slotOne = slot1[random.randint(0, len(slot1)-1)]
    slotTwo = slot1[random.randint(0, len(slot1)-1)]
    slotThree = slot1[random.randint(0, len(slot1)-1)]
    
    if (slotOne==slotTwo) and (slotTwo==slotThree):
        print(f''' {slotOne} {slotTwo} {slotThree}  You Win!''')
        score += 1
        continuePlay = input("Do you wanna play again? (y/n): ")
        if continuePlay == 'y':
            playJackPot()
        else:
            endGame(score)
    else:
        print(f''' {slotOne}  {slotTwo} {slotThree} You lose!''')
        print(score)
        continuePlay = input("Do you wanna play again? (y/n): ")
        #print(score)
        if continuePlay == 'y':
            playJackPot()
        else:
            endGame(score)

def endGame(score):
    print(f'''Thank you for playing, you got {score} points!''')

playJackPot()
