'''
### 1. Natural numbers till n

n = int(input("n: "))
for i in range(1, n):
    print(i)


### 2. even numbers till n

n = int(input("n: "))
for i in range(1, n):
    if i % 2 ==0:
        print(i)
        

### 3 odd numbers till n

n = int(input("n: "))
for i in range(1, n):
    if i % 2 !=0:
        print(i)


### 4. -10 to -1

for i in range(-10, 0, 1):
    print(i)
    

### 5. reverse n

n = int(input("n: "))
for i in range(10, 0, -1):
    print(i)


### 6.even n in reverse

n = int(input("n: "))
for i in range(n, 0, -1):
    if i % 2 ==0:
        print(i)

        
### 7.odd n in reverse

n = int(input("n: "))
for i in range(n, 0, -1):
    if i % 2 !=0:
        print(i)


### 8.sum of n
s = 0
n = int(input("n: ")) # 10
for i in range(0, n):
    s = s + i
print(s)



### 9.sum of odd till n
s = 0
n = int(input("n: ")) # 10
for i in range(0, n):
    if i % 2 != 0:
        s = s + i
print(s)


### 10.sum of even till n
s = 0
n = int(input("n: ")) # 10
for i in range(0, n):
    if i % 2 == 0:
        s = s + i
print(s)


###11. n^2
s = 0
n = int(input("n: "))
for i in range(1, n):
    s = i * i + s
print(s)


### 12. odd n^2 # ip 9
s = 0
n = int(input("n: "))
for i in range(1, n):
    if i % 2 !=0:
        s = i * i + s
print(s)


### 13. even n^2 # ip 9
s = 0
n = int(input("n: "))
for i in range(1, n):
    if i % 2 ==0:
        s = i * i + s
print(s)


###14. sum n^3
import math
s = 0
n = int(input("n: "))
for i in range(1, n):
    s = pow(i, 3) + s
print(s)


###15. sum 1 / n^2
import math
s = 0
n = int(input("n: "))
for i in range(1, n):
    s = 1 / pow(i, 2) + s
print(s)



###16. odd sum 1 / n^2
import math
s = 0
n = int(input("n: "))
for i in range(1, n):
    if i % 2 != 0:
        s = 1 / pow(i, 2) + s
print(s)

###17. even sum 1 / n^2
import math
s = 0
n = int(input("n: "))
for i in range(1, n):
    if i % 2 == 0:
        s = 1 / pow(i, 2) + s
print(s)


###18. n!
s = 1
n = int(input("n: "))
for i in range(1, n + 1):
    s = s * i
print(s)

###19. sum Factorial of n
s = 1
c = 0
n = int(input("n: "))
for i in range(1, n + 1):
    s = s * i
    c = c + s
print(c)


###20. sum of odd n!
s = 1
c = 0
n = int(input("n: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        s = s * i
        c = c + s
print(c)


###21. sum of even n!
s = 1
c = 0
n = int(input("n: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        s = s * i
        c = c + s
print(c)


###22. sum 1 / n!
s = 1
c = 0
n = int(input("n: "))
for i in range(1, n + 1):
    s = 1 / s * i
    c = c + s
print(c)


###23. sum of 1 / odd n!
s = 1
c = 0
n = int(input("n: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        s = 1 / s * i
        c = c + s
print(c)


###24. sum of 1 / even n!
s = 1
c = 0
n = int(input("n: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        s = 1 / s * i
        c = c + s
print(int(c))



###25. current and previous odd num till n
p = 0
n = int(input("n: "))
for i in range(1, n):
    if i % 2 != 0:
        p = i - 2
        print(i ,"current"," ",p, "previous")
        

###26. current and previous odd num till n
n = int(input("n: "))
for i in range(1, n):
    if i % 2 == 0:
        p = i - 2
        print(i ,"current"," ",p, "previous")

###27. Nth multiplication table till m

n = int(input("n: "))
m = int(input("m: "))
for i in range(1, m + 1):
    t = i * n
    print(i,"*",n,"=",t)


###28. reverse s number

b = 0
s = int(input("s: "))
for i in range(s):
    a = s % 10
    b = b * 10 + a
    s = s // 10
    if s == 0:
        break
print(b)


##29. print each charecters in string

s = str(input("s: "))
l = len(s) -1
for i in range(0,l + 1):
    print(s[i], end = ",")


##30. reverse a string

s = str(input("s: "))
l = len(s) -1
for i in range(l, -1, -1):
    print(s[i])



### 31 palindrome or not

n = int(input("n: "))
c = n
b = 0
for i in range(n):
    a = n % 10
    b = b * 10 + a
    n = n // 10
    if n == 0:
        break

if c == b:
    print(c, "is palinrome")
else:
    print(c, "is not palindrome")


### 32. armstrong or not
import math
n = int(input("n: ")) # 153
c = 0
s = 0
a = n
v = n
for i in range(n):
    n = n // 10
    c = c + 1
    if n == 0:
        break
    
for i in range(a):   
    r = a % 10
    h = pow(r, c)
    s = s + h
    a = a // 10
    if a == 0:
        break
if s == v:
    print(v, "is a armstrong")
else:
    print(v, "is not armstrong")


### 33. adamm or not
import math
n = int(input("n: "))
p = n
b = 0
x = pow(n, 2)
for i in range(x):
    a = x % 10
    b = b * 10 + a
    x = x // 10
    if x ==0:
        break

s = int(math.sqrt(b))
y = 0
for i in range(s):
    a = s % 10
    y = y * 10 + a
    s = s // 10
    if s == 0:
        break
    
if p == y:
    print(p ,"is adam")
else:
    print(p, "is not adam")


### 34. perfect number or not
import math
n = int(input("n: "))
b = 0
c = n
for i in range(1, n):
    if n % i == 0:
        b = b + i
if b == c:
    print(c, "is perfect number")
else:
    print(c, "is not perfect number")
    

### 47. prime number or not
import math
n = int(input("n: "))
b = 0
c = n
for i in range(1, n + 1):
    if n % i == 0:
        b = b + 1
if b == 2:
    print(c, "is prime number")
else:
    print(c, "is not prime number")


### 48. fibonacci series

n = int(input("n: "))
f = 0
s = 1
c = n
for i in range(1, n + 1):
    print(f, end = ",")
    t = f + s
    f = s
    s = t

## 49. pell series

p = int(input("p: "))
f = 0
s = 1

for i in range(0, p):
    print(f)
    t = f + 2 * s
    f = s
    s = t


## 51. count no of digits of n # 1234

n = int(input("n :"))
c = 0
for i in range(n):
    
    n = n // 10
    c = c + 1
    if n == 0:
        break
print(c)


## 52. count sum of digits of n # 1234

n = int(input("n :"))
c = 0
s = 0
for i in range(n):
    
    n = n // 10
    c = c + 1
    s = c + s
    if n == 0:
        break
print(s)


## 53. product of digits of n # 1234

n = int(input("n :"))
c = 0
s = 1
for i in range(n):
    
    n = n // 10
    c = c + 1
    s = c * s
    if n == 0:
        break
print(s)


## 54 swapping first and last digits of a number
n = int(input("n: "))
f = 0
k = n
c = 0
for i in range(n):
    
    n = n // 10
    c = c + 1
    if n == 0:
        break
f = k // pow(10, c - 1)
l = k % 10

x = k % pow(10, c - 1)
m = x // 10

print(f,l,m)
swapping = (l * pow(10, c - 1)) +( m * 10) + f
print(swapping)



## 55. find positive, negative, zero for n time value

n = int(input("n:" ))
p = 0
n1 = 0
z = 0
for i in range(n):
    e = int (input("e: "))
    if e > 0:
        p = p + 1
    if e < 0:
        n1 = n1 + 1
    if e == 0:
        z = z + 1
print(p, "possitive")
print(n1, "negative")
print(z, "neutral")

   

## 56. biggest number for n time's value

n = int(input("n: "))

h = 0
for i in range(n):
    e = int(input("e: "))
    if e > h:
        h = e
print(h, "is bigger")



## 57. smallest number for n time's value

n = int(input("n: "))

h = 0
for i in range(n):
    e = int(input("e: "))
    if e < h:
        h = e
print(h, "is smaller")


## 58. sum of numbers n time's value

n = int(input("n: "))

t = 0
for i in range(n):
    e = int(input("e: "))
    t = e + t
print(t, "is the sum")



## 59. sum of odd n time's value

n = int(input("n: "))

t = 0
for i in range(n):
    e = int(input("e: "))
    if e % 2 != 0:
        t = e + t
print(t, "is the odd sum")


## 60. sum of odd n time's value

n = int(input("n: "))

t = 0
for i in range(n):
    e = int(input("e: "))
    if e % 2 == 0:
        t = e + t
print(t, "is the even sum")


## 61. sum and avg n time's value

n = int(input("n: "))

t = 0
for i in range(n):
    e = int(input("e: "))
    t = e + t
    a = t / n

print(t, "sum", " ", int(a), "is the avg")



##62. HCF for 2 numbers

a = int(input("a: "))
b = int(input("b: "))
c = 0

for i in range(1,a+1):
    if a % i == 0 and b % i ==0:
        c = i
print(c)



##63. LCM for 2 numbers

a = int(input("a: "))
b = int(input("b: "))
c = 0
for i in range(1,a+1):
    if a % i == 0 and b % i ==0:
        c = i
x = a * b
y = x / c
print(int(y))



## 64. Prime adam or not
import math
n  = int(input("n: "))
a = 0
u = n
for i in range(1, n + 1):
    if n % i == 0:
        a = a + 1

x = pow(n, 2)
s = 0
for i in range(x):

    b = x % 10
    s = s * 10 + b
    x = x // 10
    if x == 0:
        break

y = int(math.sqrt(s))
h = 0
for i in range(y):
    g = y % 10
    h = h * 10 + g
    y = y // 10
    if y == 0:
        break
   
if a == 2 and h == u:
    print(u, "is adam and prime number")
else:
    print(u, "is not adam and prime number")

## 65. autophormic or not
import math
n = int(input("n: "))
c = 0
p = pow(n, 2)
y = n
for i in range(n):
    a = n % 10
    c = c + 1
    n = n // 10
    if n == 0:
        break

x = p % pow(10, c)

if y == x:
    print(y, "is autophormic")
else:
    print(y, "is not autophormic")


## 66. a = 0, b =0, c = 0
n = int(input("n: "))
a = 0
b = 0
c = 0

for i in range(0, n+1):
    print(a,b,c)
    c = c + 1

    if c == 10:
        c = 0
        b = b + 1
    if b == 10:
        b = 0
        a = a + 1
  


### NUMBER CONVERSION

## desimal - 10

## binary - 2

## oactl - 8

## hexadecimal

#35. Decimal to binary

n = int(input("n: "))
f = 0
k = 1
s = 0
for i in range(0, n + 1):
    a = n % 2
    f = a * k
    s = s + f
    k = k * 10
    n = n // 2 
    
    if n == 0:
        break
print(s)


#36. Decimal to octal

n = int(input("n: "))
f = 0
k = 1
s = 0
for i in range(0, n + 1):
    a = n % 8
    f = a * k
    s = s + f
    k = k * 10
    n = n // 8
    
    if n == 0:
        break
print(s)


## 37. decimal to hexadecimal

n = int(input("a: ")) #26
h = ""
for i in range(n):
    a = n % 16
    if a == 10:
        h = "a" + h
    elif a == 11:
        h = "b" + h
    elif a == 12:
        h = "c" + h
    elif a == 13:
        h = "d" + h
    elif a == 14:
        h = "e" + h
    elif a == 15:
        h = "f" + h
    elif a == 16:
        h = "g" + h
    elif n == 0:
        break
    else:
        h = str(a) + h
    n = n // 16
print(h)


### 38. binary to decimal

n = int(input("n: "))
f = 0
k = 1
s = 0
for i in range(0, n + 1):
    a = n % 10
    f = a * k
    s = s + f
    k = k * 2
    n = n // 10
    
    if n == 0:
        break
print(s)


### 39. binary to octal

# first we have to change binary to decimal
n = int(input("n: "))
f = 0
k = 1
s = 0
for i in range(0, n + 1):
    a = n % 10
    f = a * k
    s = s + f
    k = k * 2
    n = n // 10
    
    if n == 0:
        break
    
# decimal to octal
c = 0
k = 1
for i in range(0, s + 1):
    a = s % 8
    f = a * k
    c = c + f
    k = k * 10
    s = s // 8
    
    if s == 0:
        break
print(c)


### 40. binary to hexzdecimal

# first we have to change from binary to decimal


n = int(input("n: "))

f = 0
s = 0
k = 1
for i in range(n+1):

    a = n % 10
    f = a * k
    s = s + f
    k = k * 2
    n = n // 10

    if n == 0:
        break
print(s)


#deciml to hexadecimal

h = ""
for i in range(s):

    b = s % 16
    if b == 10:
        h = "a" + h
    elif b == 11:
        h = "b" + h
    elif b == 12:
        h = "c" + h
    elif b == 13:
        h = "d" + h
    elif b == 14:
        h = "e" + h
    elif b == 15:
        h = "f" + h
    else:
        h = str(b) + h
    s = s // 16
    if s == 0:
        break
print(h)



### 41. octal to decimal

n = int(input("n: "))

f = 0
s = 0
k = 1
for i in range(n+1):

    a = n % 10
    f = a * k
    s = s + f
    k = k * 8
    n = n // 10

    if n == 0:
        break
print(s)


### 42. octal to binary

# octal to decimal
n = int(input("n: "))

f = 0
s = 0
k = 1
for i in range(n+1):

    a = n % 10
    f = a * k
    s = s + f
    k = k * 8
    n = n // 10

    if n == 0:
        break
c = 0
k = 1
# decimal to binary
for i in range(s+1):

    a = s % 2
    f = a * k
    c = c + f
    k = k * 10
    s = s // 2

    if s == 0:
        break
print(c)

### 43. octal to hexadecimal

# octal to decimal
n = int(input("n: "))
f = 0
k = 1
s = 0
for i in range(n):
    a = n % 10
    f = a * k
    s = s + f
    k = k * 8
    n = n // 10

    if n == 0:
        break

# decimal to hexadecimal

h = ""
for i in range(s+1):

    b = s % 16
    if b == 10:
        h = "a" + h
    elif b == 11:
        h = "b" + h
    elif b == 12:
        h = "c" + h
    elif b == 13:
        h = "d" + h
    elif b == 14:
        h = "e" + h
    elif b == 15:
        h = "f" + h
    else:
        b = str(b) + h
    s = s // 16

print(h)

## 44. hexadecimal to decimal

b = str(input("b: "))
L = len(b) - 1
h = 0
x = 0
y = 0
k = 0
for i in range(L, -1, -1):


    if b[i] == "a":
        h = 10
    elif b[i] == "b":
        h = 11
    elif b[i] == "c":
        h = 12
    elif b[i] == "d" :
        h = 13
    elif b[i] == "e":
        h = 14
    elif b[i] == "f":
        h = 15
    else:
        h = int(b[i])
    x = h * pow(16, k)
    y = y + x
    k = k + 1
print(y)


##45. hexadecimal to binary

b = str(input("b: "))
L = len(b) - 1
h = 0
k = 0
x = 0
y = 0
for i in range(L, -1, -1):

    if b[i] == "a":
        h = 10
    elif b[i] == "b":
        h = 11
    elif b[i] == "c":
        h = 12
    elif b[i] == "d" :
        h = 13
    elif b[i] == "e":
        h = 14
    elif b[i] == "f":
        h = 15
    else:
        h = int(b[i])
    x = h * pow(16, k)
    y = y + x
    k = k + 1
print(y)

#decimal to binary

f = 0
r = 1
s = 0
for i in range(y):
    a = y % 2
    f = a * r
    s = s + f
    r = r * 10
    y = y // 2

print(s) 


## 46. Hexadecimal to actal

b = str(input("b: "))
L = len(b) - 1
h = 0
k = 0
x = 0
y = 0
for i in range(L, -1, -1):
    if b[i] == "a":
        h = 10
    elif b[i] == "b":
        h = 11
    elif b[i] == "c":
        h = 12
    elif b[i] == "d":
        h = 13
    elif b[i] == "e":
        h = 14
    elif b[i] == "f":
        h = 15
    else:
        h = int(b[i])
    x = h * pow(16, k)
    y = y + x
    k = k + 1
print(y)

# decimal to octal
f = 0
s = 0
r = 1
for i in range(y):
    a = y % 8
    f = a * r
    s = s + f
    r = r * 10
    y = y // 8
print(s)
'''















































        
