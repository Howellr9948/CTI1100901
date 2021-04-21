# Define your function here 
def miles_to_laps(user_miles):
    return user_miles/0.25

if __name__ == '__main__':
    # Type your code here. Your code must call the function. 
    print('{:.2f}'.format(miles_to_laps(float(input()))))