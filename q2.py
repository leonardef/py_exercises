# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 
# Then, the output should be:40320

n = 8
i = 1
fat = 1

while i <= n:
    fat = fat * i
    i = i + 1
print(fat)

# n = int(input('Log: '))
# fat = 1

# for i in range(1, n + 1):
#     fat = fat * i
# print(fat)
