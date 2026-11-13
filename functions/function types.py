'''
# Type 1. Without argument & without return

1.addition
 
def addition():
    a=10
    b=20
    c = a+ b
    print(c)
addition()
o/p: 30

2.area

import math
def area():
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    s = (a + b + c) / 2  
    v=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(v)
area()
a=3
b=4
c=5
o/p: 6.0

3.biggest

def biggest():
    a = int(input("a="))
    b = int(input("b="))
    if a>b:
        print(a)
    else:
        print(b)
biggest()

a=10
b=20
20

4.cuboid
def cuboid():
    a = int(input("a="))
    b = 6 * pow(a,2)
    print(b)
cuboid()
a=4
96

5.even odd

def even_odd():
    a = int(input("a="))
    if a%2==0:
        print("Even:",a)
    else:
        print("odd",a)
even_odd()
a=4
Even: 4

6.p_c
def p_c():
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    p = 4*(a+b+c)
    print("parameter triange =",p)
p_c()

7.profit

def profit():
    c = int(input("cost price ="))
    s = int(input("selling price ="))
    if s > c:
        print("profit")
    else:
        print("loss")
profit()
cost price =1000
selling price =1500
profit

### while
1.
def while_1():
    n = int(input("n ="))
    i=1
    while i<=n:
        print(i)
        i+=1
while_1()
n =5
1
2
3
4
5

2.

def reverse():
    n = int(input("n ="))
    i=1
    while n>=i:
        print(n)
        n-=1
reverse()
n =5
5
4
3
2
1

3. current previous

def current():
    n = int(input("n = "))
    while n > 0:
        if n % 2 != 0:
            print("current", n)
            print("previous", n - 2)
        n -= 1
current()
n = 8
current 7
previous 5
current 5
previous 3
current 3
previous 1
current 1
previous -1

4.Armstrong number

def arm():
    n = int(input("n: "))
    c = 0
    t = n
    y=n
    s = 0
    while n != 0:
        c+=1
        n = n // 10
    while t != 0:
        b = t % 10
        m = pow(b,c)
        s+=m
        t=t//10
    if y == s:
        print("arm strong number")
    else:
        print("not arm strong number")
arm()

n: 153
153 is an Armstrong number

## if condition
1. biggest of three numbers

def three():
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    if a>b and a>c:
        print("biggest",a)
    elif b>c and b>a:
        print("biggest",b)
    else:
        print("biggest",c)
three() 

#Nested if
1. gross pay

def gross_pay():
    salary = int(input("s: "))
    if salary <= 10000:
        a = salary * 20/100
        b = salary * 80/100
        g = salary+a+b
        print("gross pay",g)
    else:
        if salary <= 20000:
            a = salary * 25/100
            b = salary * 90/100
            g = salary+a+b
            print("gross pay",g)
        else:
            if salary > 20000:
                a = salary * 30/100
                b = salary * 95/100
                g = salary+a+b
                print("gross pay",g)
gross_pay()
s: 22000
gross pay 49500.0

#for loop
1. binary to decimal

def binary():
    a = int(input("Binary: "))
    decimal = 0
    power = 1

    for i in range(a):
        digit = a % 10
        decimal += digit * power
        power *= 2
        a //= 10
    print("Decimal =", decimal)
binary()
Binary: 1011
Decimal = 11
2.sum of the digits

def digits():
    n = int(input("n: "))
    s = 0
    for i in range(n+1):
        if 1 <=n:
            a = n%10
            s += a
            n = n // 10
    print(s)
digits()
n: 54
9

#array
1. ascending order
def asc():
    n = int(input("n: "))
    a =[]
    for i in range(n):
        b = int(input("b="))
        a.append(b)
    for i in range(n):
        for j in range(i+1,n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    print(a)
asc()
n: 4
b=3
b=7
b=5
b=2
[2, 3, 5, 7]

#multi array

def multi():
    a = [[1,4,7],[2,5,8],[3,6,9]]
    for i in a:
        for j in i:
            print(j, end=" ")
        print()
multi()
1 4 7 
2 5 8 
3 6 9


######### Type 2: with argument and without return value

import math
def area(a):
    c = math.sqrt(3) * pow(a,2) / 4
    print(c)
a = int(input("a="))
area(a)
a=5
10.825317547305483

#while loop

1.reverse
def reverse(n):
    i = 1
    while n >=i:
        print(n)
        n-=1
n = int(input("n: "))
reverse(n)
n: 3
3
2
1

2. arm strong number
def arm(n):
    c = 0
    t = n
    s = 0
    y = n
    while n > 0:
        c+=1
        n = n //10
    
    while t > 0:
        a = t % 10
        d = pow(a,c)
        s+=d
        t=t//10
    if s == y:
        print("arm")
    else:
        print("not arm")
n = int(input("n: ")) # 153
arm(n)

#if condition

1. smallest of three numbers


def three(a,b,c):
    
    if a<b and a<c:
        print("smallest",a)
    elif b<c and b<a:
        print("smallest",b)
    else:
        print("smallest",c)

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
three(a,b,c)

a=10
b=20
c=30
smallest 10




#### Type 1. without argument & without return
def add():
    n = int(input("n: "))
    n1 = int(input("n1: "))
    t = n + n1
    print(t)
add()

### if condition - function

#1. divisible by 5 or not

def division():
    n = int(input("n: "))
    if n % 5 == 0:
        print(n, "is divisible")
division()

#2. odd

def odd():
    n = int(input("n: "))
    if n % 2 != 0:
        print(n, "is odd")
odd()

### if else condition using function

def twonum():
    n = int(input("n: "))
    n1 = int(input("n1: "))
    if n > n1:
        print(n, "n is greater")
    else:
        print(n1, "n1 is greater")
twonum()


### if else ladder using function
# 1. biggest of three numbers
a: 20
b: 10
c: 15
20 A bigger

def ladder():
    a = int(input("a: ")) #20
    b = int(input("b: ")) #10
    c = int(input("c: ")) #15
    if a > b:
        if a > c:
            print(a,"A bigger") 
        else:
            print(c," C is bigger")
    else:
        if b > c:
            print(b,"B is bigger")
        else:
            print(c,"c is bigger")
ladder()

#2. positive or negative or neutral
a: 56
56 positive

def positive():
    a = int(input("a: ")) #0
    if a > 0:
        print(a,"positive")
    else:
        if a < 0:
            print(a,"negative")
        else:
            print(a,"neutral")
positive()


### switch case using function
# alphabet or consonant
a: A
vowel
def switch():
    a = input("a: ")

    match a:
        case 'a' | 'A':
            print("vowel")
        case 'e' | 'E':
            print("vowel")
        case 'i' | 'I':
            print("vowel")
        case 'o' | 'O':
            print("vowel")
        case 'u' | 'U':
            print("vowel")
        case _:
            print("consonant")
switch()
    

#emplayee designation based on enplayee code
def employee():
    a = int(input("a: "))

    match a:
        case 101:
            print("managr")
        case 102:
            print("team leader")
        case 103:
            print("software developer")
        case 104:
            print("tester")
        case 105:
            print("Hr")
        case _:
            print("invalid employee code")
employee()

### while Loops
#1. natural numbers
n: 5
0
1
2
3
4
5
def natural():
    n = int(input("n: ")) #10
    i = 0
    while i <= n:
        print(i)
        i = i + 1
natural()

#10. reverse s number
n: 5
5
4
3
2
1
0
def reverse():
    n = int(input("n: ")) #5
    i = 0
    while i <= n:
        print(n)
        n = n - 1
reverse()

### For Loops

#8. 1^2  + 2^2 + 3^2 + ... + n^2

def square():
    n = int(input("n: ")) #5
    b = 0
    for i in range(1, n+1):
        a = i * i
        b = b + a
    print(b)
square()


#15. Armstrong or not #153

def armstrong():
    n = int(input("n: "))
    f = n
    u = n
    c = 0
    for i in range(n):
        n = n // 10
        c = c + 1
        if n == 0:
            break
    h = 0
    for i in range(f):
        b = f % 10
        y = pow(b,c)
        h = y + h
        f = f // 10
        if f == 0:
            break
    if h == u:
        print(h, "is armstrong")
    else:
        print(u, "is not armstrong")
armstrong()      


###Pattern using function
#while loop
#1.
n: 5
1
12
123
1234
12345
def loop1():
    n = int(input("n: "))
    i = 1
    while i <= n:
        j = 1
        while j <=i:
            print(j, end ="")
            j = j + 1
        i = i + 1
        print()
loop1()
##for loop
#2.
n: 5
54321
4321
321
21
1

def loop():
    n = int(input("n: ")) 
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j, end = "")
        print()
loop()

### arrays using function

#2. sum of array


def sumofarray():
    n = int(input("n: "))
    x = []
    for i in range(n):
        a = int(input("a: "))
        x.append(a)
    print(x)
    
    v = 0
    for i in range(n):
         v = x[i] + v
    print(v)
sumofarray()     


# 3. avg of array elements

def avg():
    n = int(input("n: "))
    x = []
    for i in range(n):
        a = int(input("a: "))
        x.append(a)
    print(x)

    a = 0
    avg = n
    for i in range(n):
        a = x[i] + a
    v = a / avg
    print(int(v))
avg()


#### Type 2 with argument & without return
def add(a,b):
    t = a + b
    print(t)
n = int(input("n: "))
n1 = int(input("n1: "))
add(n,n1)


#if loop / 4.smaller num between 2 nums

def smsller(a,b):
    if a > b:
        print(a, "is bigger")
    else:
        print(b, "is bigger")
n = int(input("a: "))
n1 = int(input("b: "))
smsller(n,n1)

#if else/ 5.eligible for vote or not

def vote(n):
    if n >= 18:
        print("elegible for vote")
    else:
        print("not elegible for vote")
n = int(input("n: "))
vote(n)

# ladder

def ladder(a,b,c):
    
    if a > b:
        if a > c:
            print(a,"A bigger") 
        else:
            print(c," C is bigger")
    else:
        if b > c:
            print(b,"B is bigger")
        else:
            print(c,"c is bigger")
a = int(input("a: ")) #20
b = int(input("b: ")) #10
c = int(input("c: ")) #15            
ladder(a,b,c)


#loops while loops / 1.natural numbers

def natural(n):
    i = 0
    while i <= n:
        print(i)
        i = i + 1
n = int(input("n: ")) #10
natural(n)


##def avg(n):
    
    x = []
    for i in range(n):
        a = int(input("a: "))
        x.append(a)
    print(x)

    a = 0
    avg = n
    for i in range(n):
        a = x[i] + a
    v = a / avg
    print(int(v))
n = int(input("n: "))
avg(n)

#### Type 3. without argument & with return
def division():
    n = int(input("n: "))
    if n % 5 == 0:
        return "it is divisible"
h = division()
print(h)

#loop // 11.print each charecters in string [m]  - m a d h u

def string():
    n = str(input("n: "))
    L = len(n)
    for i in range(0, L+1):
        return n[i]
h = string()
print(h)


# 14. palindrome or not:
def palindrome():
    n = int(input("n: ")) # 121
    b = 0
    h = n
    for i in range(n):
        a = n % 10
        b = b * 10 + a
        n = n // 10
        if n == 0:
            break
    if h == b:
        return "its a palindrome"
    else:
        return "not palindrome"
print(palindrome())


#### Type 4. with argument & with return
#if statement
#1. divisible by 5
def division(n):
    if n % 5 == 0:
        return "it is divisible"
    else:
        return "not divisible"
n = int(input("n: "))
print(division(n))

#if ladder

def ladder(a,b,c):
    if a > b:
        if a > c:
            return "A bigger" 
        else:
            return "C bigger"
    else:
        if b > c:
            return "B bigger"
        else:
            return "C bigger"
a = int(input("a: ")) #20
b = int(input("b: ")) #10
c = int(input("c: ")) #15
print(ladder(a,b,c))

#switch
#2. employeee dedignation based on code
def switch(a):
    match a:
        case 'a' | 'A':
            return "vowel"
        case 'e' | 'E':
            return "vowel"
        case 'i' | 'I':
            return "vowel"
        case 'o' | 'O':
            return "vowel"
        case 'u' | 'U':
            return "vowel"
        case _:
            return "consonant"
a = input("a: ")
print(switch(a))

#loop
#4. neon number  (ex.n = 9 ->81 ->8 + 1 = 9)
import math
def neon(n):
    c = 1
    k = n
    for i in range(n):
        a = n * n
        b = a // 10
        c = c + b
        n = n // 10
    
        if n == 0:
            break

    if k == c:
        return "neon number"
    else:
        return "not neon number"
    
n = int(input("n: "))
print(neon(n))


#arrays
5. sum of even numbers in array

def even(n):
    x = []
    for i in range(n):
        a = int(input("a: "))
        x.append(a)
    c = []
    u = 0
    for i in range(n):
        if x[i] % 2 == 0:
            c.append(x[i])
            u = u + 1
    g = 0
    for i in range(u):
        g = g + c[i]
    return g
n = int(input("n: "))
even(n)

'''














































