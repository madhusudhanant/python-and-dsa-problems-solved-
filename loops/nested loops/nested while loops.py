'''
## NESTED LOOPS ##
#1. palindrome numbers from 100 to 999
n=int(input("enter n:"))
n1=int(input("enter n1:"))
while(n<=n1):
    a=n
    s=0
    while(a>0):
        re=a%10
        s=(s*10)+re
        a=a//10
    if(s==n):
        print(n)
    n=n+1

## 2. prime numbers from 1 to 100
n = int(input("enter n:"))
n1 = int(input("enter n1:"))
while (n <= n1):
    a = n
    s = 0
    i = 1
    while(i <= a):
        if a % i == 0:
            s = s + 1
        i = i + 1
    if s == 2:
        print(a, "prime numbers")
    n = n + 1

#3. armstrong numbers from 100 to n      
n = int(input("enter n:"))
n1 = int(input("enter n1:"))

while (n <= n1):
    a = n
    b = n
    c = 0
    i = 1
    x = 0
    while(a > 0):
        a = a // 10
        c = c + 1

    while(b > 0):
        d = b % 10
        h = pow(d, c)
        x = x + h
        b = b // 10
    if x == n:
        print(x, "is armstrong")
    n = n + 1


#4 adam from 100 t0 300

import math
n = int(input("enter n:"))
n1 = int(input("enter n1:"))


while (n <= n1):
    a = n
    b = n
    q = 0
    j = 0
    x = pow(a, 2)
    
    while(a > 0):
        p = a % 10
        q = q * 10 + p
        a = a // 10
    y = pow(q , 2)
    
    while(y > 0):
        m = y % 10
        j = j * 10 + m
        y = y // 10
    if j == x:
        print(n, "is adam")
    n = n + 1

#5 adam num from 1 to 100


n = int(input("enter n:"))
n1 = int(input("enter n1:"))

while n <= n1:
    a = n
    c = 0
    e = 0
    k = n
    p = pow(a, 2)
    
    while a > 0:
        b = a % 10
        c = c * 10 + b
        a = a // 10
    y = pow(c, 2)

    while y > 0:
        d = y % 10
        e = e * 10 + d
        y = y // 10
    if e == p:
        print(n, "is adam")
    n = n + 1    

##6 automorpic numbers from 1 to 100

import math
n = int(input("enter n:"))
n1 = int(input("enter n1:"))
while n <= n1:
    a = n
    u = n
    c = 0
    d = 0
    p = pow(a, 2)
    while a > 0:
        b = a % 10
        c = c + 1
        a = a // 10

    d = p % pow(10, c)
    n = n + 1
    if u == d:
        print(u, "is a automorphic")

## 7. Calculate student grade for each subject

n = int(input("enter no of students:"))
n1 = int(input("enter subjects:"))
i = 1
while i <= n:
    j = 1
    a = 0
    t = 0
    print("student:", i)
    while j <= n1:
        s = int(input("subjects: "))
        t = t + s
        a = t / n1
        j = j + 1
        
    if a >= 90:
        print("grade A")
    elif a >= 80 and a < 90:
        print("grade B")
    elif a >= 70 and a < 80:
        print("grade C")
    elif a >= 60 and a < 70:
        print("garde D")
    else:
        print("Fail")
    i = i + 1
        

## 8. strong number  i/p = 145, 1!, 4!, 5! = 145

n = int(input("enter n: "))
u = n
d = 0
while n > 0:
    a = n % 10
    f = 1
    i = 1
    while i <= a:
        f = f * i
        i = i + 1
    d = d + f
    n = n // 10
if d == u:
    print(u, "is strong number")
    


##9. multiplication table chart

n = int(input("n1: ")) # 4
n1 = int(input("n2: ")) # 6
n3 = int(input("no of Times: "))


while n <= n1:
    a = n
    i = 1
    
    while i <= n3:
        c = a * i
        print(i,"*",a,"=",c)
        i = i + 1
    n = n + 1

''' 

























































