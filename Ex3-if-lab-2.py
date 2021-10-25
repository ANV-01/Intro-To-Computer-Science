#Andy Villegas
#EX 3

print("Use (Y) or (N) for yes or no.")
user = input("Does your organism live in the ocean? " ) #asks user for input
if user == 'Y': #If yes, it'll determine what ocean animal it is
    user=input("Does it have fins?")
    if(user == 'Y'):
        print("Your organism is a Fish.")
        exit(1)
    if(user == 'N'):
        print("Your organism is an Octopus.")
        exit(2)
elif(user == 'N'): #if no, it'll determine what land animal it is
    user=input("Does your organism have legs?")
    if(user == 'Y'):
        print("Your organism is a Tarantula.")
        exit(3)
    if(user == 'N'):
        print("Your organism is a Snake.")
