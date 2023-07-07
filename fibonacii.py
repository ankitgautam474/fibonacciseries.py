limit = int(input("Enter the limit: "))

# initialize the first two numbers
num1, num2 = 0, 1

# print the first number of the series
print(num1, end=' ')

# generate the Fibonacci series
while num2 <= limit:
    print(num2, end=' ')
    num1, num2 = num2, num1 + num2