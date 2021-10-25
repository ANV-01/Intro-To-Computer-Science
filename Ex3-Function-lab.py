#Andy Villegas
import random
def dice():
    while 1 == 1:
        sides = 0
        rolls = 0
        i = 0
        rolls = int(input("Enter the ammount of rolls you woudld like:"))
        sides = int(input("Enter the ammount of sides the die will have:"))
        if sides == 4 or int(sides) == 6 or int(sides) == 8 or int(sides) == 10 or int(sides) == 12 or int(sides) == 20:
            while i < int(rolls):
                print(random.randint(1, sides), end=" ")
                i = i + 1
        else:
            while sides != 4 and sides != 6 and sides != 8 and sides != 10 and sides != 12 and sides != 20:
                print("Sides entered must be 4,6,8,10,12,20!")
                sides = int((input("Enter the ammount of sides the die will have:")))
                while i < rolls:
                    print(random.randint(1, sides), end=" ")
                    i = i + 1
        print()
        quit = input("press q, quit, or exit to stop the program")
        if quit == "q" or quit == "quit" or quit == "exit":
            exit()
dice()