# This program takes a number grade and outputs a letter grade
# The program was half complete with a couple of bugs - goal was to complete it and fix the bugs
# Howell, Rheanna
# CTI - 110
# 20210226
# I completed this while in the field and had to use another person hotspot to submit :D

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    # TO DO: define the rest of the scores
    B_score = 80
    C_score = 70
    D_score = 60
    # I made the F score 59 based on the class syllabus 
    F_score = 59

    # making the score float in case the teacher decided to use decimals for grading rather than int
    score = float(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score:
            print('Your grade is: B')    
        elif score >= C_score:
            print('Your grade is: C')
        else:
            if score >= D_score:
                print('Your grade is: D')
            elif score <= F_score:
                    print('Your grade is: F') # TO DO: finish this



# program start
main()
