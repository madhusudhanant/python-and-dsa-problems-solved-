'''
1.n: 5
1
12
123
1234
12345

n=int(input("1.n: "))
for i in range(1,n+1):
    j = 1
    for j in range(1,i+1):
        print(j, end="")
    print()

2.n: 5
5
54
543
5432
54321


n=int(input("2.n: "))
n1=n
for i in range(n,0,-1):
    for j in range(n1,i-1,-1):
        print(j, end="")
    print()
reverse natural numbers

n=int(input("2.n: "))
n1=n
for i in range(n,0,-1):
    for j in range(n1 ,i-1, -1):
        print(j, end="")
    print()
3.n: 5
1
21
321
4321
54321
n=int(input("3.n: "))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

4.n: 5
1
23
456
78910
n = int(input("4.n: "))
k = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k,end="")
        k=k+1
    print()

5.n: 5
    1
   21
  321
 4321
54321

n = int(input("5.n: "))
for i in range(1,n+1):
    for j in range(i, n):
        print(" ", end="")
        
    for h in range(i,0,-1):
        print(h, end="")
    print()

6.n: 5
54321
4321
321
21
1  
n = int(input("6.n: "))
for i in range(n,0, -1):
    for j in range(i,0,-1):
        print(j, end="")
    print()

7.n: 5
10101
01010
10101
01010

n = int(input("7.n: "))
k = 1
for i in range(1,n):
    for j in range(i,n+i):
        if k%2==0:
            print("0", end="")
        else:
            print("1", end="")
        k += 1
    print()

8.n: 5
1
10
101
1010
10101
n=int(input("8.n: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if j%2==0:
            print("0", end="")
        else:
            print("1", end="")
    print()

9.n: 5
1
12
123
1234
12345
1234
123
12
1
n=int(input("9.n: "))
for i in range(1,n+1):
    j = 1
    for j in range(1,i+1):
        print(j, end="")
    print()
for y in range(1,n+1):
    for r in range(1,n+1-y):
        print(r, end="")
    print()

10.n: 5
1
22
333
4444
55555

n=int(input("10.n: "))
for i in range(1,n+1):
    for k in range(1, i+1):
        print(i, end="")
    print()

11.n: 5
*
**
***
****
*****
n=int(input("11.n: "))
for i in range(1,n+1):
    for k in range(1, i+1):
        print("*", end="")
    print()

12.n: 5
12345
1234
123
12
1
n=int(input("12.n: "))
for i in range(1,n+1):
    for k in range(1, n+2-i):
        print(k, end="")
    print()

13.n: 5
54321
5432
543
54
5
n=int(input("13.n: "))
for i in range(1,n+1):
    for k in range(n,i-1,-1):
        print(k, end="")
    print()

14.n: 5
    1
   12
  123
 1234
12345
n=int(input("14.n: "))
for p in range(1,n+1):
    for j in range(1, n+1-p):
        print(" ", end="")

    for h in range(1, p+1):
        print(h, end="")
    print()

15.n: 5
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
n=int(input("15.n: "))
for i in range(1, n+1):
    for w in range(1,n+1-i):
        print(" ",end="")
    for k in range(1, i*2):
        if k == 1 or k == i*2-1: 
            print("*", end="")
        else:
            print(" ", end="")
    print()

s = 1 
for c in range(n,0, -1):
    for d in range(1,s+1):
        print(" ", end="")
    e = c*2-3
    for h in range(e,0,-1):
        if h == 1 or h == e:
            print("*", end="")
        else:
            print(" ", end="")
    s+=1
    print()

16.n: 5
12345
2345
345
45
5
n=int(input("16.n: "))
for i in range(1, n+1):
    for h in range(i, n+1):
        print(h, end="")
    print()

17.n: 5
5
45
345
2345
12345
n=int(input("17.n: "))
for i in range(n,0, -1):
    for g in range(i,n+1):
        print(g, end="")
    print()

18.n: 5
1
26
3710
481113
59121415
n=int(input("18.n: "))
for i in range(1, n+1):
    k = i
    for h in range(1,i+1):
        print(k, end=" ")
        k = k + n - h
    print()

19.n: 5
    *
   * *
  *   *
 *     *
*********
n=int(input("19.n: "))
for p in range(1, n+1):
    for r in range(p,n):
        print(" ", end="")
    y = p*2-1
    for q in range(1,y+1):
        if q == 1 or q == y or n==p:
            print("*", end="")
        else:
            print(" ", end="")
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
n=int(input("20.n: "))
for i in range(1, n+1):
    for r in range(i,n):
        print(" ", end="")
    k = 1
    m = i*2-1
    f = 1
    d = i - 1
    for x in range(1, m+1):
        if x <= i:
            print(f, end="")
            f+=1
        else:
            print(d, end="")
            d-=1 
    print()
for i in range(n,0,-1):
    for h in range(i,n+1):
        print(" ",end="")
    k = 1
    m = i*2 - 3
    f = 1
    d = i-2
    for y in range(1,m+1):
        if y <= i-1:
            print(f,end="")
            f +=1
        else:
            print(d,end="")
            d -=1

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
n=int(input("21.n: "))
for i in range(1,n+1):
    for k in range(i,n):
        print(" ", end="")

    for t in range(1,i+1):
        print("*", end=" ")
    print()
s =1
for i in range(n,0,-1):
    for k in range(i,n+1):
        print(" ", end="")
    for t in range(n+1,s+1,-1):
        print("*", end=" ")
    print()
    s+=1
    print()

22.n: 5
*********
 *     *
  *   *
   * *
    *
n = int(input("22.n: "))
s = n
e = n*2-1
for i in range(1-1,n):
    for j in range(1,i+1):
        print(" ", end="")
    k = s*2-1
    for w in range(1,k+1):
        if w == 1 or w == k or k==e:
            print("*", end="")
        else:
            print(" ", end="")
    s-=1
    print()

23.n: ABCDE
A
AB
ABC
ABCD
ABCDE
n = str(input("23.n: "))
L = len(n)
for i in range(0,L):
    for j in range(0,i+1):
        print(n[j],end="")
    print()
    
 
24.n: 5
*****
*****
*****
*****
*****
n = int(input("24.n: "))
for i in range(1,n+1):
    for j in range(1, n+1):
        print("*", end="")
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
for i in range(1,n+1):
    for j in range(i, n):
        print(" ", end="")
    k = i*2-1
    for h in range(1,k+1):
        print("*", end="")
    print()

s= 1
for i in range(n,0,-1):
    for u in range(1,s+1):
        print(" ", end="")
    k = i*2 - 1
    for j in range(1+1,k):
        print("*", end="")
    s+=1
    print()

26.n: ABCDEF
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
n = str(input("26.n: "))
L = len(n)
x=1
for i in range(0, L):
    for j in range(i, L-1):
        print(" ", end="")
    k = (x*2-1)-1
    for u in range(0, k+1):
        if u == 0 or u == k:
            print(n[i], end="")
        else:
            print(" ", end="")
    x=x+1
    print()
s=1
t = L-2
for j in range(t,-1,-1):
    for k in range(1,s+1):
        print(" ", end="")
    r = j*2-1
    for w in range(1,r+3):
        if w == 1 or w == r+2:
            print(n[j], end="")
        else:
            print(" ", end="")
    t -=1
    s+=1
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
t = n*2-1
e=n
for i in range(1,n+1):
    for j in range(1,i):
        print(" ", end="")
    r = e*2-1
    for h in range(1,r+1):
        if h == 1 or h == r or i==1:
            print("*", end="")
        else:
            print(" ", end="")
    e-=1
    print()
s =2
for i in range(n-1,0,-1):
    for j in range(i-1,0,-1):
        print(" ", end="")
    r = s*2-1
    for v in range(1,r+1):
        if v==1 or v==r or i==1:
            print("*",end="")
        else:
            print(" ", end="")
    print()
    s+=1

28.n: 5
*****
*   *
*   *
*   *
*****

n = int(input("28.n: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j == 1 or j == n or i ==1 or i ==n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
29.n: ABCDEF
    A B 
   A B C 
  A B C D 
 A B C D E 
A B C D E F 
n = str(input("29.n: "))
L = len(n)
s = L-2
for j in range(1,L):
    for k in range(j,L-1):
        print(" ", end="")
    for g in range(0, L-s):
        print(n[g], end=" ")
    s-=1
    print()

30.n: 6
*
**
***
****
*****
******
n =int(input("30.n: "))
for k in range(1,n+1):
    for j in range(1,k+1):
        print("*", end="")
    print()

31.n: ABCDE
A
BB
CCC
DDDD
EEEEE
n = str(input("31.n: "))
L = len(n)
for h in range(0,L):
    for u in range(0,h+1):
        print(n[h], end="")
    print()


32.n: ABCDE
ABCDE
ABCD
ABC
AB
A
n = str(input("32.n: "))
L = len(n)
for h in range(0,L):
    for u in range(0,L-h):
        print(n[u], end="")
    print()

33.n: 4
   *
  * *
 *   *
*******
n = int(input("33.n: "))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ", end="")
    p = i*2-1
    for k in range(1,p+1):
        if n == i or k == p or k == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

34.n: 6
******
*****
****
***
**
*
n = int(input("34.n: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*", end="")
    print()

35.n: 6
*
**
* *
*  *
*   *
******
n = int(input("35.n: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if n==i or j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

36.n: 6
     * 
    * * 
   *   * 
  *     * 
 *       * 
* * * * * *
n = int(input("36.n: "))
for i in range(1,n+1):
    for m in range(1,n+1-i):
        print(" ",end="")
    for j in range(1,i+1):
        if n==i or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


37.n: 5
1
12
1 3
1  4
12345
n = int(input("37.n: "))
for i in range(1,n+1):
    for g in range(1, i+1):
        if g ==1 or g == i or i == n:
            print(g, end="")
        else:
            print(" ", end="")
    print()
38.n: 5
12345
2  5
3 5
45
5
n = int(input("38.n: "))
for i in range(1,n+1):
    for g in range(i, n+1):
        if g == i or g == n or i == 1:
            print(g, end="")
        else:
            print(" ", end="")
    print()

39.n: 5
    1
   121
  12321
 1234321
123454321
n = int(input("39.n: "))
for i in range(1,n+1):
    for g in range(1, n+1-i):
        print(" ",end="")
    d = i * 2 -1
    t = i - 1
    f = 1
    for g in range(1, d+1):
        if g <= i:
            print(f,end="")
            f += 1
        else:
            print(t,end="")
            t-=1
    print()

40.n: 6
     * 
    * * 
   *   * 
  *     * 
 *       * 
* * * * * * 
n = int(input("40.n: "))
for i in range(1,n+1):
    for g in range(1, n+1-i):
        print(" ",end="")
    for v in range(1, i+1):
        if v == 1 or n == i or v == i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

41.n: 5
1
12
123
1234
12345
n = int(input("41.n: "))
for i in range(1,n+1):
    for g in range(1, i+1):
        print(g,end="")
    print()

42.n: 5
    1
   232
  34543
 4567654
567898765

n = int(input("42.n: "))
s=2
for i in range(1,n+1):
    for g in range(i, n):
        print(" ", end="")
    e=i*2
    k1=i
    k2=s
    for k in range(1, e):
        if k<=i:
            print(k1, end="")
            k1=k1+1
        else:
            print(k2,end="")
            k2=k2-1
    s=k1       
    print()


43.n: 5
1
121
12321
1234321
123454321

n =int(input("30.n: "))
for i in range(1,n+1):
    for k in range(1,i+1):
        print(k, end="")
    for b in range(i-1,0,-1):
        print(b, end="")
    print()


44.n: 5
********1********
*******2*2*******
******3*3*3******
*****4*4*4*4*****
****5*5*5*5*5****
n = int(input("44.n: "))
for i in range(1, n+1):
    s = n
    e = s*2-2
    for j in range(i,e+1):
        print("*", end="")
    for w in range(1,i+1):
        if w != i:
            print(i, end="*")
        else:
            print(i, end="")
    for u in range(i, e+1):
        print("*", end= "")
    print()
    s -=1

45.n: 6
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
n = int(input("45.n: "))
for i in range(1, n+1):
    for g in range(1,i):
        print(" ", end= "")
    for y in range(1, n+2-i):
        print("*", end=" ")
    print()

46.n: 5
12345
1234
123
12
1
n = int(input("46.n: "))
for i in range(1, n+1):
    for g in range(1,n+2-i):
        print(g, end= "")
    print()

47.n: 5
    1 
   1 2 
  1   3 
 1     4 
1 2 3 4 5 
n = int(input("47.n: "))
for i in range(1, n+1):
    for k in range(1, n+1-i):
        print(" ", end="")
    for g in range(1,i+1):
        if g == 1 or n == i or g == i:
            print(g, end= " ")
        else:
            print(" ", end=" ")
    print()

    
48.n: ABCDE
A
ABA
ABCBA
ABCDCBA
ABCDEDCBA
n = str(input("48.n: "))
L = len(n)
for i in range(0,L+1):
    d = i * 2 -1
    t = (i-1) - 1
    f = 0
    for g in range(0, d):
        if g <= i-1:
            print(n[f],end="")
            f += 1
        else:
            print(n[t],end="")
            t-=1
    print()

49.n: 5
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

n = int(input("49.n: "))
for i in range(1, n+1):
    for b in range(1,n+2-i):
        print("*", end="")
    p = i*2
    for b in range(1,p-1):
        print(" ", end="")
    for k in range(1,n+2-i):
        print("*", end="")
    print()
s = n
for i in range(1,n+1):
    for j in range(1, i+1):
        print("*",end="")
    k = s*2-1
    for w in range(2,k+1):
        print(" ", end="")
    for r in range(1, i+1):
        print("*", end="")
    s-=1
    print()

50.n: 5
*        *
**      **
***    ***
****  ****
**********
**********
****  ****
***    ***
**      **
*        * 

n = int(input("50.n: "))
s = n
for i in range(1,n+1):
    for j in range(1, i+1):
        print("*",end="")
    k = s*2-1
    for w in range(2,k+1):
        print(" ", end="")
    for r in range(1, i+1):
        print("*", end="")
    s-=1
    print()
for i in range(1, n+1):
    for b in range(1,n+2-i):
        print("*", end="")
    p = i*2
    for b in range(1,p-1):
        print(" ", end="")
    for k in range(1,n+2-i):
        print("*", end="")
    print()

51.n: 4
   ****
  ****
 ****
****
n=int(input("51.n: "))
for i in range(1, n+1):
    for h in range(1, n+1-i):
        print(" ", end="")
    for k in range(1, n+1):
        print("*", end="")
    print()

52.n: 4
3
44
555
6666
555
44
3

n=int(input("52.n: "))#4
s=n*2+1
y = n
r = 1
#r=-(n*2-(n+1))
for i in range(1, n*2):
    for t in range(1, i+1):
        if i<=n:
            print(i+2, end="")
        else:
            if t<=n-r:
                print(s, end="")
        t+=1
    s-=1
    y -=1
    if i > n:
        r+=1
    print()

53.n: 5
*****
     
*****
     
*****
n=int(input("53.n: "))
for i in range(1, n+1):
    for k in range(1, n+1):
        if i%2==0:
            print(" ", end="")
        else:
            print("*", end="")
    print()

54.n: 4
   ****
  *  *
 *  *
****
n=int(input("54.n: "))
for i in range(1, n+1):
    for k in range(i, n):
        print(" ", end="")
    for g in range(1, n+1):
        if g ==1 or i == 1 or n == i or g == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

55.n: 4
1
2*2
3*3*3
4*4*4*4
4*4*4*4
3*3*3
2*2
1
n=int(input("55.n: "))
for i in range(1, n+1):
    for u in range(1,i+1):
        if u == i:
            print(i, end="")
        else:
            print(i, end="*")
    print()
f=1
for i in range(n,0,-1):
    for s in range(i,0,-1):
        if s == 1:
            print(i, end="")
        else:
            print(i, end="*")
    print()
    f+=1

56.n: 5
*****
     
*   *
     
*****
n=int(input("56.n: "))
for i in range(1, n+1):
    for u in range(1,n+1):
        if (u == 1 or u == n or n == i or i == 1) and (i %2!=0):
            print("*", end="")
        else:
            print(" ", end="")
    print()

57.n: 7
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1 

n=int(input("57.n: "))
for i in range(0,n):
    k = 1
    for j in range(0,i+1):
        print(k, end=" ")
        k = k*(i-j)//(j+1)
    print()

58.n: 4
1
2*3
4*5*6
7*8*9*10
78910
456
23
1
n=int(input("58.n: "))
k=1
for i in range(1, n+1):
    for u in range(i,i*2):
        if u == i*2-1:
            print(k,end="")
        else:
            print(k,end="*")
        k+=1
    print()

j = k-n
for i in range(n, 0,-1):
    s = j
    for k in range(1,i+1):
        if k ==i:
            print(s, end="")
        else:
            print(s, end="*")
        s=s+1
    j=j-i+1
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

n=int(input("59.n: "))
for i in range(1, n+1):
    for j in range(1, n+1-i):
        print(" ", end="")
    p = i*2-1
    for k in range(1, p+1):
        if k ==1 or k == p or k ==i or n ==i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
s =1
for i in range(n,0,-1):
    for k in range(1,s+1):
        print(" ",end="")
    p = i*2-3
    for j in range(p,0,-1):
        if j ==p or j ==1 or j ==i-1:
            print("*", end="")
        else:
            print(" ",end="")
    s+=1
    print()

or

n=int(input("59.n: "))
for i in range(1, n+1):
    for j in range(i,n):
        print(" ", end="")
    p = i*2-1
    for k in range(1, p+1):
        if k == 1 or n==i or k == p or k ==i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
s=1
for k in range(n,0,-1):
    for u in range(1,s+1):
        print(" ", end="")
        
    p = k*2-3
    for h in range(1,p+1):
        if h == 1 or h == p or h ==k-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    s+=1

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
n2= n
n1= n
for i in range(1, n+1):
    p = n*2-1
    p1 = n2*2-1
    r = n1*2-1
    for j in range(1, p+1):
        if i == n or j ==p1:
            print("*", end="")
        else:
            print(" ", end="")
    n2-=1
    print()
    
n3 = n
s=3
for i in range(1, n+1):
    p = n*2-1
    p1 = s*2-3
    r = n1*2-1
    for j in range(1, p+1):
        if j ==p1:
            print("*", end="")
        else:
            print(" ", end="")
    n3-=1
    s+=1
    print()
'''













