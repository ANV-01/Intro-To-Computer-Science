#Andy Villegas
num_list = [34, 42, 99, 1301, 1, 78, 314, 818, 777]
print(num_list) 
print("----------------------------------------------")
num_list = [34, 42, 99, 1301, 1, 78, 314, 818, 777]
count = 0
while count < len(num_list):
    print(num_list[count], end=" ")
    total = sum(num_list)
    count += 1
#loop to  list the num_list
print("\nTotal =", count)
num_list.sort()
print("Largest Element=", num_list.pop())
#prints the total amount of elements in the string and the largest element in the string