#Andy Villegas
my_num_list = [3,6,4,83,2,7,2,17,4,9,0,44,2]

print(my_num_list[3])  #finds out which is the 3rd element in the string
print("----------------------------------")

my_num_list = [3,6,4,83,2,7,2,17,4,9,0,44,2]
my_num_list.append(8) #adds 8 to the end of the string
print(my_num_list)
print("----------------------------------")

my_num_list = [3,6,4,83,2,7,2,17,4,9,0,44,2]
my_num_list.insert(4,33) #inserts 33 after the 4th element
print(my_num_list)
print("----------------------------------")

my_num_list = [3,6,4,83,2,7,2,17,4,9,0,44,2]
count = my_num_list.count(2) #counts how many times 2 is used in the string
print(count)
print("----------------------------------")

my_num_list = [3,6,4,83,2,7,2,17,4,9,0,44,2]
my_num_list.sort()  #sorts from least to greatest valuable
print(my_num_list)
print("----------------------------------")

my_num_list = [3,6,4,83,2,7,2,17,4,9,0,44,2]
print(len(my_num_list)) #prints the length of the string
print("----------------------------------")

my_num_list = [3,6,4,83,2,7,2,17,4,9,0,44,2]
print(my_num_list.pop(),end=" ")
print(my_num_list.pop(),end=" ")
print(my_num_list.pop(),end=" ") #removes the last element from the string and returns it in a new string
print(my_num_list.pop())
print("----------------------------------")

my_num_list = [3,6,4,83,2,7,2,17,4,9,0,44,2]
my_num_list.pop()
my_num_list.pop()
my_num_list.pop()
my_num_list.pop()
print(len(my_num_list)) #finds out length of string after removing last 4 elements
print("----------------------------------")

