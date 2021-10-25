#Andy Villegas
count = 0
a = 0
b = 0
c = 0
#defines the variables we're gonna use throughout the program
while count <= 100:
    print(a, "+", b, "=", c)
    a = c
    b = b + 1
    c = a+b
    count = count+1