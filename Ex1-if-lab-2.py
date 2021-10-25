#Andy Villegas
#EX 1
import random #imports the random library
count = 0
secret = random.randint(1,100) #chooses a random number from 1-100

user = int(input("Guess a number from 1-100: "))
count += 1
if user > secret:
    print("The number is lower")
elif user < secret:
    print("The number is higher")
elif user == secret:
    print("YOU WIN!")
    print("You made it in",count,"guess(es).")
    exit(1) #Guess 1
user = int(input("Guess a number from 1-100: "))
count += 1
if user > secret:
    print("The number is lower")
elif user < secret:
    print("The number is higher")
elif user == secret:
    print("YOU WIN!")
    print("You made it in",count,"guess(es).")
    exit(2) #Guess 2
user = int(input("Guess a number from 1-100: "))
count += 1
if user > secret:
    print("The number is lower")
elif user < secret:
    print("The number is higher")
elif user == secret:
    print("YOU WIN!")
    print("You made it in",count,"guess(es).")
    exit(3) #Guess 3
user = int(input("Guess a number from 1-100: "))
count += 1
if user > secret:
    print("The number is lower")
elif user < secret:
    print("The number is higher")
elif user == secret:
    print("YOU WIN!")
    print("You made it in",count,"guess(es).")
    exit(4) #Guess 4
user = int(input("Guess a number from 1-100: "))
count += 1
if user > secret:
    print("The number is lower")
elif user < secret:
    print("The number is higher")
elif user == secret:
    print("YOU WIN!")
    print("You made it in",count,"guess(es).")
    exit(5) #Guess 5
user = int(input("Guess a number from 1-100: "))
count += 1
if user > secret:
    print("The number is lower")
elif user < secret:
    print("The number is higher")
elif user == secret:
    print("YOU WIN!")
    print("You made it in",count,"guess(es).")
    exit(6) #Guess 6
user = int(input("Guess a number from 1-100: "))
count += 1
if user == secret:
    #this is the possible results the end user may get
    print("YOU WIN!")
    print("You made it in",count,"guess(es).")
else:
    print("             GAME OVER               ")
    print("You did not guess the correct number.")
    print("    The correct number was", secret)
