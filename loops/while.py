'''
###NATURAL NUMBERS TILL N
n = int(input("n:"))
i = 1
while i <= n:
    print(i)
    n = i + 1
o
###EVEN NUMBERS TILL N
n = int(input("n: "))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i = i + 1


###ODD NUMBERS TILL N
n = int(input("n: "))
i = 1
while i <= n:
    if i % 2 != 0:
        print(i)
    i = i + 1

###number from 1 =10 to -1
i = -1
n = -5
while i >= n:
    print(n)
    n = n + 1

###NATURAL NUMBERS TILL N reverse
n = int(input("n:"))
i = 1
while i <= n:
    print(n)
    n = n - 1


###ODD NUMBERS TILL N
n = int(input("n: "))
i = 1
while i <= n:
    if n % 2 != 0:
        print(n)
    n = n - 1

### SUM IF NATURAL NUMBERS

n = int(input("n:"))
i = 1
s = 0
while i <= n:
    s = s + i
    i = i + 1
print(s)


### SUM OF ODD NUMBERS

n = int(input("n: "))
i = 1
s = 0

while i <= n:
    if i % 2 != 0:
        s = s + i
    i = i + 1
print(s)


### SUM OF Even NUMBERS

n = int(input("n: "))
i = 1
s = 0

while i <= n:
    if i % 2 == 0:
        s = s + i
    i = i + 1
print(s)


### narural number squre

import math
n = int(input("n: "))
i = 1
s = 0

while i <= n:
    x = pow(i,2)
    s = s + x
    i = i + 1
print(s)

### odd squre

import math
n = int(input("n: "))
i = 1
s = 0

while i <= n:
    if i % 2 != 0:
        x = pow(i,2)
        s = s + x
    i = i + 1
print(s)

### even squre

n = int(input("n: "))
i = 1
s = 0

while i <= n:
    if i % 2 == 0:
        x = i**2
        s = s + x
    i = i + 1
print(s)


###natural number cube 3:

i = 1
s = 0
n =5

while i <= n:
    u = i ** 3
    s = s + u
    i += 1
print(s)


import math
n = int(input("n: "))

i = 1
s = 0
while i <= n:
    x = pow(i,3)
    s = s + x
    i = i+1
print(s)

'''
###natural number 1 / 2 squre:

import math
n = int(input("n: "))

i = 1
s = 0

while i <= n:
    x = 1 / pow(i,2)
    s = s + x
    i = i+1
print(s)

'''


### Odd till n [1 /1^2]:

import math
n = int(input("n: "))

i = 1
s = 0

while i <= n:
    if i % 2 != 0:
        x = 1 / pow(i,2)
        s = s + x
    i = i+1
print(s)


### Even till n [1 /1^2]:

import math
n = int(input("n: "))

i = 1
s = 0

while i <= n:
    if i % 2 == 0:
        x = 1 / pow(i,2)
        s = s + x
    i = i+1
print(s)




### Find factorial value of n  
n = int(input("Enter n: ")) #1*2*3*4*5

i = 1
s = 1

while i <= n:
    s = s * i
    i = i + 1
print(s)



### 19.Find factorial n!

n = int(input("Enter n: "))
i = 1
s = 1
f = 0
while i <= n:
    s = s * i
    f = f + s
    i = i + 1
print(f)



### 20. Find odd factorial n!

n = int(input("Enter n: "))
i = 1
s = 1
f = 0
while i <= n:
    s = s * i
    if i % 2 !=0:
        f = f + s
    i = i + 1
print(f)


### 21.Find Even factorial n!

n = int(input("Enter n: "))
i = 1
s = 1
f = 0
while i <= n:
    s = s * i
    if i % 2 ==0:
        
        f = f + s
    i = i + 1
print(f)





### 22.Find factorial value of 1/n! 
n = int(input("n: "))
i = 1
s = 1
f = 0
while i <= n:
    s = s * i
    y = 1 / s 
    f = f + y
    i = i + 1
print(f)


### 25. Print current and previous ODD number till n

n = int(input("n: "))

i = 1
current = 0
pre = 0

while i <= n:
    
    if i % 2 != 0:
        current = i 
        pre = current - 2
        print(current, " ", pre )
    i = i + 1




### 26 . Print current and previous Even number till n

n = int(input("n: "))

i = 1
current = 0
pre = 0

while i <= n:
    
    if i % 2 == 0:
        current = i 
        pre = current - 2
        print(current, " ", pre )
    i = i + 1


### 27. N'th Multiplication table till m

n = int(input("N'th Multiplication Table: "))
m = int(input("M: "))

i = 1

while i <= m:

    s = i * n
    print(i,"x",n,"=",s)
    
    i = i + 1


### 28. reverse S number
n = int(input("s: "))
s = 0
while n > 0:
    f = n % 10
    s = s * 10 + f
    n = n // 10
print(s)

### 29 Print each charector in string

s = str(input("s: "))
length = len(s) - 1
i = 0

while i <= length:
    print(s[i])
    i = i + 1


### 30. reverse string

s = str(input("s: "))
length = len(s) - 1

i = 0
m = ""
while i <= length:
    m = m + s[length]
    length = length - 1
print(m)



###31. Palindrome or not. i/p #12321

p = int(input("p: "))
s = 0
t = p

while p > 0:
    
    f = p % 10
    s = s * 10 + f
    p = p // 10
if t == s:
    print(s, "is a palindrome number")
else:
    print(s, "is not palindrome number")


### 32.armstrong or not
import math
a = int(input("a: "))
c = 0
s = 0
b = a
m = a

while a > 0: # a = 153
    a = a // 10 #15
    c = c + 1
    
while b > 0:
    
    r = b % 10
    h = pow(r,c)
    s = s + h
    b = b // 10
print(s)

if s == m:
    print(s, "is a armstrrong")
else:
    print(s, "not armstrrong")

###33.adam or not

import math
a = int(input("a: "))
c = 0
t = a
p = pow(a, 2)

while p > 0:
    b = p % 10
    c = c * 10 + b
    p = p // 10

x =int(math.sqrt(c))

c = 0
while x > 0:
    
    y = x % 10
    c = c * 10 + y
    x = x // 10
if c == t:
    print(t, "is a adam")
else:
    print(t, "is not adam")



###34.Perfect number or not


a = int(input("a: ")) # a = 6
u = a
i = 1
s = 0

while i < a:
    if a % i == 0:
        s = s + i
    i = i + 1
    
if u == s:
    print(u, "is a perfect number")
else:
    print(u, "is not perfect number")
        
 

### prime number or not
a = int(input("a: "))

c = 0
i = 1

while i <= a:
    if a % i == 0:
        c = c + 1
    i = i + 1
if c == 2:
    print(a, "is prime number")

else:
    print(a, "not prime number")



### 48. fibonacci series
a = int(input("a: ")) ## 8
i = 1
f = 0
s = 1
t = 0
while i <= a:
    print(f,end=",")
    t = f + s 
    f = s
    s = t
    i = i + 1


### 49. pell series
a = int(input("a: ")) 
i = 1
f = 0
s = 1
t = 0
while i <= a:
    print(f, end =",")
    t = f + 2 * s
    f = s
    s = t
    i = i + 1


### 51. Count number of digits
a = int(input("a: ")) #1234  o/p = 4
c = 0
while a > 0:
    c = c + 1
    a = a // 10
print(c)



### 52. sum of digits
a = int(input("a: ")) #1234  o/p = 4
g = 0
d = 0
while a > 0:
    d = a % 10
    g = g + d
    a = a // 10
    
print(g)


### 53. sum of digits
a = int(input("a: ")) #1234  o/p = 4
g = 1
d = 0
while a > 0:
    d = a % 10
    g = g * d
    a = a // 10
print(g)



### 54. swap first and last digit
a = int(input("a: ")) #1234  o/p = 4
c = 0
v = a
g = 0
while a > 0:
    c = c + 1
    a = a // 10
b =  v // pow(10,c - 1) #first value
d = v % 10 #last value



x = v % pow(10, c -1)
y = x // 10


g = d * pow(10, c - 1) + y * 10 + b  
print(g)



###55. positibve negtive nutral count

n = int(input("n: "))
i = 1
c = 0
c1 = 0
c2 = 0
while i <= n:
    a = int(input("a: "))

    if a > 0:
        c = c + 1

    if a < 0:
        c1 = c1 + 1
    
    if a == 0:
        c2 = c2 + 1
    i = i + 1   

print(c, "possitive")
print(c1, "negative")
print(c2, "neutral")



###56. Biggest number of n value
n = int(input("how many numbers u want?: "))
i = 1
mx = 0
while i <= n:
    a = int(input("Give numbers: "))
    if a > mx:
        mx = a
    i = i + 1   

print(mx, "is bigger")


###57. smallest number of n value
n = int(input("how many numbers u want?: "))
i = 1
mi = int(input("give numbers: "))
while i <= n:
    a = int(input("Give numbers: "))
    if a < mi:
        mi = a
    i = i + 1   

print(mi, "is smaller")


###58. sum of n value
n = int(input("how many numbers u want?: "))
i = 1
s = 0
while i <= n:
    a = int(input("Give numbers: "))
    s = a + s
    i = i + 1   

print(s, "is the sum of given n")



###59. odd of n value
n = int(input("how many numbers u want?: "))
i = 1
s = 0
while i <= n:
    a = int(input("Give numbers: "))
    if a % 2 != 0:
        s = a + s
    i = i + 1   

print(s, "is the sum of given n")


###60. even of n value
n = int(input("how many numbers u want?: "))
i = 1
s = 0
while i <= n:
    a = int(input("Give numbers: "))
    if a % 2 == 0:
        s = a + s
    i = i + 1   

print(s, "is the sum of given n")


###61.sum and avg
n = int(input("how many numbers u want?: "))
i = 1
s = 0
avg = 0
while i <= n:
    a = int(input("Give numbers: "))
    s = a + s
    avg = s / n
    
    i = i + 1   

print(int(avg), "is the avg of given n")

###62.HCF

a = int(input("a: ")) #12
b = int(input("b: ")) #18
2
i = 1

c1 = 0

while i <= a:
    if a % i == 0 and b % i == 0: #12
        c1 = i
    i = i + 1
print(c1)


###63.LCM

a = int(input("a: ")) #6
b = int(input("b: ")) #13

i = 1

c1 = 0
  
while i <= a:
    if a % i == 0 and b % i == 0:
        c1 = i
    r = a * b / c1
    i = i + 1
print(r)    


###64. prime and adam or not
import math
a = int(input("Give number for check adam and prime or not: "))
p = pow(a,2)
j = a
c = 0
while p > 0:
    b = p % 10 # 169 -> 961
    c = c * 10 + b
    p = p // 10
sr = int(math.sqrt(c))   


c = 0
while sr > 0:
    x = sr % 10
    c = c * 10 + x
    sr = sr // 10
print(c)
m = a
c1 = 0
i = 1
while i <= m:
    if m % i == 0:
        c1 = c1 + 1
    i = i + 1

if c == j and c1 == 2:
    print(a, "is adam and prime number")
else:
    print(m, "is not adam and prime number")


### 65.automorphic or not

import math
a = int(input("a: "))
c = 0
p = pow(a, 2)
d = 0
u = a
while a > 0:
    b = a % 10
    c = c + 1
    a = a // 10
d = p % pow(10, c)

if u == d:
    print(u, "is a automorphic")
else:
    print(u, "is not automorphic")



###66. a = 0, b = 0, c = 0
n = int(input("n:" ))
i = 0
a = 0
b = 0
c = 0

while i <= n:
    print(a,b,c)
    c = c + 1
    if c == 10:
        c = 0
        b = b + 1
    if b == 10:
        b = 0
        a = a + 1
    i = i + 1
    


### 35. convert decimal to binary # a = 12

a = int(input("a: "))
c = 0
i = 1
while a > 0:
    b = a % 2 
    f = b * i 
    c = c + f
    i = i * 10
    a = a // 2
    
print(c)


### 36. convert decimal to octal # a = 12

a = int(input("a: "))
c = 0
i = 1
while a > 0:
    b = a % 8
    f = b * i
    c = c + f
    i = i * 10
    a = a // 8
print(c)


###37. decimal to hexadecimal

a = int(input("a: ")) #26
v = ""

while a > 0:
    b = a % 16
    if b == 10:
        v = "a" + v
    elif b == 11:
        v = "b" + v
    elif b == 12:
        v = "c" + v
    elif b == 13:
        v = "d" + v
    elif b == 14:
        v = "e" + v
    elif b == 15:
        v = "f" + v
    elif b == 16:
        v = "f" + v
    else:
        v = str(b) + v
    a = a // 16
    
print(v)

### 38. binary to desimal

import math
a = int(input("a: "))
c = 0
i = 0

while a > 0:
    b = a % 10
    x = b * pow(2, i)
    c = c + x
    i = i + 1
    a = a // 10
print(c)


   
###39. binary to octal

import math
a = int(input("a: "))
c = 0
i = 1
while a > 0:
    x = pow(i, 2)
    b = a % 8
    c = c + b
    a = a // 8
print(c)


###40. binary to hexadecimal
import math
a = int(input("a: ")) #1100
v = ""
c = 0
i = 1
i = 0

while a > 0:
    b = a % 10
    x = b * pow(2, i)
    c = c + x
    i = i + 1
    a = a // 10
    
while c > 0:
    b = c % 16
    if b == 10:
        v = "a" + v
    elif b == 11:
        v = "b" + v
    elif b == 12:
        v = "c" + v
    elif b == 13:
        v = "d" + v
    elif b == 14:
        v = "e" + v
    elif b == 15:
        v = "f" + v
    elif b == 16:
        v = "f" + v
    else:
        v = str(b) + v
    c = c // 16
    
print(v)

###41. octal to decimal

import math
a = int(input("a: "))
c = 0
i = 0

while a > 0:
    b = a % 10
    x = b * pow(8, i)
    c = c + x
    i = i + 1
    a = a // 10
print(c)


### 42.octal to binary

# now octal to decimal
import math
a = int(input("a: ")) #12
c = 0
i = 0
c1 = 0
while a > 0:
    b = a % 10
    x = b * pow(8, i)
    c = c + x
    i = i + 1
    a = a // 10

# now decimal to binary
i = 1
while c > 0:
    b = c % 2 
    f = b * i 
    c1 = c1 + f
    i = i * 10
    c = c // 2
    
print(c1)    


### 43. octal to hexadesimal

# now octal to decimal
import math
a = int(input("a: ")) #12
c = 0
i = 0
v = ""

while a > 0:
    b = a % 10
    x = b * pow(8, i)
    c = c + x
    i = i + 1
    a = a // 10


while c > 0:
    b = c % 16
    if b == 10:
        v = "a" + v
    elif b == 11:
        v = "b" + v
    elif b == 12:
        v = "c" + v
    elif b == 13:
        v = "d" + v
    elif b == 14:
        v = "e" + v
    elif b == 15:
        v = "f" + v
    elif b == 16:
        v = "f" + v
    else:
        v = str(b) + v
    c = c // 16
    
print(v)

### 44.hexadecimal to desimal
import math
a = input("a: ") #1a
c = 0
i = 0
v = 0
l = len(a) - 1
y = 0
while l >= 0:
    if a[l] == "a":
        v = 10
    elif a[l] == "b":
        v = 11
    elif a[l] == "c":
        v = 12
    elif a[l] == "d":
        v = 13
    elif a[l] == "e":
        v = 14
    elif a[l] == "f":
        v = 15
    elif a[l] == "g":
        v = 16
    else:
        v = int(a[l])
    x = v * pow(16, i)
    y = y + x
    i = i + 1
    l = l - 1
print(y)



### 45.hexadecimal to Binary
import math
a = input("a: ") #1a
c = 0
i = 0
v = 0
l = len(a) - 1
y = 0

while l >= 0:
    if a[l] == "a":
        v = 10
    elif a[l] == "b":
        v = 11
    elif a[l] == "c":
        v = 12
    elif a[l] == "d":
        v = 13
    elif a[l] == "e":
        v = 14
    elif a[l] == "f":
        v = 15
    elif a[l] == "g":
        v = 16
    else:
        v = int(a[l])
    x = v * pow(16, i)
    y = y + x
    i = i + 1
    l = l - 1
    
# now decimal to binary
i = 1
c1 = 0
while y > 0:
    b = y % 2 
    f = b * i 
    c1 = c1 + f
    i = i * 10
    y = y // 2 
print(c1) 


### 46.hexadecimal to octal
import math
a = input("a: ") #1a
c = 0
i = 0
v = 0
l = len(a) - 1
y = 0

while l >= 0:
    if a[l] == "a":
        v = 10
    elif a[l] == "b":
        v = 11
    elif a[l] == "c":
        v = 12
    elif a[l] == "d":
        v = 13
    elif a[l] == "e":
        v = 14
    elif a[l] == "f":
        v = 15
    elif a[l] == "g":
        v = 16
    else:
        v = int(a[l])
    x = v * pow(16, i)
    y = y + x
    i = i + 1
    l = l - 1
#now convert decimal to octal
c1 = 0
i = 1
while y > 0:
    b = y % 8
    f = b * i
    c1 = c1 + f
    i = i * 10
    y = y // 8
print(c1)
'''













    
