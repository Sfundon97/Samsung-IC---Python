merger_count = 0
#Swapping Algorithm

def swap1(S, x, y):
    t = S[x]
    S[x] = S[y]
    S[y] = t

li = [10, 20]
print(li)
swap1(li, 0, 1)
print(li)

#Bubble Sort
def bubblesort(S):
    n = len(S)
    for i in range(n):
        print(S)
        for j in range(n - 1):
            if S[j]> S[j + 1]:
                S[j], S[j + 1] = S[j + 1], S[j]

S = [10, 50, 20, 40, 30]
bubblesort(S)
print(S)

#Merge Sort
def mergesort(S):
    n = len(S)
    if n > 1:
        print(S)
        mid = n // 2
        L, R = S[:mid], S[mid:]
        mergesort(L)
        mergesort(R)
        merge1(S, L, R)

def merge1(S, L, R):
    k = 0
    while len(L) > 0 and len(R) > 0:
        if L[0] <= R[0]:
            S[k] = L.pop(0)
        else:
            S[k] = R.pop(0)
        k += 1
    while len(L) != 0:
        S[k] = L.pop(0)
        k += 1
    while len(R) != 0:
        S[k] = R.pop(0)
        k += 1
mergList = [27, 10, 12, 20, 25, 13, 15, 22]
mergesort(mergList)
print(mergList)

#Practice
def mergesort1(items):
    m = len(items)

    if m > 1:
        print(items)
        midi = m // 2
        Left, Right = items[:midi], items[midi:]
        mergesort1(Left)
        mergesort1(Right)
        merge(items, Left, Right)

def merge(items, Left, Right):
    l = 0
    global merger_count
    merger_count += 1
    while len(Left) > 0 and len(Right) > 0:
        if Left[0] <= Right[0]:
            items[l] = Left.pop(0)
        else:
            items[l] = Right.pop(0)
        l += 1
    while len(Left) != 0:
        items[l] = Left.pop(0)
        l +=1
    while len(Right) != 0:
        items[l] = Right.pop(0)
        l +=1

mergList1 = [27, 10, 12, 20, 25, 13, 15, 22]
mergesort1(mergList1)
print(mergList1)
print(merger_count)

#Bubble Sort
def bubble_sort(items):
    global merger_count
    
    m = len(items)
    for i in range(m):
        merger_count += 1 
        print(items)
       
        for j in range(m -1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

mergList2 = [27, 10, 12, 20, 25, 13, 15, 22]
mergesort1(mergList2)
print(mergList2)
print(merger_count)