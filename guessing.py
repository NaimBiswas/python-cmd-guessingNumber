
import random


lowRange = 0
highRange = 100

humanEnteredNumber = int(input("Enter a number to guess:-"))
machineGeneratedNumber = random.randint(lowRange, highRange)
if humanEnteredNumber > 100 or humanEnteredNumber < 0:
    print("Number should be between 0 to 100 only")
elif humanEnteredNumber > machineGeneratedNumber: 
    print("Your Number is to high.", "Guessed Number was", machineGeneratedNumber)
elif humanEnteredNumber < machineGeneratedNumber:
    print("Your Number is to low.", "Guessed Number was", machineGeneratedNumber)
else: print("You have own the game 👌👏👏 \nThank for playing",)