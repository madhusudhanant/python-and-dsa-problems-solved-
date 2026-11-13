
'''## Bubble sort - with argument without return // type 2
def bubble(n,x):
    for i in range(n):
        for j in range(i + 1,n):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
        print(x)
        
n = int(input("bubble sort: "))
x = []
for i in range(n):
    a = int(input("a: "))
    x.append(a)
bubble(n,x)


# with argument with return // type 4
def bubble(n,x):
    for i in range(n):
        for j in range(i + 1,n):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    return x       
n = int(input("bubble sort: "))
x = []
for i in range(n):
    a = int(input("a: "))
    x.append(a)
l = bubble(n,x)
print(l)
    

#selection sort // with argument without return // type 2
def selection(n,x):
    for i in range(n):
        mi = i
        for j in range(i + 1, n):
            print("j =", j)
            if x[mi] > x[j]:
                mi = j
        x[i],x[mi] = x[mi], x[i]
        print(x)
        
n = int(input("selection sort: "))
x = []
for i in range(n):
    a = int(input("a: "))
    x.append(a)
print(x)
selection(n,x)


#selection sort with argument with return // type 4
def selection(n,x):
    for i in range(n):
        mi = i
        for j in range(i + 1, n):
            if x[mi] > x[j]:
                mi = j
        x[i],x[mi] = x[mi], x[i]
    return x
        
n = int(input("selection sort: "))
x = []
for i in range(n):
    a = int(input("a: "))
    x.append(a)
a = selection(n,x)
print(a)


#insertion sorting // with argument without return // type 2
def insertion(n,x):
    for i in range(1,n):
        j=i
        while(j > 0):
            if(a[j] < a[j-1]):
                a[j], a[j-1] = a[j-1], a[j]
            j = j-1
        print(a)
    print("Sort array",a)
n=4
a=[]
for i in range(n):
    x=int(input("Enter element: "))
    a.append(x)
insertion(n,x)

#insertion sorting with argument with return // type 4

def insertion(n,a):
    for i in range(1,n):
        j = i
        while j > 0:
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            j = j - 1
    return a
n = 4
a = []
for i in range(n):
    x = int(input("elements: "))
    a.append(x)
u = insertion(n,a)
print(u)


###heap sort  // i/p - 8972... find max then sort it// with argument without return // type 2
def heap(n,x):
    for i in range(n-1,0,-1):
        for j in range(1, i + 1):
            k = j
            while(k > 0):
                z = (k-1) // 2
                if x[z] < x[k]:
                    x[z], x[k] = x[k], x[z]
                    k = z
                else:
                    break
        x[0], x[i] = x[i], x[0]
        print(x)
n = int(input("heap sort: "))
x = []
for i in range(n):
    a = int(input("a: "))
    x.append(a)
heap(n,x)

###heap sort with argument with return // type 4
def heap(n,x):
    for i in range(n-1,0,-1):
        for j in range(1, i + 1):
            k = j
            while(k > 0):
                z = (k-1) // 2
                if x[z] < x[k]:
                    x[z], x[k] = x[k], x[z]
                    k = z
                else:
                    break
        x[0], x[i] = x[i], x[0]
    return x
    
n = int(input("heap sort: "))
x = []
for i in range(n):
    a = int(input("a: "))
    x.append(a)
d = heap(n,x)
print(d)



# merge sort - with argument without return type 2
# indirect recursion

def short(x):
    n = len(x)
    
    if n <= 1:
        return
    
    mid = n // 2

    left = x[:mid]
    r8 = x[mid:]
    
    print("left", left)
    print("right", r8)
    
    short(left)
    short(r8)
def merge(n, x):
    short(x)
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    print("sorted:", x)
    
    
n = int(input("merge sort: "))
x = []

for i in range(n):
    a = int(input("a: "))
    x.append(a)
merge(n, x)

# merge sort - with argument with return type 4
# indirect recursion
def short(x):
    n = len(x)

    if n <= 1:
        return
    mid = n // 2
    left = x[:mid]
    right = x[mid:]

    print("left", left)
    print("right", right)

    short(left)
    short(right)
    
def merge(n,x):
    short(x)
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    return x
n = int(input("merge sort: "))
x = []

for i in range(n):
    a = int(input("a: "))
    x.append(a)
d = merge(n,x)
print(d)


##indirect recursion
def fun1(n):
    if n > 0:
        print("fun1", n)
        fun2(n-1)
def fun2(n):
    if n > 0:
        print("Fun2", n)
        fun1(n-1)

n = int(input("n: "))
print(fun1(n))


###Quick sort - pivot - with argument without return type 4

def quick(x):
    n = len(x)
    if n <= 1:
        return

    pivot = x[-1]
    left = []
    right = []
    for i in range(n-1):
        if x[i] <= pivot:
            left.append(x[i])
        else:
            right.append(x[i])
            
            
    print("left", left)
    print("right", right)
    quick(left)
    quick(right)

def short(x,n):
    quick(x)
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    print("sorted: ",x)

n = int(input("quick sort: "))
x = []
for i in range(n):
    a = int(input("a: "))
    x.append(a)
short(x,n)


###Quick sort - with argument with return type 4
def quick(x):
    n = len(x)
    if n <= 1:
        return

    pivot = x[-1]
    left = []
    right = []
    for i in range(n-1):
        if x[i] <= pivot:
            left.append(x[i])
        else:
            right.append(x[i])

    print("left", left)
    print("right", right)
    quick(left)
    quick(right)

def short(x,n):
    quick(x)
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    return x
n = int(input("quick sort: "))
x = []
for i in range(n):
    a = int(input("a: "))
    x.append(a)
d = short(x,n)
print(d)
'''























































        
