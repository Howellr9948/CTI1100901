# Brief Description
# 20210424
# CTI-110 P5HW2 - Math Quiz
# Rheanna Howell
#

#The program is menu driven
#the program should generate random numbers.
#option 1: add random numbers and guess what they add into
#option 2: subtract random numbers but ask to enter the remainder of the subtraction
#program terminates after option 3 is entered

#Pseudocode:
#import random
import random

#create random number function
def Create_Random_Number():
 randomNumber = random.randint(1, 1000)
 return randomNumber

#Create function to ask user for their answers
def Ask_User_Number(message="Enter your answer: "):
 answer = int(input(message))
 return answer
 
#def main menu for game
def main():
 userCongratulated = False
 start = True
 print("""
   Main Menu
   ---------------
   1. Add Random Number
   2. Subtract Random Number
   3. Exit
   """)
 choice = int(input("Pick an option from the Menu: "))
 if choice == 1: #starts game for addition option
   print("Let's play an addition game.")
   a = Create_Random_Number()
   b = Create_Random_Number()
   right = a + b
   print("What does ", a, " + ", b, "equal?")
   while userCongratulated or start: #Call menu regardless of answer
     answer = Ask_User_Number()
     if answer == right:
       print("Congratulations, the answer is correct!")
       main()
     else:
       print("That is incorrect, the answer is ", right)
       main()
   
 if choice == 2:# starts game for subtration option
   print("Let's play a subtraction game.")
   a = Create_Random_Number()
   b = Create_Random_Number()
   right = a - b
   print("What does ", a, " - ", b, "equal?")
   while userCongratulated or start: #Call menu regardless of answer
     answer = Ask_User_Number()
     if answer == right:
       print("Congratulations, the answer is correct!")
       main()
     else:
       print("That is incorrect, the answer is ", right)
       main()
   
 if choice == 3:
   print("Goodbye")
   exit()

if __name__ == '__main__':
 main()
