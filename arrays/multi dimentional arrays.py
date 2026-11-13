'''### MULTI DIMENTIONAL ARRAYS
n = int(input("n: "))
n1 = int(input("n1: "))
x = []
for i in range(n):
    g = []
    for j in range(n1):
        a = int(input("a: "))
        g.append(a)
    x.append(g)
        
print(x)

for i in range(n):
    for j in range(n1):
        print(x[i][j], end=" ")
    print()


#1. Transpose matrix
[[12, 23], [34, 45]]
12 34 
23 45

n = int(input("n: "))
n1 = int(input("n1: "))
x = []

for i in range(n):
    y = []
    for j in range(n1):
        a = int(input("a: "))
        y.append(a)
    x.append(y)
print(x)

for i in range(n):
    for j in range(n1):
        print(x[j][i], end=" ")
    print()
#3. idendity matrix or not
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
1 0 0 
0 1 0 
0 0 1 
9
9
its a idendity matrix

n = int(input("n: "))
n1 = int(input("n1: "))
x = []


    for i in range(n):
        y = []
        for j in range(n1):
            a = int(input("a: "))
            y.append(a)
        x.append(y)
    print(x)
else:
    print("input is not squre matrix")
for i in range(n):
    for j in range(n1):
        print(x[i][j], end= " ")
    print()
c = 0
c1 = 0
for i in range(n):
    for j in range(n1):
        if i == j and x[i][j] == 1:
            c = c + 1
        if i != j and x[i][j] == 0:
            c1 = c1 + 1          
h = c + c1
g = n * n1
if h == g:
    print("its a idendity matrix")

#4. Symmetic matrix
n: 2
n1: 2
n: 1
n: 2
n: 2
n: 3
[[1, 2], [2, 3]]
1 2 
2 3 
its a symmetrical matrix


n = int(input("n: "))
n1 = int(input("n1: "))

x = []
if n == n1:
    for i in range(n):
        y = []
        for j in range(n1):
            a = int(input("n: "))
            y.append(a)
        x.append(y)
    print(x)
else:
    print("input is not squre matrix")
c = 0   
for i in range(n):
    for j in range(n1):
        print(x[j][i], end = " ")
        if x[i][j] == x[j][i]:
            c = c + 1
    print()
h = n * n1
if h == c:
    print("its a symmetrical matrix")
else:
    print("not symmetrical matrix")


#2.matrix multiplication
n = int(input("n: "))
n1 = int(input("n1: "))

x = []
if n == n1:
    for i in range(n):
        y = []
        for j in range(n1):
            a = int(input("n: "))
            y.append(a)
        x.append(y)
    print(x)

x1 = []
if n == n1:
    for i in range(n):
        y1 = []
        for j in range(n1):
            a = int(input("n: "))
            y1.append(a)
        x1.append(y1)
    print(x)

for i in range(n):
    for j in range(n1):
        r = 0
        for k in range(n):
            r = r + x[i][k] * x1[k][j]
        print(r,end = " ")
    print()


#5. sudent mark lst in the table formet using matrix
[['madhu', 67, 54], ['raj', 98, 43]]
madhu 67 54 
raj 98 43

n = int(input("n: "))
n1 = int(input("n1: "))
x = []
for i in range(n):
    y = []
    na = str(input("name: "))
    y.append(na)
    for j in range(n1):
        a = int(input("a: "))
        y.append(a)
    x.append(y)
print(x)
for i in range(n):
    for j in range(n1+ 1):
        print(x[i][j], end=" ")
    print()

'''






























