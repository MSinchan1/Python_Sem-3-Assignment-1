#   4.Consider the given series and calculate the summation upto t'N' number.1+1+4+9+25+64+......+N.
n = int(input("Enter number: "))
a, b = 1, 0
final_sum = 1
for i in range(1, n):
    sum = a + b
    b = a
    a = sum
    final_sum += (sum * sum)
print(final_sum)