from timeit import *
#CHAPTER 2

#Append method and sum method
# person1 = ["John Smith", 20, 1, 180.0, 100.0]
# person2 = ["Joe Doe", 25, 1, 170.0, 70.0]
# person3 = ["jane Carter", 22, 0, 169.0, 60.0]
# person4 = ["Peter Kelly", 40, 1, 150.0, 50.0]
# list3 = list(range(2, 10))
# print(list3)
# person1.append("Sfundo Nondi")
# print(person1)
# del person1[5]
# print( 100.0 in person1)

# person_list = person1 + person2 + person3 + person4

# n_persons = int (len(person_list)/5)
# age_sum = 0.0
# for age in person_list[1::5] :
#     age_sum += age
# average_age = float(age_sum)/n_persons
# print('The average age is ' + str(average_age))

# element = [2, 3, 5, 7]
# l = element.copy()
# element.append(11)
# newList = list(range(1,11))

# print('Created List: ', newList)
# print("Original list ",element)
# print("Copied list ",l)
# print('The first element of prime list is ', element[0])

# #copy and count methods
# sample_list = ['a', 'b', 'c', 'd', 'e']
# target = input('Enter a character to search for: ')
# count = sample_list.count(target)
# print(f'Number of occurence of: {target} is {count}')

# #index method
# fruit = ['Apple', 'Banana', 'Pear']
# target1 = input('Enter a fruit name: ')
# try:
#     index = fruit.index(target1)
#     print(f'The occurence of {target1} is at {index}')
# except ValueError:
#     print(f'The fruit name {target1} is not found')

# #count method
# target2 = input('Enter a number up to 11: ')
# try:
#     count1 = element.count(int(target2))
#     print(f'The occurence of {target2} is {count1}')
# except ValueError:
#     print(f'The value of {target2} does not exist')

# #DICTIONARY pop and clear methods
personDetails = {'name' : 'Sfundo', 'age' : 20, 'city' : 'Bloemfontein', 'minor' : False}
# age = personDetails.pop('age')
# print(f'The age of is {age}')
# print('Updated Dictionary: ', personDetails)
# personDetails.clear()
# personDetails.items("John Doe")
# print( personDetails)

# #SETS add method
# mySet = {2, 3, 4, 5 ,6}
# print(mySet)
# mySet.add(9)
# print('Uodated Set: ', mySet)

# #Dictionary Edit and Add Key-Value method
# str1 = ['a', 'b', 'c', 'a', 'a', 'b', 'c']
# dic = {}

# for character in str1:
#     if character not in dic.keys():
#         dic[character] = 0
#     dic[character] += 1

# #with setdefault
# print('alphabet counting: ', dic)

# dictio = {'key1' : 'sunglasses', 'key2' : 'shoes'}
# print(dictio)

#Q1 of the quiz
# l1 = ['I like', 'I love']
# l2 = ['pancake', 'kiwi juice', 'espresso']

# print(l1[0] +' '+ l2[0])
# print(l1[0] +' '+ l2[1])
# print(l1[0] +' '+ l2[2])
# print(l1[1] +' '+ l2[0])
# print(l1[1] +' '+ l2[1])
# print(l1[1] +' '+ l2[2])

# #Python Scoping Rule
# x = 10
# y = 11

# def foo():
#     x = 20
#     def bar():
#         a = 30
#         print(a, x, y)
#     bar()
#     x = 40()
#     bar()

# foo()

# def print_va():
#     global counter 
#     counter = 200
#     print("Counter = ", counter)

# print_va()
# counter = 100

# print("Counter = ", counter)

# #Arbitrary arguement
# def greet(*names):
#     for name in names:
#         print('Hello', name, '!')
        
      
# greet('A', 'B', 'C', 'D')

# #Default Parameter
# def star(n = 1):
#     for _ in range(n):
#         print('**************************')

# star(5)

# def divide(a, b = 2):
#     return a / b

# print('div(4) =', divide(4))

# #Keyword Parameter or Named Parameter
# def get_root(a, b, c):
#     r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5)/(2 * a)
#     r2 = (-b + (b ** 2 - 4 * a * c) ** 0.5)/(2 * a)

#     return r1, r2
# result1, result2 = get_root(1, 2, -8)
# print('The result is', result1, 'or', result2)

# #Advantage of using Keyword Parameter is that it does not matter what position they are
# result1, result2 = get_root(a=1,b= 2,c= -8)
# print('The result is', result1, 'or', result2)

# result1, result2 = get_root(a=1,c= -8, b= 2)
# print('The result is', result1, 'or', result2)

# #Factorial
# n = int(input('Enter a number: '))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i

# print('{}! = {}'.format(n, fact))

#Finding a Factorial with a Recursive Function
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# n = 5
# print('{}! = {}'.format(n, factorial(n)))

# #Fibonacci Function
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return(fibonacci(n-1) + fibonacci(n-2))
# nterms = int(input("How many Fibonacci numbers do you want? "))

# #Cannot find Fibonacci number if it is negative
# if nterms <= 0:
#     print("Error: Enter a positive number.")
# else:
#     print("Fibonacci sequence")
#     for i in range(nterms):
#         print(fibonacci(i), end='')

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print()   
# print(fib(10))

# def fib1(n):
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         return fib1(n-1) + fib(n-2)

# t3 = Timer("fib1(30)", "from __main__ import fib1")
# print("fib1(30) * 20 times: ", t3.timeit(number= 20), "seconds")  

#Paper Coding
# def number(n):
#     n = int(input('Enter a number '))
#     sum1 = 0
#     for i in range(1, n+1):
#         sum1 = sum1 + i
#         print(sum1)

# number(0)
# def sum(x,y):
#     return x + y
# num1 = int(input('Enter number 1: '))
# num2 = int(input('Enter number 1: '))
# print(sum(num1, num2))

# #Lambda Expression
# add = lambda x, y:  x + y
# num3 = int(input('Enter number 1: '))
# num4 = int(input('Enter number 1: '))
# print('Lambda Expression')
# print(add(num3, num4))

#Filter Function
def adult(n):
    if n >= 19:
        return True
    else:
        return False
ages = [23, 22, 19, 16, 45, 32, 10]
print('Adults:')
for adults in filter(adult, ages):
    print(adults, end= ' ')

#Filter Function with Lambda
adult1 = lambda x : x > 18
ages1 = [23, 22, 19, 16, 45, 32, 10]
print()
print('Adults:')
for adult1 in filter(adult1, ages1):
    print(adult1, end= ' ')

