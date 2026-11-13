#python user define function
#Find the smallest Value
def my_min(a,b,c):
    s = a
    if b < s:
        a = s
    if c < s:
        c = s
    return s
print(my_min(5,10,25))

#Find the Largest Value
def my_max(a, b, c):
    L = a
    if b > L:
        L = b
    if c > L:
        L = c
    return L

print(my_max(5, 10, 25))

def my_abs(n):
    if n < 0:
        return -n
    return n
print(my_abs(-10))

#pow() – Power

def my_pow(a,b):
    r = 1
    for i in range(b):
        r *= a
    return r
print(my_pow(4,3))



#User-defined Square Root
def my_sqrt(n):
    i = 1
    while i * i <= n:
        if i * i == n:
            return i
        i+=1
print(my_sqrt(64))





























