# Andy Villegas
# EX 4

user = input("Is this shape red(Y) or blue(N)? ") #asks user what color shape they have
if user == 'Y': #if user has a red color it will single out only the red colors
    user = input("Does it have more than 4 sides? ")
    if user == 'Y':
        user = input("Is it exactly 4 sides? ")
        if user == 'Y':
            print("Your shape is a red square. ")
        if user == 'N':
            print("Your shape is a red pentagon. ")
        exit(1)
    if user == 'N':
        print("Your shape is a red triangle. ")
        exit(2)
elif user == 'N': #if user has blue color it will single out only the blue colors
    user = input("Does it have more than 4 sides? ")
    if user == 'Y': #if user shape has more than 4 sides it will take out the square from the equation
            user = input("Does it have 6 sides? ")
            if user == 'Y':
                print("Your shape is a blue hexagon.")
                exit(3)
            if user == 'N':
                print("Your shape is a blue pentagon.")
            exit(4)
    if user == 'N': #if user shape has 4 or less sides it will single out only triangle and square
        user = input("Is it exactly 4 sides? ")
        if user == 'Y':
            print("Your shape is a blue square. ")
        if user == 'N':
            print("Your shape is a blue triangle")
