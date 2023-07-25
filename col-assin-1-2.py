#   2.    A
#   	 B B
#       C C C
#      D D D D
#     E E E E E
n = int(input("Enter no of rows: "))
for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(64 + i), end=" ")
    print()