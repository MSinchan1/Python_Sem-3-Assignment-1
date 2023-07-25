#  1.	*
#	    #*
#	    #*#
#	    *#*#
#	    *#*#*
n = int(input("Enter no of rows: "))
c = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        if c >= 1 and c <= 2:
            if (i + j) % 2 == 0:
                print("*", end="")
            else:
                print("#", end="")
        if c >= 3 and c <= 4:
            if (i + j) % 2 == 0:
                print("#", end="")
            else:
                print("*", end="")
    if c == 4:
        c = 1
    c += 1
    print()