# Andy Villegas
# EX 2

import random #imports random library

random.randint(1, 100)
Min = 1
Max = 100
span = Max - Min
guess = int(span / 2)
print("Use (H) for higher, (L) for lower, or (E) for equal.")
print("I guess this number:", guess)
you = input("Is your number Higher, Lower, or Equal to my number: ")
if you == 'H':
    Min = guess + 1
    span = Max - Min
    guess = int(span / 2) + Min #determing what number it might be
if you == "L":
    guess = int(span / 2) + Min
if you == "L":
    Max = guess - 1
    span = Max - Min
    guess = int(span / 2) + Min
if you == "E":
    print("Thank you for playing")
    exit(3)
print("I guess this number", guess)
you = input("Is your number Higher, Lower, or Equal to my number: ") #determines the best course of action
if you == 'H':
    Min = guess + 1
    span = Max - Min
    guess = int(span / 2) + Min
if you == "L":
    Max = guess - 1
    span = Max - Min
    guess = int(span / 2) + Min
if you == "E":
    print("Thank you for playing")
    exit(4)
print("I guess this number", guess)
you = input("Is your number Higher, Lower, or Equal to my number: ")
if you == 'H':
    Min = guess + 1
    span = Max - Min
    guess = int(span / 2) + Min
if you == "L":
    Max = guess - 1
    span = Max - Min #chooses which numbers are eligible to be used
    guess = int(span / 2) + Min
if you == "E":
    print("Thank you for playing")
    exit(5)
print("I guess this number", guess)
you = input("Is your number Higher, Lower, or Equal to my number: ")
if you == 'H':
    Min = guess + 1
    span = Max - Min
    guess = int(span / 2) + Min
if you == "L":
    Max = guess - 1
    span = Max - Min
    guess = int(span / 2) + Min
if you == "E":
    #possible results end user may recieve
    print("Thank you for playing")
    exit(6)
print("I guess this number", guess)
you = input("Is your number Higher, Lower, or Equal to my number: ")
if you == 'L' or 'H':
    print("You beat me :c")
if you == "E":
    print("I win!")
    exit(7)
