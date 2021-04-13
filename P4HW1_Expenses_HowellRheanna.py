#CTI-110
#P4HW1 - Expenses
#Rheanna Howell
#20210409

#Program:
#Prompt user to enter amount in account in which money will be withdrawn from
#Prompt user to enter amount of first expense
#Subtract expense from account
#Ask user if he/she would like to enter another expense.
#Program DOES NOT move on to next step unless user chooses not to enter another expense.

#if user says no for second expense:
#Amount in account BEFORE expenses subtracted
#Number of expenses entered
#Amount in account AFTER expenses subtracted

#Psuedocode:
#prompt user for the starting account balance
account = float(input('Enter starting amount in account: $'))
print()
#variable for current expense entered by user
currentExpense = 0.0
#variable for the total expenses entered by user, so far
totalExpenses = 0
#initialize counter for the expense
numExpenses = 0
#variable for user choice about entering any more expenses or not
yesNo='\0'
#while loop until user enters 'n' or 'N'
while yesNo !='n' and yesNo !='N':
    #prompt user for expenses one by one
    currentExpense=float(input('Enter expense {0}: $'.format((numExpenses + 1))))
    #increase the number of expenses by 1
    numExpenses += 1
    #add current expense to the total expenses amount
    totalExpenses += currentExpense
    #prompt user to continue loop or exit loop
    yesNo = input('Do you want to enter another expense?(y/n) ')
    #if user chooses 'n', display the results and exit loop
    if yesNo =='n' or yesNo =='N':
        print('\nAmount in account before expenses subtracted: ${0:.1f}'.format(account))
        #calculate
        account -= totalExpenses
        print('Number of expense entered: {0}'.format(numExpenses))
        #print balance after subtracting the total expense
        print('Amount in account after expenses subtracted: ${0:.1f}'.format(account))
        #exit loop
        break
    print()
