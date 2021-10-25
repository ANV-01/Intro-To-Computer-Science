#Andy Villegas
my_char_list = ['a','b','a','c','d','a','d','z','r','a']
print(len(my_char_list)) #prints the length of a string
print("------------------------------")

my_char_list = ['a','b','a','c','d','a','d','z','r','a']
print(my_char_list.index("d")) #finds the first d element in the string and prints it
print("------------------------------")

my_char_list = ['a','b','a','c','d','a','d','z','r','a']
my_char_list.insert(4,"a") #inserts a after the 4th element
print(my_char_list)
print("------------------------------")

my_char_list = ['a','b','a','c','d','a','d','z','r','a']
my_char_list.insert(4,"a")
print(len(my_char_list)) #prints the length of the list after adding an element
print("------------------------------")

my_char_list = ['a','b','a','c','d','a','d','z','r','a']
my_char_list.insert(4,"a")
print(my_char_list.count("a")) #counts how many times a is used in the string
print("------------------------------")

