# python-cmd-guessingNumber BY <h1>Naim Biswas</h1>

import random </br>


lowRange = 0 </br>
highRange = 100 </br>

def guessNumberFun (): </br>
    machineGeneratedNumber = random.randint(lowRange, highRange) </br>
    humanEnteredNumber = int(input("Enter a number to guess:-")) </br>
    if humanEnteredNumber > 100 or humanEnteredNumber < 0: </br>
        print("Number should be between 0 to 100 only") </br>
        return False </br>
    elif humanEnteredNumber > machineGeneratedNumber:  </br>
        print("Your Number is to high.", "Guessed Number was", machineGeneratedNumber) </br>
        return False </br>
    elif humanEnteredNumber < machineGeneratedNumber: </br>
        print("Your Number is to low.", "Guessed Number was", machineGeneratedNumber) </br>
        return False </br>
    else: print("You have own the game 👌👏👏 \nThank for playing"); return True </br>
 </br>
while(guessNumberFun() != True): </br>
    guessNumberFun() </br>
 </br>
