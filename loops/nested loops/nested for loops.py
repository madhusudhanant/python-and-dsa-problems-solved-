'''
### 1. palindrome from 100 to 300

n = int(input("n: ")) #100
n1 = int(input("n1: ")) #300

i = 1
for i in range(n, n1 + 1):
    a = i
    b = 0
    d = i
    i = 1
    for j in range(a):
        x = a % 10
        b = b * 10 + x
        a = a // 10
        
        if a == 0:
            break
    if b == d:
        print(d, "is palindrome")


#2. prime numbers from 1 to 100

n =  int(input("n: "))
n1 = int(input("n1: "))
for i in range(n, n1 + 1):
    a = i
    c = 0
    for j in range(1, a + 1):
        if a % j == 0:
            c = c + 1
    if c == 2:
        print(a, "is prime number")

n =  int(input("n: "))
n1 = int(input("n1: "))
for i in range(n, n1 + 1):
    a = i
    c = 0
    for j in range(1, a+1):
        if a % j ==0:
            c = c+1
    if c == 2:
        print(a, "is prime number")
        

#3. armstromg number from 1 - 100   o/p 153
n = int(input("enter n:")) #100
n1 = int(input("enter n1:")) # 200

for i in range(n, n1):
    a = i
    c = 0
    b = i
    x = 0
    
    for j in range(1, a):
        a = a // 10
        c = c + 1
        if a == 0:
            break
    for k in range(1, b):
        d = b % 10
        h = pow(d, c)
        x = x + h
        b = b // 10
        if b == 0:
            break
    if x == i:
        print(x, "is armstrong")



n = int(input("enter n:")) #100
n1 = int(input("enter n1:")) # 200

for i in range(n, n1):
    a = i
    c = 0
    b = i
    y = 0
    u = i
    for j in range(1, a):
        a = a // 10
        c+=1
        if a == 0:
            break
    for k in range(1,b):
        x = b % 10
        h = x ** c
        y = y + h
        b = b // 10

        if k == 0:
            break
    if u == y:
        print(y)
        

## 4.adam numbers
n = int(input("enter n:")) #100
n1 = int(input("enter n1:")) # 200     

for i in range(n, n1+1):
    u = i
    a = i
    q = 0
    l = pow(i, 2) # 12 === 144
    for z in range(a): # 12
        p = a % 10
        q = q * 10 + p
        a = a // 10 # 21
        if a == 0:
            break
    x = pow(q, 2) # 21 === 441
    k = 0
    for j in range(x):
        p = x % 10 # 441
        k = k * 10 + p
        x = x // 10 # 114
        if x == 0:
            break
    if l == k:
        print(u, "is adam number")   
    

## 5.adam numbers # 1 to 100
n = int(input("enter n:")) #100
n1 = int(input("enter n1:")) # 200     

for i in range(n, n1+1):
    u = i
    a = i
    q = 0
    l = pow(i, 2) # 12 === 144
    for z in range(a): # 12
        p = a % 10
        q = q * 10 + p
        a = a // 10 # 21
        if a == 0:
            break
    x = pow(q, 2) # 21 === 441
    k = 0
    for j in range(x):
        p = x % 10 # 441
        k = k * 10 + p
        x = x // 10 # 114
        if x == 0:
            break
    if l == k:
        print(u, "is adam number") 

## 6. automorpic num from 1 to 100   # 5^2 === 25 , 6^2 = 36, 25^2 = 625 last number should be same 

n = int(input("enter n:")) #1
n1 = int(input("enter n1:")) # 100    

for i in range(n, n1+1):
    a = i
    b = i
    c = 0
    p = pow(a, 2)
    y = 0
    for j in range(a):
        x = a % 10
        c = c + 1
        a = a // 10
        if a == 0:
            break
    y = p % pow(10, c)
    if y == b:
        print(b," is a automorpic")
        

# 7. student grade fro each subject

n = int(input("how many students:")) # 5 students
n1 = int(input("How many subjects:")) # How many subjects (5 subjects)


for i in range(1, n):
    a = n
    y = 0
    t = 0
    print("students", i)
    for j in range(a):
        s = int(input("enter marks: "))
        y = y + s
        t = y / n1
        
    if t >= 90:
        print("grade A")
    elif t >= 80 and t < 90:
        print("grade B")
    elif t >= 70 and t < 80:
        print("grade C")
    elif t >= 60 and t < 70:
        print("garde D")
    else:
        print("Fail") 


## 8. strong number 145 # factorial for each number and sum
n = int(input("enter n:")) # 145
s = 0
for i in range(1, n+1):
    a = n % 10
    f = 1
    for j in range(1, a + 1):
        f = f * j
    s = s + f
    n = n // 10
    if n == 0:
        break
print(s)


## 9. multiplication table chart

n = int(input("Table from: ")) #4
n1 = int(input("Table Till")) #6
n3 = int(input("till table")) #10

for i in range(n, n1+1):
    for j in range(1, n3+1):
        c = i * j
        print(j,"*",i,"=",c)
    print()

'''




































































        

