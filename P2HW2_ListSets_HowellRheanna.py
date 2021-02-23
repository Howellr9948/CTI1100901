#CTI-110
#P2HW2 - List and Sets
#Rheanna Howell
#20210221


#Ask the user to enter a series of 10 numbers
#Input a number list size
lst = []
num = int(input("Enter number of elements: "))


#The program should store the numbers in a list. Give the list a descriptive name.
for n in range(num):
    numbers = float(input('Enter number: '))
    lst.append(numbers)


#Display the following: lowest number, highest number, total of the numbers, average of the numbers.
#Display the minimal number of the list
print()
print("Mininum number is: ", min(lst))
#Display the maximum number of the list
print()
print("Maximum number is: ", max(lst))
#Display the total number of the list
print()
print("Total is: ", sum(lst))
#Display the average number of the list
#Create a variable 'avg' then have the sum divided by the number of elements
print()
avg = sum(lst)/num
print("The Average is: ", avg)

#Convert the list into a set
#Create a variable then have it 'set' the list created
print()
uniqueNumbers = set(lst)

#Display the set content.
print()
print("The Set of entered numbers: ", uniqueNumbers)

#Notes that if list contained duplicated numbers, duplicates will no longer appear in the set created.

