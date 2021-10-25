#Andy Villegas
import random
myString = "hello from my function"
def text():
    print(myString) #prints the string assigned to myString
text()
print("\n--------------------")
def numberrange():
    for i in range(1,21):
        print(i, end=" ") #prints the entire range of numbers from 1-20
numberrange()
print("\n--------------------")
def numberrandom():
    num = int(input("Please enter a number:"))
    sum = (num * 7)
    print(sum) #multiplies whatever number the user inputted by 7
numberrandom()
print("\n--------------------")
def words():
    my_list = ["sixteen","twenty-nine","throw","it","up"]
    my_list.sort()
    print(my_list) #sorts my_list before printing it
words()
print("\n--------------------")
