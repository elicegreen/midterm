# This is a very simple game of sticks. There are 21 sticks, first the user picks number of sticks between 1-4, then the computer picks sticks(1-4).
# Who ever will pick the last stick will lose.

import random
sticks = 21




#Main game function

def playGame():
    print('There are 21 sticks. You can pick from 1 to 4 sticks at a time, and the computer will then pick from 1 to 4 sticks at a time. Whoever picks the last stick loses!')
    while True:
        print('Current sticks: ' + str(sticks))
        userChoice = askUserChoice()
        if subtractSticks( userChoice ):
            print('You lost!')
            break
        
        computerChoice = determineComputerChoice()
        print('Computer picked: ' + str(computerChoice) )
        if subtractSticks( computerChoice ):
            print('Computer lost!')
            break




        
# This functiont asks the user to enter their input (between 1 and 4) and return that input as an integer
# If the user's input is not valid (if it's not between 1 and 4), the user is asked to re-enter their input until enters valid input.
    
def askUserChoice():
    validInput = ['1', '2', '3', '4']
    print('Please enter a number between 1 and 4')
    userNum = input()
    while True:
        if userNum not in validInput:
            print('Your selection is invalid. Please enter a number between 1 and 4')
            userNum = input()
        else:
            return int(userNum)

                  



# This function subtracts the parameter `number` from the global variable `sticks`
# If the number subtracted resulted in the last stick, it returns True
# If there are still sticks left, it returns False

def subtractSticks( number ):
    global sticks
    sticks = sticks - number
    if sticks <= 0:
        return True
    else:
        return False




    
# This function returns an integer between 1 and 4, randomly chosen by the computer
    
def determineComputerChoice():
        return random.randint(1,4)

