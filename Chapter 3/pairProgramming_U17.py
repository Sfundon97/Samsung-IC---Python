
#Q1
def my_greet():
    print('Welcome.')

my_greet()
my_greet()

#Q2
def max2(m, n):
    return max(m, n)

def min2(m, n):
    return min(m, n)

max_v = max2(100, 200)
min_v = min2(100, 200)

print('The greater of', 100, 'or', 200, 'is', max_v)
print('The smaller of', 100, 'or', 200, 'is', min_v)

#Q3
def mile2km(mi):
    return mi * 1.61

for mile in range(1, 6):
    km = mile2km(mile)

    print(f"{mile} mile = {km:.2f} kilometers")
#Q4
def cel2fah(cel):
    fahrenheit = cel * 9/5 + 32
    return fahrenheit

for celcius in range(10, 60, 10):
    faher = cel2fah(celcius)
    print(f"{celcius} degrees Celcius = {faher} degrees Fahrenheit")


