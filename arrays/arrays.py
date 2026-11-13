'''
###ARRAYS
a=int(input("Enter a"))
z=[]
for i in range(a):
    b=int(input("Enter b"))
    z.append(b)
print("Array = ",z)
print("First element in Array ",z[0])

#1. find and print 3rd AND 5TH ELEMENTS IN ARRAY

n =  int(input("Enter n:" ))
               
x = []
            
for i in range(n):
    b = int(input("Enter b: "))
    x.append(b)
print("ARRAY = ", x)
print("third elemet",x[2])
print( "5th elemnt", x[4])

   
#2.find and print 1st AND last ELEMENTS IN ARRAY


n =  int(input("Enter n:" ))
               
x = []
            
for i in range(n):
    b = int(input("Enter b: "))
    x.append(b)
print("ARRAY = ", x)
print("first elemet",x[0])
print( "lastelemnt", x[-1])
               
#3.change 2nd number to 50


n =  int(input("Enter n:" ))
               
x = []

c = 50
for i in range(n):
    b = int(input("Enter b: "))
    x.append(b)
x[1] = 50
    
print("ARRAY = ", x)
print("second elemet",x[0])


#4.[10,20,30,40,50] swap first and last elemet

n =  int(input("Enter n:" ))       
x = []
c = 50
for i in range(n):
    b = int(input("Enter b: "))
    x.append(b)
p = x[0]
q = x[-1]
x[0] = q
x[-1] = p
print("ARRAY = ", x)

#5. [10,20,30,40,50] check value exists 
n =  int(input("Enter n:" ))       
x = []
c = 50
for i in range(n):
    b = int(input("Enter b: "))
    x.append(b)
k = int(input("check value: "))
for j in range(n):
    if k == x[j]:
        print(k, "is exist")

#6. [10,20,30,40,50] index of an array element
n =  int(input("Enter n:" ))       
x = []

for i in range(n):
    b = int(input("Enter b: "))
    x.append(b)
k = int(input("check value: "))

for j in range(n):
    if k == x[j]:
        print([j], "is the index")

#7. remove a specific element from a array
n = int(input("n: "))

x = []

for i in range(n):
    a = int(input("enter values: "))
    x.append(a)
print(x)

k = int(input("remove value: "))
for j in range(n):
    if k == x[j]:
        x.remove(k)
        print(x)

for d in range(n-1):
    print(x[d])

#8. sum of an array
n = int(input("n: "))
x = []

for i in range(n):
    a = int(input("enter values: "))
    x.append(a)
b = 0
for j in range(n):
    b = b + x[j]
print(b)

#9 addition of two single dimentional arrays
n1 = int(input("array 1 count: "))
n2 = int(input("array 2 cpunt: "))

if n1 == n2:
    x1 = []
    for i in range(n1):
        a1 = int(input("array 1: "))
        x1.append(a1)
        
    x2 = []
    for j in range(n1):
        a2 = int(input("array 2: "))
        x2.append(a2)
        
    f = []
    for k in range(n1):
        h = x1[k] + x2[k]
        f.append(h)
    print(f)
 

# 10 reverse an array of integer values  

n = int(input("n: "))
x = []

for i in range(n):
    a = int(input("enter values: "))
    x.append(a)
#reverse
h = []

for j in range(n - 1, -1, -1):
    h.append(x[j])
print("Reversed =",h)

#11. arranging the numbers in ascending order 
n = int(input("n: "))
x = []
for i in range(n):
    a = int(input("enter values: "))
    x.append(a)

for i in range(n):
    for j in range(i+1,n):
        if x[i] > x[j]:
            s = x[i]
            x[i] =  x[j]
            x[j] = s
print(x)

#12. arranging the numbers in adcending order
n = int(input("n: "))
x = []
for i in range(n):
    a = int(input("enter values: "))
    x.append(a)

for i in range(n):
    for j in range(i+1,n):
        if x[i] < x[j]:
            s = x[i]
            x[i] =  x[j]
            x[j] = s
print(x)

#13. largest number in the array
'''
n = int(input("n: "))
x = []
for i in range(n):
    a = int(input("enter values: "))
    x.append(a)
mx = x[0] 
for i in range(n):
    for j in range(i + 1, n):
        if mx < x[j]:
            mx = x[j]
print("largest number is ", mx)

'''
#14. small number in the array
n = int(input("n: "))
x = []
for i in range(n):
    a = int(input("enter values: "))
    x.append(a)
mx = x[0] 
for i in range(n):
   
    for j in range(i + 1, n):
        if mx > x[j]:
            mx = x[j]
print("smallest number is ", mx)


#15 2nd largest number in array while in ascending order

n = int(input("n: "))

x = []

for i in range(n):
    a = int(input("a: "))
    x.append(a)
for i in range(n):
    for j in range(i+1, n):
        if x[i] > x[j]:
            x[i], x[j] = x[j], x[i]
print(x)
print("2nd largest number in array is", x[-2])


#16. 2nd smallest number in array while in ascending order

n = int(input("n: "))

x = []

for i in range(n):
    a = int(input("a: "))
    x.append(a)
for i in range(n):
    for j in range(i+1, n):
        if x[i] > x[j]:
            x[i], x[j] = x[j], x[i]
print(x)
print("2nd smallest number in array is", x[1])


#17. 2nd largest number in array while in decending order

n = int(input("n: "))

x = []

for i in range(n):
    a = int(input("a: "))
    x.append(a)
for i in range(n):
    for j in range(i+1, n):
        if x[i] < x[j]:
            x[i], x[j] = x[j], x[i]
print(x)
print("2nd largest number in array is", x[1])


#18. 2nd smallest number in array while in decending order

n = int(input("n: "))

x = []

for i in range(n):
    a = int(input("a: "))
    x.append(a)
for i in range(n):
    for j in range(i+1, n):
        if x[i] < x[j]:
            x[i], x[j] = x[j], x[i]
print(x)
print("2nd largest number in array is", x[-2])


# 19. find the duplicates elements in the array
n = int(input("n: "))

x = []

for i in range(n):
    a = int(input("a: "))
    x.append(a)
    
for i in range(n):
    for j in range(i+1, n):
        if x[i] > x[j]:
            x[i], x[j] = x[j], x[i]
print(x)          
u = []              
for k in range(n):
    for p in range(k + 1, n):
        if x[k] == x[p]:
            u.append(x[k])    
print(u)

    
# 20. find duplicate value of an array of string values
n = int(input("n: "))

x = []

for i in range(n):
    a = str(input("a: "))
    x.append(a)
    
for i in range(n):
    for j in range(i+1, n):
        if x[i] > x[j]:
            x[i], x[j] = x[j], x[i]
print(x)          
u = []              
for k in range(n):
    for p in range(k + 1, n):
        if x[k] == x[p]:
            u.append(x[k])    
print(u)

# 21. find the common arrays between two arrays of integers

n1 = int(input("n1: "))
n2 = int(input("n2: "))
x1 = []
x2 = []
for i in range(n1):
    a1 = int(input("a1: "))
    print("-----")
    a2 = int(input("a2: "))
    x1.append(a1)
    x2.append(a2)

print("input of x1: ",x1)
print("input of x2: ",x2)
    
u = []
for k in range(n1):
    for p in range(n1):
        if x1[k] == x2[p]:
            if x1[k] not in u:
                u.append(x1[k])    
print("common elementsis ",u)


#22 find the common arrays between two arrays in string values

n1 = int(input("n1: "))
n2 = int(input("n2: "))
x1 = []
x2 = []
for i in range(n1):
    a1 = str(input("a1: "))
    print("-----")
    a2 = str(input("a2: "))
    x1.append(a1)
    x2.append(a2)
print("input of x1: ",x1)
print("input of x2: ",x2)
u = []
for i in range(n1):
    for j in range(n1):
        if x1[i] == x2[j]:
            if x1[i] not in u:
                u.append(x1[i])
print("common elementsis ",u)

# 23 remove duplicate elements in array

n1 = int(input("n1: "))

x1 = []

for i in range(n1):
    a1 = int(input("a1: "))
    x1.append(a1)
print("input of x1: ",x1)
u = []
for i in range(n1):
    for j in range(n1):
        if x1[i] == x1[j]:
            if x1[i] > 2:
                u.append(x1[i])
print("non duplicates",u)


# 24. equalty of two arrays
n1 = int(input("n1: "))
n2 = int(input("n2: "))
x1 = []
x2 = []
if n1 == n2:
    for i in range(n1):
        a1 = int(input("a1: "))
        print("-----")
        a2 = int(input("a2: "))
        x1.append(a1)
        x2.append(a2)
    print("input of x1: ",x1)
    print("input of x2: ",x2)
else:
    print("length is not same")
a = 0  
u = []
for i in range(n1):
    for j in range(n1):
        if x1[i] == x2[j]:
            a = a + 1
            u.append(x1[i])
       
if a == n1:
    print(u)
else:
    print("not same")

# 25. add 0 in end 
n1 = int(input("n1: "))

x1 = []

for i in range(n1):
    a1 = int(input("a1: "))
    x1.append(a1)
     
        
print("input of x1: ",x1)
a = 0 
u = []
for i in range(n1):
    if x1[i] != 0:
        u.append(x1[i])
    else:
        a = a + 1
for j in range(a):
    u.append(0)
print(u)



# 26. odd or even  of two arrays
n1 = int(input("n1: "))
x1 = []
odd = []
even = []
for i in range(n1):
    a1 = int(input("a1: "))
    x1.append(a1)
    
for i in range(n1):
    if x1[i] % 2 == 0:
        even.append(x1[i])
        
    
    if x1[i] % 2 != 0:
        odd.append(x1[i])
    
print("odd num",odd)
print("even", even)


# 27. avg
n1 = int(input("n1: "))
x1 = []
for i in range(n1):
    a1 = int(input("a1: "))
    x1.append(a1)
    
for i in range(n1):
    for j in range(i + 1, n1):
        if x1[i] > x1[j]:
            x1[i], x1[j] = x1[j], x1[i]      
print(x1)

avg = n1 - 2
a = 0

for k in range(1, n1 - 1):
    a = a + x1[k]
b = a / avg
print(int(b))
    

# 28. without 0 and -1
n1 = int(input("n1: "))
x1 = []
a = 0
b = 0

for i in range(n1):
    a1 = int(input("a1: "))
    x1.append(a1)
    
for i in range(n1):
    if x1[i] == 0:
        a = 1
    elif x1[i] == -1:
        b =  1
if a == 1 or b == 1:
    print("have 0 and -1")
else:
    print("no 0 and -1")

# 29. find leader
n = int(input("n: "))
x = []


for i in range(n):
    a = int(input("a: "))
    x.append(a)
for i in range(n):
    c=0
    for j in range(i + 1, n):
        if x[i] < x[j]:
            c=1
    if c == 0:
        print("LEADER", x[i])
print(x)

#30 0s left side 1s right side
n = int(input("n: "))
x = []


for i in range(n):
    a = int(input("a: "))
    x.append(a)
a = []
b = []
c = []
for i in range(n):
    if x[i] == 0:
        a.append(x[i])
    elif x[i] == 1:
        b.append(x[i])
    else:
        c.append(x[i])
print(a)
print(b)
print(c)
d = a + c + b
print(d)

'''





































  







