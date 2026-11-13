'''
Memory Trick
If a function returns a real value, print(function()) prints that value.
If a function doesn't return a value (or uses just return), Python automatically returns None, so print(function()) prints None.

## Direct recursion - mostly

Direct recursion occurs when a function calls itself directly.

def fun_name(n):
    if n == 0:
        return

    print(n)
    fun_name(n-1)
fun_name(5)

#even number
def direct(n):
    if n == 0:
        return
    
    if n % 2 == 0:
        print(n)
    direct(n-1)
direct(10)

##indirect recursion
Definition:
Indirect recursion occurs when a function calls another function, and that function calls the first function back.

def fun1(n):
    if n > 0:
        print(n)
        fun2(n-1)
def fun2(n):
    if n > 0:
        print(n)
        fun1(n-1)
fun1(10)

## Tail recursion
definition
Tail recursion is a type of recursion in which the recursive call is the last operation performed by the function.

def tail_recursive(n):
    if n == 0:
        return
    print(n)
    tail_recursive(n-1)
tail_recursive(5)   

### Non-tail recursion
definition:
Non-tail recursion is a type of recursion in which the recursive call is not the last operation in the function.
def tail_recursive(n):
    if n == 0:
        return 0

    return n + tail_recursive(n - 1)

n = int(input("n: "))
print(tail_recursive(n))
'''
#factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)
print(factorial(5))
'''
#Non tail
#1.sum of nature number
def nature(n):
    if n == 0:
        return 0
    
    return n + nature(n-1)
n = int(input("n: "))
print(nature(n))


#2.Power of a Number (X^N)
def power(n,x):
    if n==0 or x == 0:
        return 1
    x -= 1
    return n * power(n,x)
print(power(3,3))


#3. reverse a string  i/p = madhu  /////// o/p = uhdam
def string(s,le,emp):
    if le == -1:
        return emp
    else:

        emp += s[le]
        return string(s,le-1,emp)
s = str(input("s: "))
le = len(s) - 1
emp = ""
print(string(s,le,emp))

# 4.Count Digits in a Number // direct recursion
def digit(n,c):
    if n == 0:
        return c
    else:
        n = n // 10
        c +=1
        return digit(n,c)
c = 0
n = int(input("n: "))
print(digit(n,c))


##5. Fibonacci Series
def febionacci(n,t,f,s):
    if n == -1:
        return t
    else:
        t = f + s
        f = s
        s = t
        return febionacci(n-1,t,f,s)   
t = 0
f = 0
s = 1
n = int(input("n: "))
febionacci(n,t,f,s)
'''
def fib(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)
n = int(input("n: "))
print(fib(n))
































































