#Write a program whose inputs are three integers
# whose output is the smallest of the three values

user_num = int(input())
user_num2 = int(input())
user_num3 = int(input())

if (user_num < user_num2) and (user_num < user_num3):
    print(user_num)
if (user_num2 < user_num) and (user_num2 < user_num3):
    print (user_num2)
if (user_num3 <= user_num) and (user_num3 <= user_num2):
    print(user_num3)
