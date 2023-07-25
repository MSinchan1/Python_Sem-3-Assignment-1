#   10.Write a program to merge two sorted array of length M and N(M and N may not be equal)
M = int(input("Enter the size of the first array: "))
a1 = []
print("Enter the first array elements:")
for i in range(M):
    a1.append(int(input()))
N = int(input("Enter the size of the second array: "))
a2 = []
print("Enter the second array elements:")
for i in range(N):
    a2.append(int(input()))
merged_array = []
i = j = 0
while i < len(a1) and j < len(a2):
    if a1[i] < a2[j]:
        merged_array.append(a1[i])
        i += 1
    else:
        merged_array.append(a2[j])
        j += 1
while i < len(a1):
    merged_array.append(a1[i])
    i += 1
while j < len(a2):
    merged_array.append(a2[j])
    j += 1
print("Merged sorted array:")
for num in merged_array:
    print(num, end=" ")