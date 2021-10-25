#Andy Villegas
rows = 5
for count in range(1, rows + 1):
    print("o" * count) #make 5 rows of o's
print("\n----------------")
for count in range(6, 0, -1):
    print("o" * count) #constantly decreases and then increases after reaching 1 one
print("\n----------------")
count = int(input("Enter a number : "))
#asks user for input to see how many rows they may want
for rand_var in range(1, count, + 1):
    print("o" * rand_var)
for rand_var in range(count, 0, -1):
    print("o" * rand_var)
print("\n----------------")
count = int(input("Enter height : "))
#asks user for input to see how many rows they may want
for rows in range(1, count + 1):
    character = (rows * 2) - 1
    structure = count - rows
    print(" " * structure, end="")
    print("o" * character)