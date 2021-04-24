# Write a program that generates a random number in the range from 1 through 100
# 20210421
# CTI - 110 P5HW1 - Random Number
# Rheanna Howell
#

# This program plays a number guessing game with the user.
# If the user's guess is to high it will display too high
# If the user's guess is to low it will display too low, try again
# If the user is correct it will display congratulations you won
# Game will start over with correct guess

#Pseudocode:
#import random so you can get random numbers
import random
#create random number function
def Create_Random_Number():
    randomNumber = random.randint(1,100) #Creates a random number between 1 - 100
    return randomNumber

#Create function to ask user their number
def Ask_User_Number(message="Enter a number 1-100: "): #Ask user to place a guessed number
    userNumber = int(input(message))
    return userNumber

#Function to check if user's number is too high, too low, or correct
def Check_User_Number(userNumber, randomNumber):
    if userNumber > randomNumber:
        return 'Too High, Try again'
    elif userNumber < randomNumber:
        return 'Too Low, Try again'
    else:
        return 'Congratulations! You Win!'

#Main function for game
def main():
    userCongratulated = False
    start = True
    print("""
        Main Menu
        ---------------
        1. Play Game
        2. Exit
        """) #Create a menu for the user to select
    choice = input("Pick an option fromt the menu: ")
    if choice == "1":  #starts game
        numberOfGuesses = 0  #Optional to place the amount of guesses user made
        print("Let's play a guessing game.")
        print("I am thinking of a number between 1 - 100.")
        print("Try and guess the number and I will give you hints along the way.")
        randomNumber = Create_Random_Number()
        while userCongratulated or start:
            userNumber = Ask_User_Number()
            numberOfGuesses = numberOfGuesses + 1
            message = Check_User_Number(userNumber, randomNumber)     
            if message != 'Congratulations! You Win!':
                print(message)
            else:
                print(message)
                print("You guessed the number in", numberOfGuesses, "attempts.")
                #Display would you like to play again
                play_choice = input("Would you like to play again? (y/n): ")
                if play_choice.lower() == 'y':
                    userCongratulated = True
                    main()#call menu after you've guessed correctly
                else:
                    exit()
    if choice =="2":
        exit()

if __name__ == '__main__':
    main()
