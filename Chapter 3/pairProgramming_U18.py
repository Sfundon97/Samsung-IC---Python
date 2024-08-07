#Recursive Function
#Q1
def number(n):
    n = int(input('Enter a number '))
    sum1 = 0
    for i in range(1, n+1):
        sum1 = sum1 + i
        print(sum1)

number(0)

#Q2
def power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(x, -n)
    else:
        return x * power(x, n - 1)

# Prompting the user to enter the values for x and n
x = int(input("Enter x: "))
n = int(input("Enter n: "))


result = power(x, n)
print(result)
