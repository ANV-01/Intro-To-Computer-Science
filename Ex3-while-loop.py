subtotal = 0

entry = input("Please enter a number to add or 'q' to quit >: ") #asks for user input
while entry != "q":
    subtotal = (subtotal + int(entry)) #adds the subtotal with the user input
    print("Your Sub total is", subtotal)
    entry = input("Please enter a number to add or 'q' to quit >: ")

print("Your Grand total is", subtotal)