#Andy Villegas
import time
import random #imports time and random library

print("16")
time.sleep(0.2)
print("*")
time.sleep(0.2)
print("29")
time.sleep(0.2)
print("Throw")
time.sleep(0.2)
print("It")
time.sleep(0.2) #This counts the amount of seconds till it can execute
print("Up!")
print('--------------------')
print(time.time())
time.sleep(0.5)
print(time.time())
time.sleep(1.0)
print(time.time()) #shows the current time
print('--------------------')
count = 0
while count <= 10:
    print(count)
    count = count+1 #get the count number and adds 1
print('--------------------')
count = 0
while count <= 10:
    print(count, end="-") #end="-" adds a - after every count that is printed
    count = count+1
print("\n--------------------")
count = 1
while count <= 5: #while loop that keeps running until the count variable reaches 5 or more
    print(count)
    count = count+1
    time.sleep(0.5)
print('--------------------')
count = 0
while count <= 20:
    print(count)
    count = count+2
print('--------------------')
count = 20
while count > 0:
    print(count)
    count = count-3
print('--------------------')
count = 0
while count < 10:
    print(random.randint(0, 100)) #gets a random integer between 0-100
    count = count+1
print('--------------------')
count = 0
while count <= 100:
    userinput = int(input("Enter a number greater than 100:")) #Asks user for an input greater than 100
    count = userinput

print("Thank you")