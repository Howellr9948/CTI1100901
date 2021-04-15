# CTI - 110
# P4HW2 - Distance Traveled
# Rheanna Howell
# 20210414
# adding more properties to P3HW2 - Distance Traveled
# adding else - if statement so the program can run
# Program will be displayed in a tabular format

#Psuedocode:
# enter variables for speed and time
# prompt will be float 
speed = int(input("Enter car's speed: "))
print()
time = int(input("Enter time traveled: "))


#This loop will run until break statement is executed
while (True):
    #if time is greater than zero
    #print in tabular format
    if(time<=0):
        print("Error ! time entered should be > 0")
        
        print("Time        Distance")
        i=1
        while i<time+1:
            print(i,"           ",float(i*speed))
            i=i+1
        print("Would you like to enter a different time? (y for yes): ")
        s = input()
        #break the loop if user entered no
        if(s=="n"):
            break
    #take input again in case of error/enter a different time
        time = int(input("Enter time traveled: "))
    else:
        print("Time        Distance")
        i=1
        while i<time+1:
            print(i,"           ",float(i*speed))
            i=i+1
        print("Would you like to enter a different time? (y for yes): ")
        s = input()
        #break the loop if user entered no
        if(s=="n"):
            break
    #take input again in case of error/enter a different time
        time = int(input("Enter time traveled: "))

# The program is to display the results in a tabular format below:
# the if for the loop is used, range function only accepts integers


#Ask user if they'd like to run program and enter a different number of hours
