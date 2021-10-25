#Andy Villegas
import random
def dice_1():
    random_num = random.randint(1,6) #Chooses a random number from 1-6
    print(random_num)
dice_1()
print("\n--------------------")
def dice_2():
    return random.randint(1,6) #Stores a random number from 1-6
dice_2()
print("\n--------------------")
def dice_3():
    x = int(input("Please enter the number of sides of the die:"))
    number_rand = random.randint(1,x) #Asks for user input and selects a random number from 1 through to the number the user inputted
    print(number_rand)
dice_3()
print("\n--------------------")
def dice_4():
 x = int(input("Please enter the number of sides of the die:"))
 if x<1:
      print(random.randint(1,6))
 else:
      print(random.randint(1, x)) #Asks for input and if it isnt anything above 1 it will default to 1-6
dice_4()
def dice_5():
    evens = [4,6,8,10,12,20]
    sides = int(input("Please enter the number of sides of the die:"))
    if sides in list(evens):
        print(random.randint(1, sides))  #Asks for input but has to be 4,6,8,10,12
    else:
        print("Sides entered must be 4,6,8,10,12,20!")
dice_5()
print("\n--------------------")
def dice_6(sides, rolls):
    times_rolled = 0
    even = [4, 6, 8, 10, 12, 20]
    while times_rolled < rolls:
        if sides in list(even):
            if times_rolled == (rolls - 1):
                print(random.randint(1, sides))
            else: #Loop for random dice rolls so long as theyre 4,6,8,10,12
                print(random.randint(1,sides), end = " ")
        else:
           print("Sides entered must be 4,6,8,10,12,20!")
        times_rolled += rolls
    times_rolled += 14
dice_6(20,2)
print("\n--------------------")
def dice_7(sides=50, rolls =1):
 return dice_6(sides,rolls)
#returns 1-50