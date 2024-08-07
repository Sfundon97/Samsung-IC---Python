from functools import reduce
#Lambda
#Q1
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = list(filter(lambda x: x % 2 == 0, n_list))

print(even_list)

#Q2
#Q3
def to_upper(letters):
    return letters.upper()

a_list = ['a', 'b', 'c', 'd']
upper_a_list = list(map(to_upper, a_list))

# Printing the result
print(upper_a_list)

#Q4
sum_of_integers = reduce(lambda x, y: x + y, range(1, 101))

# Printing the result
print("Sum of 1 to 100: ",sum_of_integers)
