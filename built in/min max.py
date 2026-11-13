# min
from mini import 
def mini(n):
    s = n[0]
    for i in n:
        if i < s:
            s = i
    return s
def maxi(n):
    L = n[0]
    for i in n:
        if i > L:
            L = i
    return L
n = [5, 10, 25, 3, 18]
print(mini(n))
print(maxi(n))
