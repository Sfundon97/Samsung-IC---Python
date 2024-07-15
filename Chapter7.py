#Data Visualisation

import chart
import random
import fund_calc, cal_n, time

x = [1, 2, 2, 3, 4, 5, 6, 7]
chart.histogram(x)

def main():
    i = 0
    for i in range(10):
        a = random.random()
        print(a)

main()

i = 0
for i in range(5):
    a = random.randint(1, 20)
    print(a)
    
def main1():
    t = int(input("Enter the number of people who participated in the hospital donation event: "))
    total = fund_calc.fund(t)

    print("The total donation is: ", total)

    n = int(input("Enter a desired number: "))
    sum_v = cal_n.sum(n)
    print("The sum of adding from 1 until ", n, " is: ", sum_v)

    sum_vv = cal_n.sum(n)
    print("The sum of adding consecutively from 1 until ", n, " is: ", sum_vv)

main1()

for i in range(10):
    print('Hello', i + 1)
    time.sleep(4)