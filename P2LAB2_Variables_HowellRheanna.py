user_int = int(input())

# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space

user_float = float(input())
letter = input()
word = input()

print("Enter integer (32 - 126):\nEnter float:\nEnter character:\nEnter string:")
print(user_int, user_float, letter, word)

# FIXME (2): Output the four values in reverse

print(word, letter, user_float, user_int)
  
# FIXME (3): Convert the integer to a character, and output that character

chara = chr(user_int)
print(user_int, 'converted to a character is', chara)
