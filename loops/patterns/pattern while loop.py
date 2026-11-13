'''
1.n:5

1
12
123
1234
12345

n=int(input("enter n:"))
i=1
while(i<=n):
    j=1
    while(j<=i):
        print(j, end = "")
        j=j+1
    i=i+1
    print()

#2.n:5
5
54
543
5432
54321

n = int(input("n: ")) #5
k = n
i = 1
while i <= n:
    j = k
    while j >= n:
        print(j, end = "")
        j = j - 1
    print()
    n = n - 1

#3
1
21
321
4321
54321

n = int(input("n: "))

i = 1
while i <= n:
    j = i
    while j >= 1:
        print(j, end = "")
        j = j - 1
    i = i + 1
    print()

# 4
1
23
456
78910

n = int(input("n: ")) #4
i = 1
k = 1
while i <= n:
    j = 1
    while j <= i:
        print(k, end = "")
        j = j + 1
        k = k + 1
    print()
    i = i + 1

### 5
     1
    21
   321
  4321
 54321
 
n = int(input("5.n: ")) #5
i = 1
f = 1
while i <= n:
    j = 1
    while j <= n:
        print(" ", end = "")
        j = j + 1
    n -= 1
    
    k = f
    while k >= 1:
        print(k, end = "")
        k = k - 1
    f += 1
    print()

# 6
54321
4321
321
21
1

n = int(input("n: "))

i = 1
while i <= n:
    j = n
    while j >= 1:
        print(j, end = "")
        j = j - 1
    print()
    n = n - 1

# 7

10101
01010
10101
01010


n = int(input("n: ")) #5

i = 1
k = 1
while i < n:
    j = 1
    while j <= n:
        if k % 2 != 0:
            k = 1
        else:
            k = 0
        print(k, end= "")
        j = j + 1
        k = k + 1
    print()
    i = i + 1


#8

n: 5
1
10
101
1010
10101
n = int(input("n: "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        if j % 2 == 0:
            print(0, end= "")
        else:
            print(1, end= "")
    
        j = j + 1
    print()
    i = i + 1


# 9. n: 5
1
12
123
1234
12345
1234
123
12
1


n = int(input("9. n: ")) #5
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end ="")
        j = j + 1
    i = i+1
    print()

i = 1
n = n-1
while i <= n:
    j = 1
    while j <= n:
        print(j, end ="")
        j = j + 1
    n = n-1
    print()



# 10

1
22
333
4444
55555


n = int(input("10 n: ")) #5
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(i, end = "")
        j = j + 1
    print()
    i = i + 1

# 11
*
**
***
****
*****


n = int(input("11.n: ")) #5
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end =" ")
        j = j + 1
    print()
    i = i + 1
    

##12
12345
1234
123
12
1


n = int(input("12.n: ")) #5
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(j, end ="")
        j = j + 1
    print()
    n = n - 1


#13
54321
5432
543
54
5

n = int(input("13.n: ")) #5
i = 1
k = n
while i <= n:
    j = k
    while j >= i:
        print(j, end= "")
        j = j - 1
    print()
    i = i + 1

## 14
n: 5
    1
   12
  123
 1234
12345

n = int(input("14.n: ")) #5
i = 1
f = 1
while i <= n:
    k = f
    while k < n:
        print(" ", end="")
        k += 1
    f += 1
    j = 1
    while j <= i:
        print(j, end = "")
        j = j + 1
    i += 1
    print()

15. n: 5
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
n = int(input("15. n: "))
i = 1
while i <= n:
    q = i
    while q < n:
        print(" ", end="")
        q += 1
    k = 1
    while k <= i*2 - 1:
        if k == 1 or k == i*2 -1: 
            print("*", end="")
        else:
            print(" ", end="")
        k+=1
    i = i + 1  
    print()
n=5
y = n - 1
s1=1
while y >= 1:
    s=s1
    while s>=1:
        print(" ", end="")
        s -= 1
    r = (y*2)-1
    j=r
    while j>=1:
        if r == j or j==1:
            print("*", end="")
        else:
            print(" ", end="")
        j -= 1
    y -= 1
    s1=s1+1
    print()

##16
12345
2345
345
45
5

n = int(input("16. n: "))
i = 1
k = n
while i <= n:
    j = i
    while j <= n:
        print(j, end = "")
        j = j + 1
    print()
    i = i + 1


# 17
5
45
345
2345
12345

n = int(input("16. n: "))
i = 1
k = n
while i <= n:
    j = n
    while j <= k:
        print(j, end = "")
        j = j + 1
    print()
    n = n - 1

##18. n: 5
1 
2 6 
3 7 10 
4 8 11 13 
5 9 12 14 15

n = int(input("18.n: "))
i = 1
while i <= n:
    j = 1
    k = i
    while j <= i:
        print(k, end= " ")
        k = k + n - j
        j = j + 1
    i = i + 1
    print()

19.n: 5
    *
   * *
  *   *
 *     *
*********
n = int(input("19.n: "))
i = 1
while i <=n:
    j = i
    while j < n:
        print(" ", end="")
        j = j + 1
    j=1
    while(j<=i*2-1):
        if(j==1 or j==i*2-1 or i==n):
            print("*",end="")
        else:
            print(" ",end="")
        j=j+1
    i = i + 1
    print()

20.n: 5
    1
   121
  12321
 1234321
123454321
 1234321
  12321
   121
    1

n = int(input("20.n: "))
i = 1
while i <=n:
    k = i
    while k <n:
        print(" ",end= "")
        k = k +1
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    r = i - 1
    while r >= 1:
        print(r, end= "")
        r -= 1
    i = i + 1
    print()
i = 1
w = 1
q = 1
while i <= n:
    j = w
    while j >=1:
        print(" ", end="")
        j -= 1
    e = 1
    while e < n:
        print(e, end="")
        e = e + 1
    t = n-2
    while t >= 1:
        print(t, end= "")
        t -= 1
    n = n - 1
    w = w + 1
    print()

    or
20.n: 5
     1
    121
   12321
  1234321
 123454321
  1234321
   12321
    121
     1
n = int(input("20.n: "))
i = 1
while i <= n:
    k = i
    while k <= n:
        print(" ", end="")
        k+= 1
    j = 1
    m = i*2-1
    f = 1
    l = i-1
    while j <= m:
        if j <= i:
            print(f,end="")
            f=f+1
        else:
            print(l, end="")
            l=l-1
        j = j + 1
    i+=1
    print()
'''
n=int(input("enter n:"))
i = 1
while i<=n:
    j = i
    while j <n:
        print(" ", end="")
        j+=1
    k = 1
    while k <= i:
        print("*", end=" ")
        k+=1
    i+=1
    print()
'''
21.n: 5
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
n = int(input("21.n: "))
i = 1
while i <=n:
    k = i
    while k < n:
        print(" ", end= "")
        k += 1
    j = 1
    while j <= i:
        print("*" , end=" ")
        j +=1
    i +=1
    print()
i = 1
while i <= n:
    e = 1
    while e <= i:
        print(" ", end="")
        e = e+ 1
    t = i
    while t<n:
        print("*", end=" ")
        t +=1
    i +=1
    print()
        
22.n: 5
*********
 *     *
  *   *
   * *
    *

n = int(input("22.n: "))
i = n
while i >= 1:
    j = i
    while j < n:
        print(" ", end="")
        j = j+ 1
    r = 1
    while r <= i*2-1:
        if r == i*2-1 or r == 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
        r = r + 1
    i = i - 1
    print()


23. enter a:ABCDEF
A
AB
ABC
ABCD
ABCDE
ABCDEF
a=str(input("23. enter a:"))
L = len(a)
i = 0
while i < L:
    j = 0
    while j <= i:
        print(a[j], end="")
        j += 1
    i += 1
    print()

24.n: 5
*****
*****
*****
*****
*****
n = int(input("24.n: "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        print("*",end="")
        j = j + 1
    i += 1
    print()
    
25.n: 5
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
n = int(input("25.n: "))
i = 1
while i <= n:
    j = i
    while j < n:
        print(" ", end="")
        j = j + 1
    h = 1
    f = i * 2 - 1
    while h <= f:
        print("*", end="")
        h +=1
    i += 1
    print()
i = 1
n = n - 1
t1 = 1
while i <= n:
    t = t1
    while t >= 1:
        print(" ", end="")
        t = t- 1
    q = n*2-1
    v = 1
    while v <= q:
        print("*", end="")
        v += 1
    t1 += 1
    n -= 1
    print()

26.a: ABCDEF
     A
    B B
   C   C
  D     D
 E       E
F         F
 E       E
  D     D
   C   C
    B B
     A
a = str(input("26.a: "))
i = 0
L = len(a)
while i < L:
    j = i
    while j < L-1:
        print(" ",end="")
        j += 1
    q = 1
    y = i + 1
    m = y * 2 - 1
    while q <= m:
        if q == 1 or q== m:
            print(a[i], end="")
        else :
            print(" ", end="")
        q+=1
    i+=1
    print()
i = 0
s1=1
L = len(a)-2
while i <= L:
    j = s1
    while j >= 1:
        print(" ", end="")
        j -=1
    h = 1
    m = L * 2+1
    while h <= m:
        if h == 1 or h == m:
            print(a[L], end="")
        else:
            print(" ", end="")
        h = h + 1
    L -= 1
    s1 = s1 + 1
    print()
        
27.n: 5
*********
 *     *
  *   *
   * *
    *
   * *
  *   *
 *     *
*********
n = int(input("27.n: "))
i = 1
n1 = n
n2 = n
t1 = 1
while i <= n:
    t = t1
    while t > 1:
        print(" ", end="")
        t -= 1
    q = n *2-1
    v = 1
    while v <= q:
        if v == 1 or v == q or n==n1:
            print("*", end="")
        else:
            print(" ", end="")
        v += 1
    t1 += 1
    n -= 1
    print()

i = 2
while i <= n2:
    j = i
    while j < n2:
        print(" ", end="")
        j = j + 1
    e = 1
    w = i*2-1
    while e <= w:
        if e == 1 or e == w or n1 == i:
            print("*", end="")
        else:
            print(" ", end="")
        e += 1
    i = i + 1
    print()

28..n: 5
*****
*   *
*   *
*   *
*****
n = int(input("28..n: "))
i = 1
y = n
while i <= n:
    u = 1
    while u <= n:
        if u == 1 or u == n or n == i or i == 1:
            print("*", end="")
        else:
            print(" ", end="")
        u += 1
    i += 1
    print()
    
29. enter a: ABCDEF
     A 
    A B 
   A B C 
  A B C D 
 A B C D E 
A B C D E F
a=str(input("29. enter a: "))
L = len(a)
i = 0
while i < L:
    j = i
    while j < L-1:
        print(" ", end="")
        j += 1

    h = 0
    while h <= i:
        print(a[h], end=" ")
        h +=1
    i += 1
    print()


30..n: 6
*
**
***
****
*****
******
n = int(input("30..n: "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    i += 1
    print()

31. enter a:ABCDE
A
BB
CCC
DDDD
EEEEE
a=str(input("31. enter a:"))
L = len(a)
i = 0
while i < L:
    j = 0
    while j <= i:
        print(a[i], end="")
        j += 1
    i += 1
    print()

32. enter a:ABCDE
ABCDE
ABCD
ABC
AB
A
a=str(input("32. enter a:"))
L = len(a)
i = 0
while i < L:
    j = 0
    while j < L:
        print(a[j], end="")
        j += 1
    L = L - 1
    print()

33.n: 5
   *
  * *
 *   *
*******
n = int(input("33.n: "))
i = 1
while i < n:
    j = i
    while j < n-1:
        print(" ", end="")
        j += 1
    t = 1
    q = i * 2 - 1
    while t <= q:
        if t == 1 or t == q or i == n-1:
            print("*", end="")
        else:
            print(" ", end="")
        t += 1
    i += 1
    print()

34.n: 6
******
*****
****
***
**
*
n = int(input("34..n: "))
i = 1
while i <= n:
    j = i
    while j <= n:
        print("*", end="")
        j += 1
    i += 1
    print()

35.n: 5
*
**
* *
*  *
*****

n = int(input("35.n: "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        if j == 1 or j == i or i == n:
            print("*", end= "")
        else:
            print(" ", end= "")
        j = j + 1
    i += 1
    print()

36.n: 5
    * 
   * * 
  *   * 
 *     * 
* * * * *
 
n = int(input("36.n: "))
i = 1
f = 1
while i <= n:
    j = f
    while j < n:
        print(" ", end= "")
        j = j + 1
    f = f + 1
    
    t = 1
    while t <= i:
        if t == 1 or t == i or i == n:
            print("*", end= " ")
        else:
            print(" ", end= " ")
        t = t+ 1
    i = i + 1
    print()

37..n: 5
1
12
1 3
1  4
12345

n = int(input("37..n: "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        if(j==1 or j==i or i==n):
            print(j, end= "")
        else:
            print(" ",end="")
        j = j + 1
    i = i + 1
    print()

38.n: 5
12345
2  5
3 5
45
5

n = int(input("38.n: "))
i = 1
while i <= n:
    j = i
    y = 1
    while j <= n:
        if j == y or j == i or j == n:
            print(j, end="")
        else:
            print(" ",end="")
        j = j + 1
        y = y + 1
    i = i + 1
    print()

###39..n: 5
    1
   121
  12321
 1234321
123454321

n = int(input("39..n: "))
i = 1
while i <= n:
    k = i
    while k < n:
        print(" ", end= "")
        k = k + 1
    
    g = 1
    while g <= i:
        print(g, end = "")
        g = g + 1
    a = i - 1 
    h = a
    while h >= 1:
        print(h, end="")
        h = h - 1
    i = i + 1
    print()
 
40.n: 6
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
n = int(input("40.n: "))
i = 1
while i <= n:
    j = i
    while j < n:
        print(" ", end="")
        j = j + 1
    
    k = 1
    while k <= i:
        print("*", end=" ")
        k = k + 1
    i = i + 1
    print()

41.n: 5
1
12
123
1234
12345
n = int(input("41.n: "))
i = 1
while i <= n:
    k = 1
    while k <= i:
        print(k, end="")
        k = k + 1
    i = i + 1
    print()
    
42.n: 5
    1
   232
  34543
 4567654
567898765
n = int(input("42.n: "))
i = 1
t = 0
while i <= n:
    k = i
    while k < n:
        print(" ", end="")
        k = k + 1
        
    j = 1
    k=i
    while j <= i:
        print(k, end="")
        j = j + 1
        k = k + 1

    j = i
    u = t 
    while j > 1:
        print(u, end="")
        u = u - 1
        j = j - 1
    t = t + 2
    i = i + 1
    print()

43. n: 5
1
121
12321
1234321
123454321
n = int(input("43. n: "))
i = 1
while i <= n:
    q = 1
    m = i * 2 - 1
    f = 1
    l = i - 1
    while q <= m:
        if q <= i:
           print(f, end="")
           f = f + 1
        else:
            print(l, end= "")
            l = l - 1
        q+=1
    i = i + 1
    print()

###44..n: 5
********1********
*******2*2*******
******3*3*3******
*****4*4*4*4*****
****5*5*5*5*5****
          
n = int(input("44..n: "))
i = 1
while i <= n:
    k = i
    p = 2 * n - 2
    while k <= p:
        print("*", end= "")
        k = k + 1
    
    g = 1
    while g <= i:
        if g == i:
            print(i, end ="")
        else:
            print(i, end ="*")
        g = g + 1
    k = i
    p = 2 * n - 2
    while k <= p:
        print("*", end= "")
        k = k + 1
    i = i + 1
    print()

45.n: 6
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 

n = int(input("45.n: "))
i = 1
while i <= n:
    k = 1
    while k < i:
        print(" ", end ="")
        k = k + 1
    j = i
    while j <= n:
        print("*", end=" ")
        j = j + 1
    i = i + 1
    print()
   
46.n: 5
12345
1234
123
12
1
n = int(input("46.n: "))
i = 1
while i <= n:
    k = i
    while k <= n:
        print(k, end="")
        k = k + 1
    n = n - 1
    print()

47.n: 5
    1 
   1 2 
  1   3 
 1     4 
1 2 3 4 5 

n = int(input("47.n: "))
i = 1
f = 1
while i <= n:
    j = f
    while j < n:
        print(" ", end= "")
        j = j + 1
    f = f + 1
    t = 1
    while t <= i:
        if t == 1 or t == i or i == n:
            print(t, end= " ")
        else:
            print(" ", end= " ")
        t = t+ 1
    i = i + 1
    print()

48.a: ABCDE
A
ABA
ABCBA
ABCDCBA
ABCDEDCBA
a = str(input("48.a: ")) #ABCDE
i = 1
L = len(a)
while i <= L:
    p = 1
    m = i * 2 - 1
    f = 0
    g = i - 2
    while p <= m:
        if p <= i:
            print(a[f], end="")
            f = f + 1
        else:
            print(a[g], end="")
            g = g - 1
        p += 1
    i+= 1
    print()

49.n: 5
**********
****  ****
***    ***
**      **
*        *
**      **
***    ***
****  ****
**********
n = int(input("49.n: "))
i = 1
while i <= n:
    j = i
    while j <= n:
        print("*", end = "")
        j = j + 1
    k = 1
    while k < i:
        print(" ", end = "")
        k = k + 1
    g = 1
    while g < i:
        print(" ", end= "")
        g = g + 1
    h = i
    while h <= n:
        print("*",end="")
        h = h + 1
    i = i + 1
    print()
i = 2
while i <= n:
    y = 1
    while y <= i:
        print("*", end = "")
        y += 1
    h = i
    while h < n:
        print(" ",end="")
        h = h + 1
    j = i
    while j < n:
        print(" ", end = "")
        j = j + 1
    k = 1
    while k <= i:
        print("*", end = "")
        k = k + 1
    i = i + 1
    print()
    
50.n: 6
*          *
**        **
***      ***
****    ****
*****  *****
************
************
*****  *****
****    ****
***      ***
**        **
*          *
n = int(input("50.n: "))
i = 1
y = n
while i <= n:
    k = 1
    y = n * 2
    z = y - i
    while k <= y:
        if k<=i or z<k:
            print("*", end="")
        else:
            print(" ", end="")
        k = k + 1
    i = i + 1
    print()
i = 1
temp=n
temp1=n
while i <= n:
    r = 1
    t = temp * 2
    f = t - n
    while r <= t:
        if n==temp1 or r<=n or r>f:
            print("*", end="")
        else:
            print(" ", end="")
        r = r + 1
    n -= 1
    print()


### 51.n: 5
   *****
  *****
 *****
*****

n = int(input("51.n: "))
i = 1
while i < n:
    k = i
    g = n-2
    while k <= g:
        print(" ", end= "")
        k = k + 1
    f = 1
    while f < n:
        print("*", end="")
        f = f + 1
    i +=1
    print()

####52.n: 4
3
44
555
6666
555
44
3

n = int(input("52..n: "))
i = 1
while i <= n:
    k = 1
    while k <= i:
        print(i + 2, end="")
        k = k + 1
    i = i + 1
    print()
    
f = n - 1
while f >= 1:
    i = 1
    while i <= f:
        print(f + 2, end="")
        i = i + 1
    f = f - 1
    print()

### 53. n = 5
11111
22222
33333
44444
55555

*****
empty
*****
empty  
*****

n = int(input("51.n: "))
i = 1
while i <= n:
    k = 1
    while k <= n:
        if i % 2 != 0:
            print("*", end="")
        else:
            print(" ", end="")
        k = k + 1
    i = i + 1
    print()

54.n: 4
   ****
  *  *
 *  *
****
n = int(input("54.n: "))
i = 1
c = n
while i <= n:
    j = i
    while j < n:
        print(" ", end="")
        j += 1
    h = 1
    while h <= n:
        if h == 1 or h == n or c == i or i == 1:
            print("*", end="")
        else:
            print(" ", end="")
        h = h + 1
    i += 1
    print()
    
###55..n: 4
1
2*2
3*3*3
4*4*4*4
4*4*4*4
3*3*3
2*2
1

n = int(input("55..n: "))
i = 1
while i <= n:
    k = 1
    while k <=  i:
        if k == i:
            print(i, end="")
        else:
            print(i, end="*")
        k = k + 1
    i = i + 1
    print()
j = n
while j >= 1:
    k = 1
    while k <= j:
        if k == j:
            print(j, end="")
        else:
            print(j, end="*")
        k = k + 1
    j = j - 1
    print()

56.n: 5
*****
     
*   *
     
*****
n = int(input("56.n: "))
i = 1
w = n
while i <= n:
    j = 1
    while j <= n:
        if  (j == 1 or j == n or i == 1 or i == n) and (i % 2 != 0):
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    i +=1
    print()

57..n: 7
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1 
n = int(input("57..n: "))
i = 0
while i< n:
    k = 1
    j = 0
    while j <= i:
        print(k, end=" ")
        k = k*(i-j)//(j+1)
        j+=1
    print()
    i=i+1

58.n: 4
1
2*3
4*5*6
7*8*9*10
7*8*9*10
4*5*6
2*3
1
n = int(input("58..n: "))
i = 1
j = 1
while i <= n:
    k = 1
    while k <= i:
        if i == k:
            print(j, end="")
        else:
            print(j, end="*")
        k = k + 1
        j = j + 1
    i = i + 1
    print()
i = 1
while i <= n:
    k = 1
    s = j - n
    while k <= n:
        if k == n:
            print(s, end="")
        else:
            print(s, end="*")
        k = k + 1
        s = s + 1
    j = j - n
    n = n - 1
    print()

59.n: 5
    *
   ***
  * * *
 *  *  *
*********
 *  *  *
  * * *
   ***
    *
n = int(input("59.n: "))
i = 1
f = n
while i <= n:
    j = i
    while j < n:
        print(" ", end="")
        j = j + 1
    t = 1
    while t <= i:
        if n == i or i == t or t == 1: 
            print("*", end="")
        else:
            print(" ", end="") 
        t = t + 1
    y = 2
    while y <= i:
        if n == i or y == i: 
            print("*", end="")
        else:
            print(" ", end="") 
        y = y + 1
    i +=1
    print()
i = 1
s = 1
k = n
while i < n:
    j = s
    u = 1
    while u <= j:
        print(" ", end="")
        u +=1
    a = n
    r = n
    while a > 1:
        if a == r or a == 2:
            print("*", end="")
        else:
            print(" ", end="")
        a -= 1
    v = k
    f = k
    j = s + 2
    while j <= v:
        if j == v:
            print("*", end="")
        else:
            print(" ", end="")
        j +=1
    n -= 1
    s = s + 1
    print()

    OR
    

n = int(input("59.n: "))
i = 1
while i <= n:
    j = i
    while j < n:
        print(" ", end="")
        j = j + 1
    r = 1
    k = i*2 - 1
    while r <= k:
        if r == 1 or r == i or r == k or n == i:
            print("*", end="")
        else:
            print(" ", end="")
        r +=1
    i = i + 1
    print()
i = 1
s = 1
while i <= n:
    j = s
    while j>= 1:
        print(" ",end="")
        j-=1
    r = 1
    t = n
    k = n*2 - 3
    while r <= k:
        if r == 1 or r == k or r == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
        r += 1
    s +=1
    n -= 1
    print()


60.n: 5
        *
      *  
    *    
  *      
*********
  *
    *
      *
        *

n = int(input("60.n: "))
i = 1
k = n
e = n
temp=n
while i <= n:
    t1 = n + 1
    t = n*2
    t2= temp*2-1
    m = n * 2 - i
    j = 1
    while j < t:
        if(i==n or j==t2):
            print("*",end="")
        else:
            print(" ",end="")
        j = j + 1
    i += 1
    temp=temp-1
    print()
    
i = 1
n = e
s1 = 1
n = temp
while i < e:
    t1 = n + 1
    s = s1
    t = s*2 + 1
    j = 1
    while j <= t:
        if j == t:
            print("*", end="")
        else:
            print(" ", end="")
        j = j + 1
    s1 +=1
    e -= 1
    print()
'''





































  
