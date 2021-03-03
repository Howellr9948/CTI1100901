# CTI - 110
# P3HW2 - Distance Traveled
# Rheanna Howell
# 20210227
# adding more properties to P2HW1 - Distance Traveled
# adding else - if statement so the program can run
# 

speed = float(input('Enter speed: '))
time = float(input('Enter time: '))

#enter an error message if time is < 0
print()
if time <= 0:
    print('Error! Time entered should be >0')
else:
    distance = speed * time
    print()
    print("Speed entered: ", speed)
    print("Time entered: ", time)
    print("Distance entered: ", distance)
