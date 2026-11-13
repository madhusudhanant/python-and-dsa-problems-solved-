'''
Definition:
Tuples are ordered collections that are immutable (unchangeable) once defined.
1. Creating and Accessing Tuples
tuple1 = ("apple", "banana", "cherry")
print(tuple1)
print(len(tuple1))

2. Single Element Tuple
tuple1 = ("apple",)
print(type(tuple1))
tuple1 = ("apple")  #Not a tuple
print(type(tuple1))  #Output: <class 'str'>

3. Tuple with Mixed Data Types

tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple2)
print(tuple3)

4. Tuple Constructor

tuple1 = tuple(("apple", "banana", "cherry"))
print(tuple1)

5. Tuple Indexing and Slicing

tuple1 = ("apple", "banana", "cherry")
print(tuple1[1])

tuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple1[-4:-1])
print(tuple1[2:5])
print(tuple1[:4])
print(tuple1[2:])

tuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if "apple" in tuple1:
  print("Yes, 'apple' is in the fruits tuple")

7. Change Tuple Values (via list conversion)

tuple1 = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))
tuple1[1] = "pineapple"
print(tuple1)

x = ("apple", "banana", "cherry")
y = list(x)

y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")

thistuple = tuple(y)
del thistuple

10. Unpacking a Tuple

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

11. Using Asterisk for Variable Capture

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

12. Loop Through Tuple

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
for x in fruits:
    print(x)

for i in range(len(fruits)):
    print(fruits[i])

i = 0
while i < len(fruits):
    print(fruits[i])
    i+=1

13. Join and Multiply Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("a", "b" , "c")
mytuple = fruits * 2
print(mytuple)

######### exercise ###########
Exercise 1: Reverse the following tuple
Expected output:
[50, 40, 30, 20, 10]

t = ([10, 20, 30, 40, 50])
t.reverse()
print(t)

Exercise 2: Access value 20 from the following tuple

t = (["orange", [10, 20, 30], (5, 15, 25)])

for i in range(len(t)):
    print(t[1][1])
    break
output 20

Exercise 3: Create a tuple with single item 50
t = (50,)
print(t)

Exercise 4: Unpack the following tuple into 4 variables

t = (10, 20, 30, 40)
(a, b, c, d) = t
print(a) # should print 10
print(b) # should print 20
print(c) # should print 30
print(d) # should print 40

Exercise 5: Swap the following two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print("tuple =", tuple1)

Exercise 6: Copy element 44 and 55 from the following tuple into a new tuple

tuple1 = ([11, 22, 33, 44, 55, 66])
tuple2 = []
for i in range(len(tuple1)):
    if tuple1[i] == 44 or tuple1[i] == 55:
        tuple2.append(tuple1[i])
t1 = tuple(tuple2)
print("tuple2 =", t1)

Exercise 7: Modify the first item (22) of a list inside a following tuple to 222
Expected output:
(11, [222, 33], 44, 55)

t1 = ([11, [22, 33], 44, 55])
t1[1][0] = 222
z = tuple(t1)
print(z)

Exercise 8: Sort a tuple of tuples by 2nd item

Expected output:
(('c', 11), ('a', 23), ('d', 29), ('b', 37))  #assending order

t1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))

t = list(t1)

for i in range(len(t)):
    for j in range(i + 1, len(t)):
        if t[i][1] > t[j][1]:
            t[i], t[j] = t[j], t[i]

print(tuple(t))

Exercise 9: Counts the number of occurrences of item 50 from a tuple
Expected output: 2

t = (50, 10, 60, 70, 50)
c = list(t)

t = 0
for i in range(len(c)):
    if c[i] == 50: 
        t = t + 1
print(t)

t = (50, 10, 60, 70, 50)

print(t.count(50))

Exercise 10: Check if all items in the following tuple are the same
Expected output: True

t = (45, 45, 45, 45)
v = 0
r = t[0]
for i in range(len(t)):
    if t[i] == r:
        v = v + 1
    if v == len(t):
        print("True")

t = (45, 45, 45, 45)

print(len(set(t)) == 1)

###Python Tuple Exercise page no: 18 ###

1. Find the size of a Tuple in Python

Examples:
Tupe1 = ("A", 1,"B", 2, "C", 3)
Output:Size of Tuple1: 72bytes

import sys
t = ("A", 1,"B", 2, "C", 3)

print(sys.getsizeof(t))

2. Maximum and Minimum K elements in Tuple

Input : test_tup = (3, 7, 1, 18, 9), k = 2 
Output : (3, 1, 9, 18)


t = (3, 7, 1, 18, 9)
k = 2
y = sorted(t)
a = tuple(y[:k])
b = tuple(y[-k:])
print(a+b)

3. cube in each tuple

Input: list = [1, 2, 3]
Output: [(1, 1), (2, 8), (3, 27)]

a = [1, 2, 3]
h=[]
for i in a:
    k = i**3
    h.append((i,k))
print(h)

4. Adding Tuple to List and vice – versa

Output : 

The original list is : [5, 6, 7] t = (9,10)
The container after addition : [5, 6, 7, 9, 10]

l = [5, 6, 7]
t = (9, 10)
p = list(t)

#using loop
h=[]
for i in l:
    h.append(i)
for i in p:
    h.append(i)
print(h)

#concatenation
h = l + p
print(h)

#using extend()
l.extend(t)
print(l)

5. Sum of tuple elements

Output : 
The original tuple is : (7, 8, 9, 1, 10, 7)
The summation of tuple elements are : 42

t = (7, 8, 9, 1, 10, 7)
u = 0
for i in t:
    u = i+u
print(u)

6.Modulo of tuple elements

Output : 

The original tuple 1 : (10, 4, 5, 6)
The original tuple 2 : (5, 6, 7, 5)
The modulus tuple : (0, 4, 5, 1)

t1 =  (10, 4, 5, 6)
t2 =  (5, 6, 7, 5)
h = []
for i in range(len(t1)):
    h.append(t1[i] % t2[i])
y = tuple(h)
print(y)

7. Row wise element Addition in Tuple Matrix
Input :
test_list = [[(‘Gfg’, 3)], [(‘best’, 1)]]
cus_eles = [1, 2]
Output : [[(‘Gfg’, 3, 1)], [(‘best’, 1, 2)]]


t = [[("Gfg", 3)], [("best", 1)]]
a = [1,2]
h = []
for i in range(len(t)):
    for j in range(len(a)):
        c = t[i][0] + (a[i],)
    h.append([c])
print(h)

8. Update each element in tuple list

Output :
The original list : [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
List after bulk update : [(5, 7, 8), (6, 8, 10), (7, 12, 5)]

t = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
u = 4
h = []
for i in range(len(t)):
    f=[]
    for j in range(len(t[i])):
        f.append(t[i][j] + u)
    h.append(tuple(f))
print(h)

9. Multiply Adjacent elements

Output :
The original tuple : (1, 5, 7, 8, 10)
Resultant tuple after multiplication : (5, 35, 56, 80)


t = (1, 5, 7, 8, 10)
h = []
for i in range(len(t)-1):
    h.append(t[i]*t[i+1])
print(tuple(h))

10. Join Tuples if similar initial element
Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
Output : [(5, 6, 7, 8), (6, 10), (7, 13)]
explaination: Join tuples if the first element is the same.

t = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
d = {}
for i in t:
    if i[0] not in d:
        d[i[0]] = [i[0]]
    d[i[0]].append(i[1])

h =[]
for i in d:
    h.append(tuple(d[i]))
print(h)

11. All pair combinations of 2 tuples
Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]

from itertools import permutations
t1 = (7,2)
t2 = (7,8)
v = []

for i in t1:
    for j in t2:
        v.append((i,j))

for i in t2:
    for j in t1:
        v.append((i,j))
print(v)

12. Remove Tuples of Length K

Given list of tuples, remove all the tuples with length K.
Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 2
Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
Explanation : (4, 5) of len = 2 is removed.

t = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k = 2
h = []
for i in t:
    if k != len(i):
        h.append(i)
print(h)

13. Remove Tuples from the List having every element as None

Given a Tuple list, remove all tuples with all None values.
Input : test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )] 
Output : [(None, 2), (3, 4), (12, 3)] 


t = [(None, 2), (None, None), (3, 4), (12, 3), (None,)]
h = []
for i in t:
    c = 0
    for j in i:
        if j is None:
            c += 1
    if c != len(i):
        h.append(i)

print(h)

14. program to sort a list of tuples by second Item
Given a list of tuples, write a Python program to sort the tuples by the second item of each tuple.
Examples:
Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]

t = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[i][1] > t[j][1]:
            t[i], t[j] = t[j], t[i]
print(t)

15. Sort Tuples by Total digits  ##### hard sum to me ####

Given a Tuple List, perform sort on basis of total digits in tuple.
Examples:
Input : test_list = [(3, 4, 6, 723), (1, 2), (134, 234, 34)] 
Output : [(1, 2), (3, 4, 6, 723), (134, 234, 34


t = [(3, 4, 6, 723), (1, 2), (134, 234, 34)]

for i in range(len(t)):
    for j in range(i+1,len(t)):
        s1 = 0
        for x in t[i]:
            c = 0
            while x > 0:
                x = x// 10
                c = c + 1
            s1 = s1 + c
        s2 = 0
        for x in t[j]:
            c = 0
            while x > 0:
                x = x// 10
                c = c + 1
            s2 = s2 + c
        print("s1",s1)
        print("s2",s2)
        if s1 > s2:
            t[i], t[j] = t[j], t[i]
print(t)


16. Elements frequency in Tuple

Given a Tuple, find frequency of each element.
Input : test_tup = (4, 5, 4, 5, 6, 6, 5) 
Output : {4: 2, 5: 3, 6: 2}

t = (4, 5, 4, 5, 6, 6, 5) 
d ={}
for i in range(len(t)):
    c = 0
    for j in range(len(t)):
        if t[i] == t[j]:
            c+=1
    d[t[i]] = c
print(d)


17. Filter Range Length Tuples

Output :
The original list is : [(4, ), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]
The tuple list after filtering range records : [(5, 6), (2, 3, 5), (5, 9)]

explaination: Filter the tuple list by keeping only the tuples whose length falls within the specified range (the sample output implies lengths 2 to 3).

t = [(4,), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]
h = []
for i in t:
    if len(i) >= 2 and len(i) <= 3:
        h.append(i)
print(h)

18. Assign Frequency to Tuples

Given tuple list, assign frequency to each tuple in list.
Input : test_list = [(6, 5, 8), (2, 7), (6, 5, 8), (9, ), (2, 7)] 
Output : [(6, 5, 8, 2), (2, 7, 2), (9, 1)] 
Explanation : (2, 7) occurs 2 times, hence 2 is append in tuple.


t = [(6, 5, 8), (2, 7), (6, 5, 8), (9, ), (2, 7)]
h=[]
for i in range(len(t)):
    c = 0
    for j in range(len(t)):
        if t[i] == t[j]:
            c+=1
    y = t[i] + (c,)
    if y not in h:
        h.append(y)
print(h)


19. Records with Value at K index
Output :
The original list is : [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]
The tuples of element at Kth position : [(1, 3, 6), (6, 3, 0)]
     

t = [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]
k = 1 #index
h=[]
for i in t:
    if i[k] == 3:
        h.append(i)
print(h)

20. Test if tuple is distinct
Output :
The original tuple is : (1, 4, 5, 6, 1, 4)
Is tuple distinct ? : False

t = (1, 4, 5, 6, 1, 4)
h = []
for i in range(len(t)):
    if t[i] not in h:
        h.append(t[i])
if len(h) == len(t):
    print(True)
else:
    print(False)

21. program to find tuples which have all elements divisible by K from a list of tuples
Input : test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)], K = 6 
Output : [(6, 24, 12), (60, 12, 6)] 
Explanation : Both tuples have all elements multiple of 6

t = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
k = 6
h = []
for i in range(len(t)):
    c = 0
    for j in range(len(t[i])):
        if t[i][j]%k == 0:
            c +=1
    if c == len(t[i]):
        h.append(t[i])
print(h)

22. program to find Tuples with positive elements in List of tuples

Given a list of tuples. The task is to get all the tuples that have all positive elements.
Examples:
Input : test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)] 
Output : [(4, 5, 9)] 
Explanation : Extracted tuples with all positive elements


t = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)]
h = []
for i in range(len(t)):
    c = 0
    for j in range(len(t[i])):
        if t[i][j] > 0:
            c+=1
    if c == len(t[i]):
        h.append(t[i])
print(h)

23. Count tuples occurrence in list of tuples
Input = [[('hi', 'bye')], [('Geeks', 'forGeeks')],
         [('a', 'b')], [('hi', 'bye')], [('a', 'b')]]

Output:
defaultdict(<class 'int'>, {('Geeks', 'forGeeks'): 1, ('hi', 'bye'): 2, ('a', 'b'): 2})


t = [[('hi', 'bye')], [('Geeks', 'forGeeks')], [('a', 'b')], [('hi', 'bye')], [('a', 'b')]]
d ={}
for i in range(len(t)):
    c=0
    for j in range(len(t)):
        if t[i][0] == t[j][0]:
            c+=1
    d[t[i][0]] = c
print(d)

24. Removing duplicates from tuple

Output:
The original tuple is : (1, 3, 5, 2, 3, 5, 1, 1, 3)
The tuple after removing duplicates : (1, 3, 5, 2)

t = (1, 3, 5, 2, 3, 5, 1, 1, 3)
h = []
for i in t:
    if i not in h:
        h.append(i)
print(tuple(h))


or
print(tuple(set(t)))

25. Remove duplicate lists in tuples (Preserving Order)

Output : 
The original tuple is : ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])
The unique lists tuple is : [[4, 7, 8], [1, 2, 3], [9, 10, 11]]
 
t = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])
h = []
for i in t:
    if i not in h:
        h.append(i)
print(h)

26. Extract digits from Tuple list
Input : test_list = [(15, 3), (3, 9)] 
Output : [9, 5, 3, 1]


t = [(15, 3), (3, 9)]
h = []
for i in t:
    for j in i:
        while j > 0:
            a = j % 10
            j = j // 10
            if a not in h:
                h.append(a)     
print(list(reversed(h)))

27. Cross Pairing in Tuple List

Input : test_list1 = [(1, 7), (6, 7), (8, 100), (4, 21)], test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)]
Output : [(7, 3)]
Explanation : 1 occurs as tuple element at pos. 1 in both tuple, its 2nd elements are paired and returned.

t1 = [(1, 7), (6, 7), (8, 100), (4, 21)]
t2 = [(1, 3), (2, 1), (9, 7), (2, 17)]
h = []
for i in range(len(t1)):
    for j in range(len(t2)):
        if t1[i][0] == t2[j][0]:
            h.append((t1[i][1],t2[j][1]))
print(h)

28. Consecutive Kth column Difference in Tuple List

Examples:
Input : test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)], K = 0 
Output : [4, 4, 2] 
Explanation : 5 – 1 = 4, hence 4. 
 
Input : test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)], K = 2 
Output : [2, 4, 5] 
Explanation : 8 – 3 = 5, hence 5.


t = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]
k = 0 
h = []
for i in range(len(t)-1):
    d = abs(t[i][k] - t[i+1][k])
    h.append(d)
    #(or)
    if t[i][k] > t[i + 1][k]:
        h.append(t[i][k] - t[i + 1][k])
    else:
        h.append(t[i + 1][k] - t[i][k])
print(h)

29. Kth Column Product in Tuple List

Output :
The original list is : [(5, 6, 7), (1, 3, 5), (8, 9, 19)]
Product of Kth Column of Tuple List : 665

t = [(5, 6, 7), (1, 3, 5), (8, 9, 19)]
k = 2
y = 1
for i in range(len(t)):
    y *= t[i][k]
print(y)

30. Flatten tuple of List to tuple

Input : test_tuple = ([5], [6], [3], [8]) 
Output : (5, 6, 3, 8) 


e = ([5], [6], [3], [8])
h=[]
for i in e:
    for j in  i:
        h.append(j)
print(tuple(h))

31. Flatten Tuples List to String

Output : 
The original list : [('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]
Tuple list converted to String is : 1 4 6 5 8 2 9 1 10


t = [('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]
s = ""
for i in t:
    for j in i:
        s += j + " "
print(s)
        
32. program to sort a list of tuples alphabetically

Given a list of tuples, write a Python program to sort the tuples alphabetically by the first item of each tuple.
Examples:
Input: [("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]
Output: [('Abhishek', 29), ('Amana', 28), ('B', 'C'), ('Nikhil', 21), ('Zenat', 30)]


t = [("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]
for i in range(len(t)):
    for j in range(i + 1, len(t)):
        if t[i][0] > t[j][0]:
            t[i], t[j] = t[j], t[i]
print(t)

33. Combinations of sum with tuples in tuple list

Output :
The original list : [(2, 4), (6, 7), (5, 1), (6, 10)]
The Summation combinations are : [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]


t = [(2, 4), (6, 7), (5, 1), (6, 10)]
h=[]
for i in range(len(t)):
    for j in range(i+1, len(t)):
        y = t[i][0] + t[j][0]
        y1 = t[i][1] + t[j][1]
        h.append((y,y1))
print(h)

34. Custom sorting in list of tuples

Output :
The original list is : [(7, 8), (5, 6), (7, 5), (10, 4), (10, 1)]
The tuple after custom sorting is : [(10, 1), (10, 4), (7, 5), (5, 6), (7, 8)]


t = [(7, 8), (5, 6), (7, 5), (10, 4), (10, 1)]
for i in range(len(t)):
    for j in range(i+1, len(t)):
        if t[i][1] > t[j][1]:
            t[i],t[j]=t[j], t[i]
print(t)

35. program to convert tuple into list by adding the given string after every element
Given a Tuple. The task is to convert it to List by adding the given string after every element.
Examples:
Input : test_tup = (5, 6, 7), K = "Gfg" 
Output : [5, 'Gfg', 6, 'Gfg', 7, 'Gfg'] 
Explanation : Added "Gfg" as succeeding element.
 

t = (5, 6, 7)
k = "Gfg"
h = []
for i in t:
    h.append(i)
    h.append(k)
print(h)

36. Convert Tuple Matrix to Tuple List
Given a Tuple Matrix, flatten to tuple list with each tuple representing each column.
Input : test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)]] 
Output : [(4, 7, 10, 18), (5, 8, 13, 17)] 
Explanation : All column number elements contained together. 


t = [[(4, 5), (7, 8)], [(10, 13), (18, 17)]] 
h = []
u = []
u1=[]
for i in range(len(t)):
    for j in range(len(t[i])):
        u.append(t[i][j][0])
        u1.append(t[i][j][1])
h.append(tuple(u))
h.append(tuple(u1))
print(h)

37. Convert Tuple to Tuple Pair
Input : test_tuple = (‘A’, ‘B’, ‘C’)
Output : [(‘A’, ‘B’), (‘A’, ‘C’)]


t = ("A", "B", "C")
h=[]
for i in range(1,len(t)):
    y = t[0],t[i]
    h.append(y)
print(tuple(h))

38. Convert List of Lists to Tuple of Tuples
Input : test_list = [['Best'], ['Gfg'], ['Gfg']] 
Output : (('Best', ), ('Gfg', ), ('Gfg', ))    
   
t = [['Best'], ['Gfg'], ['Gfg']]
h=[]
for i in t:
    for j in i:
        h.append((j,))
print(tuple(h))

39.Convert Matrix to Custom Tuple Matrix

Input : test_list = [[4, 5], [7, 3]], add_list = [‘Gfg’, ‘best’] 
Output : [(‘Gfg’, 4), (‘Gfg’, 5), (‘best’, 7), (‘best’, 3)] 

t = [[4, 5], [7, 3]]
at = ["Gfg", "best"]
c=[]
for i in range(len(t)):
    for j in range(len(t[i])):
        c.append((at[i],t[i][j]))
print(c)
#or
x=0
for i in t:
    for j in i:
        c.append((at[x],j))
    x+=1
print(c)

40.page no: 28 Convert Nested Tuple to Custom Key Dictionary

Input : test_tuple = ((1, ‘Gfg’, 2), (3, ‘best’, 4)), keys = [‘key’, ‘value’, ‘id’]
Output : [{‘key’: 1, ‘value’: ‘Gfg’, ‘id’: 2}, {‘key’: 3, ‘value’: ‘best’, ‘id’: 4}]


t = ((1, "Gfg", 2), (3, "best", 4))
k = ["key", "value", "id"]
h = []
for i in range(len(t)):
    d={}
    for j in range(len(t[i])):
        d[k[j]] = t[i][j]
    h.append(d)
print(h)

41. Convert tuple to float value
t = (4, 56)
Output :
The original tuple : (4, 56)
The float after conversion from tuple is : 4.56

t = (4, 56)
s = str(t[0]) + "." + str(t[1])
print(float(s)) 

42. Extract tuples having K digit elements
Input : test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )], K = 2 
Output : [(34, 55), (12, 45), (78,)] 
Explanation : All tuples have numbers with 2 digits

t = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]
k = 2
h = []
for i in t:
    for j in i:
        c=0
        x = j
        while x >0:
            x = x//10
            c+=1
        if c != k:
            break
    else:
        h.append(i)
print(h)

#str conversion
t = [(54, 2), (34, 55), (222, 23), (12, 45), (78,)]
K = 2
a = []
for i in t:
    for j in i:
        if len(str(j)) != K:
            break
    else:
        a.append(i)

print(a)

43. (pg no: 29) Extract Symmetric Tuples

Input : test_list = [(6, 7), (2, 3), (7, 6)]
Output : {(6, 7)}
Input : test_list = [(6, 7), (2, 3)] Output : {}


t = [(6, 7), (2, 3), (7, 6)]
h=[]
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[i][0] == t[j][1] and t[i][1] == t[j][0]:
            h.append(t[i])
print(h)

44. Sort Tuples by their Maximum element
t = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)] 
Output : [(19, 4, 5, 3), (4, 5, 5, 7), (1, 3, 7, 4), (1, 2)] 
Explanation : 19 > 7 = 7 > 2

t = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]
c = []
for i in range(len(t)):
    mx = 0
    u = 0
    for j in range(len(t[i])):
        if t[i][j] > mx:
            mx = t[i][j]
    c.append((mx,t[i]))

for i in range(len(c)):
    for j in range(i + 1, len(c)):
        if c[i][0] < c[j][0]:
            c[i], c[j] = c[j], c[i]
h = []
for i in range(len(c)):
    h.append(c[i][1])
print(h)

#or inbuilt
t = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]
r = sorted(t, key=max, reveres=True)
print(r)

45. Remove nested records from tuple
The original tuple : (1, 5, 7, (4, 6), 10)
Elements after removal of nested records : (1, 5, 7, 10)


t = (1, 5, 7, (4, 6), 10)
h = ()
for i in t:
    if type(i) != tuple:
        h = h +(i,)
print(h)

f = [i for i in t if type(i) != tuple]
print(f)

46. Elements Frequency in Mixed Nested Tuple

Input : test_tuple = (5, (6, (7, 8, 6)))
Output : {5: 1, 6: 2, 7: 1, 8: 1} 


t = (5, (6, (7, 8, 6)))
d={}
def freq(t):
    for i in t:
        if type(i) == tuple:
            freq(i)
        else:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
freq(t)
print(d)

47. get unique elements in nested tuple

Output
The original list : [(3, 4, 5), (4, 5, 7), (1, 4)]
Unique elements in nested tuples are : [3, 4, 5, 7, 1]

t = [(3, 4, 5), (4, 5, 7), (1, 4)]
d={}
c=[]
def freq(t):
    for i in t:
        if type(i) == tuple:
            freq(i)
        else:
            if i not in d:
                d[i] = 1
                c.append(i)
            else:
                d[i] += 1
freq(t)
print(c)

48. Concatenate tuples to nested tuples
Output : 
The original tuple 1 : ((3, 4), )
The original tuple 2 : ((5, 6), )
Tuples after Concatenating : ((3, 4), (5, 6))


t1 = ((3, 4), )
t2 = ((5, 6), )

t = t1 + t2
print(t)

49. Sort by Frequency of second element in Tuple List

Input : test_list = [(6, 5), (1, 7), (2, 5), (8, 7), (9, 8), (3, 7)]
Output : [(1, 7), (8, 7), (3, 7), (6, 5), (2, 5), (9, 8)]
Explanation : 7 occurs 3 times as 2nd element, hence all tuples with 7, are aligned first

t = [(6, 5), (1, 7), (2, 5), (8, 7), (9, 8), (3, 7)]
d ={}
for i in t:
    if i[1] not in d:
        d[i[1]] = 1
    else:
        d[i[1]] += 1
t = list(t)
for i in range(len(t)):
    for j in range(i + 1, len(t)):
        if d[t[i][1]] < d[t[j][1]]:
            t[i], t[j] = t[j], t[i]            
print(t)

50.Sort lists in tuple
The original tuple is : ([7, 5, 4], [8, 2, 4], [0, 7, 5])
The tuple after sorting lists : ([4, 5, 7], [2, 4, 8], [0, 5, 7])

t = ([7, 5, 4], [8, 2, 4], [0, 7, 5])
h =[]
for i in t:
    y = sorted(i)
    h.append(y)
print(tuple(h))

51. Order Tuples by List
t = [('Gfg', 10), ('best', 3), ('CS', 8), ('Geeks', 7)]
ord_list = ['Geeks', 'best', 'CS', 'Gfg']
Output : [(‘Geeks’, 7), (‘best’, 3), (‘CS’, 8), (‘Gfg’, 10)] 

t = [('Gfg', 10), ('best', 3), ('CS', 8), ('Geeks', 7)]
ord_list = ['Geeks', 'best', 'CS', 'Gfg']
h=[]
for i in ord_list:
    for j in t:
        if i == j[0]:
            h.append(j)
print(h)

52. Filter Tuples by Kth element from List
t = [("GFg", 5, 9), ("is", 4, 3), ("best", 10, 29)]
check_list = [4, 2, 3, 10]
K = 2
Output : [(‘is’, 4, 3)]
Explanation : 3 is 2nd element and present in list, hence filtered tuple

t = [("GFg", 5, 9), ("is", 4, 3), ("best", 10, 29)]
check_list = [4, 2, 3, 10]
k = 2
h =[]
for i in t:
    if i[k] in check_list:
         h.append(i)
print(h)

53. Closest Pair to Kth index element in Tuple
test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
tup = (17, 23)
K = 2
Output : (19, 23)

t = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
tup = (17, 23)
k = 2
ans=t[0]
mn = abs(t[0][k-1] - tup[k-1])
for i in t:
    d = abs(i[k-1] - tup[k-1])
    if d < mn:
        mn = d
        ans = i
print(ans)

54. Tuple List intersection (Order irrespective)
test_list1 = [(3, 4), (5, 6)]
test_list2 = [(5, 4), (4, 3)] 
Output : {(3, 4)}


t1 = [(3, 4), (5, 6)]
t2 = [(5, 4), (4, 3)] 
h = []
for i in t1:
    for j in t2:
        if sorted(i) == sorted(j):
            h.append(i)
print(h)

55.| Intersection in Tuple Records Data
The original list 1 is : [('gfg', 1), ('is', 2), ('best', 3)]
The original list 2 is : [('i', 3), ('love', 4), ('gfg', 1)]
Output :
The Intersection of data records is : [('gfg', 1)]

t1 = [('gfg', 1), ('is', 2), ('best', 3)]
t2 = [('i', 3), ('love', 4), ('gfg', 1)]
h=[]
for i in t1:
    for j in t2:
        if i == j:
            h.append(i)
print(h)

56. Unique Tuple Frequency (Order Irrespective)
Input : test_list = [(3, 4), (1, 2), (4, 3), (3, 4)]
Output : 2

t = [(3, 4), (1, 2), (4, 3), (3, 4)]
h = []
for i in t:
    x = sorted(i)
    if x not in h:
        h.append(x)
print(len(h))  

57. Skew Nested Tuple Summation
Input : test_tup = (5, (6, (1, (9, None))))
Output : 21
Explanation : 9 + 6 + 5 + 1 = 21.

t = (5, (6, (1, (9, None))))

def skew(t):
    s = 0
    for i in t:
        if type(i) == tuple:
            s+=skew(i)
        elif i != None:
            s+=i
    return s
print(skew(t))

58. Convert Binary tuple to Integer
Input : test_tup = (1, 1, 0) 
Output : 6 
Explanation : 4 + 2 = 6. 
Input : test_tup = (1, 1, 1) 
Output : 7 
Explanation : 4 + 2 + 1 = 7.
(1, 1, 0)

Position:  2   1   0
Power:    2² 2¹ 2⁰
Value:     4  2  1

t = (1, 1, 0)
p = len(t) - 1
s = 0
for i in t:
    s = s + i * (2 ** p)
    p = p -1
print(s)
    
59. Tuple XOR operation
Output :
The original tuple 1 : (10, 4, 6, 9)
The original tuple 2 : (5, 2, 3, 3)
The XOR tuple : (15, 6, 5, 10)

t1 = (10, 4, 6, 9)
t2 = (5, 2, 3, 3)
h = ()
for i in range(len(t1)):
    h = h + (t1[i]^t2[i],)
print(h)

60. AND operation between Tuples
Output :
The original tuple 1 : (10, 4, 5)
The original tuple 2 : (2, 5, 18)
Resultant tuple after AND operation : (2, 4, 0)

t1 = (10, 4, 5)
t2 = (2, 5, 18)
h = ()
for i in range(len(t1)):
    h = h + (t1[i]&t2[i],)
print(h)

61. Elementwise AND in tuples
Output :
The original tuple 1 : (10, 4, 6, 9)
The original tuple 2 : (5, 2, 3, 3)
The AND tuple : (0, 0, 2, 1)

t1 = (10, 4, 6, 9)
t2 = (5, 2, 3, 3)
h = ()
for i in range(len(t1)):
    h = h + (t1[i]&t2[i],)
print(h)

'''












































