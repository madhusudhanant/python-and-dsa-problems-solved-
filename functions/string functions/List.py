'''
Creating Lists and Accessing Elements
list1 = ["hey", "madhu", "ms"]
print(list1)

print(len(list1))  # Output: 3

list1 = {"abc", 34, True, 40, "male"}
print(type(list1))  

list1 = list(("apple", "mango", "orange", "beetroot", "carrot"))
print(list1)
print(list1[1])   # Output: mango
print(list1[-1])  # Output: orange
print(list1[2:4]) # Output: ['orange', 'beetroot']
print(list1[:3])  # Output: ['apple', 'mango', 'orange']
print(list1[1:])  # Output: ['mango', 'orange', 'beetroot', 'carrot']
print(list1[-4:-1])  # Output ['mango', 'orange', 'beetroot']


list1 = ["hey", "madhu", "ms"]
if "madhu" in list1:
    print("Yes, 'madhu' is in the list")

list1 = ["hey", "madhu", "ms"]
print(list1)
list1[1] = "systems"  # Replace element at index
print(list1)
list1[1] = "yogi"  # Replace element at index 1
print(list1)
list1[1:3] = ["kalpana", "sakthi"]  # Replace a range
print(list1)
list1[1:2] = ["kalpana", "sakthi1"]  # Replace one item with two
print(list1)

##ADD ITEMS
list1 = ["hey", "madhu", "ms"]
list1.insert(1,"sai")
print(list1)
list1.append("sakth")  # Add at the end
print(list1)
list1 = ["hey", "madhu", "ms"]
list2 = ["hello", "ms", "yuva"]
list1.extend(list2)
print(list1)

###REMOVING ITEMS
list1 = ["hey", "madhu", "ms", "yuva"]
list1.remove("yuva")
print(list1)

list1 = ["hey", "madhu", "ms"]

list1.pop(1)  # Remove by index
print(list1)

list1.pop()  # Remove last item

list1 = ["hey", "madhu", "ms"]
del list1[0]  # Delete by index
print(list1)

list1 = ["hey", "madhu", "ms"]
del list1  # Delete entire list
print(list1)


list1 = ["hey", "madhu", "ms"]
list1.clear()  # Clear all items from list

###LOOP THROUGH LISTS
list1 = ["hey", "madhu", "ms", "guru", "kanna"]
for x in list1:
    print(x)

list1 = ["hey", "madhu", "ms", "guru", "kanna"]
for i in range(len(list1)):
    print(list1[i])

i=0
while i<len(list1):
    print(list1[i])
    i+=1

list1 = ["hey", "madhu", "ms", "guru", "kanna"]
[print(x) for x in list1]  

#LIST COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
n =[]
for i in fruits:
    if "a" in i:
        n.append(i)
print(n)

n = [x for x in fruits if "a" in x]  # Same as above using list comprehension
print(n)

n = [x for x in fruits if "apple" != x]  
print(n)

###SORTING AND REVERSING LIST
fruits = ["cherry", "banana", "apple", "kiwi", "mango"]

fruits.sort()  
print(fruits)

fruits.sort(reverse=True)  
print(fruits)

fruits = ["apple", "DOG", "cherry", "kiwi", "MOON"]
fruits.sort(key=str.lower)  # Case-insensitive sort    consider evenly
print(fruits)
fruits = ["apple", "DOG", "cherry", "kiwi", "MOON"]
fruits.reverse()  
print(fruits)

######## COPYING AND JOINIG LIST
list1 = ["apple", "DOG", "cherry", "kiwi", "MOON"]
list2 = ["tom", "jerry", "hat", "try", "been"]

list1 = list2.copy()
print(list1)

list2 = ("tom", "jerry", "hat", "try", "been")

list2 = list(list1)
print(list2)
list1 = ["apple", "DOG", "cherry", "kiwi", "MOON"]
list2 = ["tom", "jerry", "hat", "try", "been"]

list3 = list1 + list2
print(list3)


Exercise 1: Reverse a given list in Python

a = [100, 200, 300, 400, 500]
a.reverse()
print(a)
output:- [500, 400, 300, 200, 100]

Exercise 2: Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
c = []
for x in range(len(list1)):
    c.append(list1[x]+list2[x])
print(c)

Exercise 3: Given a Python list of numbers. Turn every item of a list into its square

List = [1, 2, 3, 4, 5, 6, 7]
c=[]
for x in List:
    y = x**2
    c.append(y)
print(c)
#o/p [1, 4, 9, 16, 25, 36, 49]
Exercise 4: Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
c = []
for x in range(len(list1)):
    for i in range(len(list1)):
        c.append(list1[x]+ list2[i])
print(c)

#o/p ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

Exercise 5: Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()
for i in range(len(list1)):
    print(list1[i], list2[i])
o/p=
10 400
20 300
30 200
40 100

Exercise 6: Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for i in list1:
    if i == "":
        list1.remove(i)
print(list1)
#o/p ['Mike', 'Emma', 'Kelly', 'Brad']

Exercise 7: Add item 7000 after 6000 in the following Python List

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#o/p [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

Exercise 8: Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list
Sub List to be added = ["h", "i", "j"]

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub = ["h", "i", "j"]
for j in range(len(sub)):
    list1[2][1][2].append(sub[j])
print(list1)

#O/p ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

Exercise 9: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

list1 = [5, 10, 15, 20, 25, 50, 20]
for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break
print(list1)

Exercise 10: Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
c = []
for i in range(len(list1)):
    if list1[i] != 20:
        c.append(list1[i])
print(c)


#### Extra Questions ####
1. swap 1st and last elements in list

a = [12, 35, 9, 56, 24]

for i in range(len(a)):
    a[0], a[-1] = a[-1], a[0]
print(a)

a = [1,2,3]


a[0], a[-1] = a[-1], a[0]
print(a)

2.Python program to swap two elements in a list

Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
 
Examples:
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]

a = [23, 65, 19, 90]

a[0], a[2] = a[2], a[0]
print(a)

a = [1, 2, 3, 4, 5]

a[1], a[4] = a[4], a[1]
print(a)


3. Python – Swap elements in String list
Examples:  

Input: List ['Gfg', 'is', 'best', 'for', 'Geeks']
Output: ['efg', 'is', 'bGst', 'for', 'eGGks']

g -> e
e -> g

a = ['Gfg', 'is', 'best', 'for', 'Geeks']

a1=[]
s=""
for i in a:
    x = list(i)
    for k in range(len(x)):
        if x[k]=='G':
            x[k]='e'
        s = s + x[k]
    a1.append(s)
print(a1)

s1=a[0]


print(s1)
for i in range(len(a)):
    a[i][0],a[i+1][0]=a[i+1][0],a[i][0]

print(a)

Python | Ways to find length of list

Examples:  
The list is :

a = [1, 4, 5, 7, 8]
print(len(a))

4. Python program to find largest number in a list
Given two numbers, write a Python code to find the Maximum of these two numbers.
Examples: 
Input: a = [2,1,3,0,-1,-23,4]
Output: 4

Input: a = [-1,-23,-2,-45,-56]
Output: -1

a = [2,1,3,0.-1,-23,4]
f = max(a)
print(f)

a = [2,1,3000,0,-1,-23,4]
ma = a[0]

for i in range(len(a)):
    if ma <= a[i]:
        ma = a[i]
print(ma)

5. Python program to find smallest number in a list

Given two numbers, write a Python code to find the Minimum of these two numbers.
Examples:
Input: a = [2,1,3,0.-1,-23,4]
Output: -23

a = [2,1,3,0.-1,-23,4]
ma = a[0]

for i in range(len(a)):
    if ma >= a[i]:
        ma = a[i]
print("min is =",ma)

6. Check if element exists in list in Python

Example:
list = test_list = [1, 6, 3, 5, 3, 4]
Input: 3  # Check if 3 exist or not.
Output: True

Input: 7  # Check if 7 exist or not.
Output: False

a = [1, 6, 3, 5, 3, 4]
c = False
for i in range(len(a)):
    if 3 == a[i]:
        c = True
print(c)

7. Different ways to clear a list in Python
Example:
GEEK before clear: [6, 0, 4, 1]
GEEK after clear: []

a = [6, 0, 4, 1]
a.clear()
print(a)

8. Reversing a List in Python

Input: list = [4, 5, 6, 7, 8, 9]
Output : [9, 8, 7, 6, 5, 4] 

a = [4, 5, 6, 7, 8, 9]
h = len(a) - 1
c = []
for i in range(h,-1, -1):
    c.append(a[i])
print(c)


9. count the digits
a = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
c = 0
for i in range(len(a)):
    if x == a[i]:
        c = c + 1
print(c)

10. Find sum and average of List in Python

Given a List. The task is to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of elements.
Examples:
Input: [4, 5, 1, 2, 9, 7, 10, 8]
Output:
sum =  46
average =  5.75

a = [4, 5, 1, 2, 9, 7, 10, 8]
t = len(a)
y = sum(a)
g = y / t
print(g)

a = [4, 5, 1, 2, 9, 7, 10, 8]
s = 0
c = 0
for i in range(len(a)):
    s = s + a[i]
    c = c + 1
avg = s / c
print(avg)

11. Python | Sum of number digits in List
Examples:
The original list is : [12, 67, 98, 34]
List Integer Summation : [3, 13, 17, 7]

a = [12, 67, 98, 34]
g = []
for i in range(len(a)):
    k = a[i]
    su=0
    while k > 0:
        d = k % 10
        su = su+d
        k = k // 10
    g.append(su)
print(g)

12. Multiply all numbers in the list
Input :  list1 = [1, 2, 3] 
Output : 6 
Explanation: 1*2*3=6 

a = [1, 2, 3]
k = 1
for i in range(len(a)):
    k = k * a[i]
print(k)

13. second largest number in a list
Input: list1 = [10, 20, 4]
Output: 10

a = [10, 20, 4, 100, 99,101]

f = a[0]
s = a[0]
for i in range(len(a)):
    if f <= a[i]:
        f = a[i]
for i in range(len(a)):
    if a[i] > s and a[i] != f:
        s = a[i]
print(s)

14. print even numbers in a list

Input: list1 = [2, 7, 5, 64, 14]
Output: [2, 64, 14]

a = [2, 7, 5, 64, 14]
c = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        c.append(a[i])
print(c)

15. print odd numbers in a List
Input: list1 = [2, 7, 5, 64, 14]
Output: [7, 5]

a = [2, 7, 5, 64, 14]
c = []
for i in range(len(a)):
    if a[i] % 2 != 0:
        c.append(a[i])
print(c)

16. count Even and Odd numbers in a List
Input: list1 = [2, 7, 5, 64, 14]
Output: Even = 3, odd = 2

a = [2, 7, 5, 64, 14]
c = 0
c1 = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        c = c + 1
    else:
        c1 = c1 + 1
print("Even=",c, "Odd=",c1)


17. print positive numbers in a list

Input: list1 = [12, -7, 5, 64, -14]
Output: 12, 5, 64

a = [12, -7, 5, 64, -14]
c = []
for i in range(len(a)):
    if a[i] > 0:
        c.append(a[i])
print(c)

18. print negative numbers in a list
Input: list1 = [12, -7, 5, 64, -14]
Output: -7, -14

a = [12, -7, 5, 64, -14]
c = []
for i in range(len(a)):
    if a[i] < 0:
        c.append(a[i])
print(c)

19. Remove multiple elements from a list in Python
Input: [12, 15, 3, 10]
Output: Remove = [12, 3], New_List = [15, 10]

a = [12, 15, 3, 10]
r = [12, 3]
for i in r:
    a.remove(i)
print(a)

20. Remove empty tuples from a list
Input : tuples = [(), (‘ram’,’15’,’8′), (), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”,”),()]
Output : [(‘ram’, ’15’, ‘8’), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”, ”)]

a = [
    (),
    ("ram", "15", "8"),
    (),
    ("laxman", "sita"),
    ("krishna", "akbar", "45"),
    ("", ""),
    ()
]
for i in range(len(a)):
    if a[i] == ():
        a[i] = ""
c = []
for i in range(len(a)):
    if a[i] != "":
        c.append(a[i])
print(c)   

21. Program to print duplicates from a list of integers
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]

a = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
h = []
for i in range(len(a)):
    c = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            c = c + 1
    if c > 1 and a[i] not in h:
        h.append(a[i])  
print(h)

22. Remove empty List from List
The original list is : [5, 6, [], 3, [], [], 9]
List after empty list removal : [5, 6, 3, 9]

a = [5, 6, [], 3, [], [], 9]
c = []
for i in range(len(a)):
    if a[i] != []:
        c.append(a[i])
print(c)

23. Convert List to List of dictionaries
Input :
test_list = ["Gfg", 3, "is", 8]
key_list = ["name", "id"]
Output :
[{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}]

a = ["Gfg", 3, "is", 8, "madhu", 18]
b = ["name", "id"]
m = []
for i in range(0, len(a), 2):
    d = {}
    d[b[0]] = a[i]
    d[b[1]] = a[i + 1]
    m.append(d)
print(m)

24. Convert Lists of List to Dictionary
The original list is : [[‘a’, ‘b’, 1, 2], [‘c’, ‘d’, 3, 4], [‘e’, ‘f’, 5, 6]]
The mapped Dictionary : {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’): (1, 2)}


a = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
d = {}
for i in range(len(a)):
    key = (a[i][0], a[i][1])
    value = (a[i][2], a[i][3])
    d[key] = value
print(d)


25. Uncommon elements in Lists of List
Output : 
The original list 1 : [[1, 2], [3, 4], [5, 6]]
The original list 2 : [[3, 4], [5, 7], [1, 2]]
The uncommon of two lists is : [[5, 6], [5, 7]]

a = [[1, 2], [3, 4], [5, 6]]
b = [[3, 4], [5, 7], [1, 2]]
c = []
for i in range(len(a)):
    if a[i] not in b:
        c.append(a[i])
for j in range(len(b)):
    if b[j] not in a:
        c.append(b[j])
print(c)

+
26. select Random value form list of lists

import random
d = 1, 4 ,7 ,8, 2
f = random.choice(d)
print(f)

a = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
h=random.choice(a)
y=random.choice(h)
print(y)

27. Reverse Row sort in Lists of List
The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]


a = [[4, 1, 6], [7, 8], [4, 10, 8]]
for i in a:
    i.sort(reverse= True)
print(a)

28. Pair elements with Rear element in Matrix Row
The original list is : [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
The list after pairing is : [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]

a = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
c = []
for i in range(len(a)):
    x = []
    y = a[i][-1]
    for j in range(len(a[i])-1):
        x.append([a[i][j], y])
    c.append(x)
print(c)

29. count unique values inside a list
input_list = [1, 2, 2, 5, 8, 4, 4, 8]

Output:
	No of unique items are: 5

a = [1, 2, 2, 5, 8, 4, 4\\\\
h = []
c = 0
for i in range(len(a)):
    if a[i] not in h:
        h.append(a[i])
        c = c+1
print(c)


30. List product excluding duplicates

The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
Duplication removal list product : 90

a = [1, 3, 5, 6, 3, 5, 6, 1]
h = []
u = 1
for i in range(len(a)):
    if a[i] not in h:
        h.append(a[i])
        u= a[i] * u
print(u)

31. Extract elements with Frequency greater than K
Given a List, extract all elements whose frequency is greater than K.
Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 
Output : [4, 3] 
Explanation : Both elements occur 4 times.
a = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3
h = []
for i in range(len(a)):
    c = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            c += 1
    print("c", c)
    if c > k and a[i] not in h:
        h.append(a[i])      
print(h)

##########32. Test if List contains elements in Range

Output :

The original list is : [4, 5, 6, 7, 3, 9]
Does list contain all elements in range : True


33. three consecutive common numbers in Python

Our task is to print the element which occurs 3 consecutive times in a Python list.
Example :

Input : [4, 5, 5, 5, 3, 8]

Output : 5

a = [1, 1, 1, 64, 23, 64, 22, 22, 22]
h = []
for i in range(len(a)-2):
    if a[i] == a[i+1] and a[i+1] == a[i+2]:
        print(a[i])

34. program to find the Strongest Neighbour

Given an array arr[] of N positive integers. The task is to find the maximum for every adjacent pair in the array.
Examples:y
Input: 1 2 2 3 4 5
Output: 2 2 3 4 5

a = [1,2,2,3,4,5]
h = []
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        h.append(a[i])
    else:
        h.append(a[i+1])
print(h)

35. print all Possible Combinations from the three Digits
Examples:
Input: [1, 2, 3]

Output:
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1


a = [1, 2, 3]
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            if i != j and j != k and i != k:
                print(a[i], a[j], a[k])

36. find all the Combinations in the list with the given condition
[1]
[2]
[3]
[1, 2]
[1, 3]
[2, 3]
[1, 2, 3]


a = [1, 2, 3]
for i in range(len(a)):
    print([a[i]])
for i in range(len(a)):
    for j in range(i+1, len(a)):
        print([a[i],a[j]])
        
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1,(len(a))):
            print([a[i],a[j],a[k]])
    
37. get all unique combinations of two Lists
List_1 = ["a","b"]
List_2 = [1,2]
Unique_combination = [[('a',1),('b',2)],[('a',2),('b',1)]] 

list_1 = ["a","b"]
list_2 = [1,2]
r=1
d=[]
for i in range(len(list_1)):
    h=[]
    for j in range(len(list_2)):
        if i==1:
            x = list_1[j], list_2[r]
            r=r-1
            h.append(x)
        else:
            x = list_1[j], list_2[j]
            h.append(x)
    d.append(h)
print(d)

best solution

from itertools import permutations

a = ["a", "b"]
b = [1, 2]
h = []
for p in permutations(b):
    x = []
    for i in range(len(a)):
        x.append((a[i], p[i]))
    h.append(x)
print(h)


38. Remove all the occurrences of an element from a list in Python
Examples:
Input : 1 1 2 3 4 5 1 2 1 
Output : 2 3 4 5 2 


a= [1,1,2,3,4,5,1,2,1]
m = 0
max_e = [0]
for i in range(len(a)):
    c = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            c = c + 1
    if c > m:
        m = c
        max_e = a[i]
print(max_e)
h = []
for i in range(len(a)):
    if a[i] != max_e:
        h.append(a[i])
print(h)

39. Remove Consecutive K element records
Input :
test_list = [(4, 5), (5, 6), (1, 3), (0, 0)]
K = 0
Output : [(4, 5), (5, 6), (1, 3)]

a = [(4, 5), (5, 6), (1, 3), (0, 0)]
k = 0
h = []
for i in a:
    if i != (k,k):
        h.append(i)
print(h)

40. Replace index elements with elements in Other List

Output :
The original list 1 is : [‘Gfg’, ‘is’, ‘best’]
The original list 2 is : [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]
o/p; ['Gfg', 'is', 'best', 'is', 'Gfg', 'Gfg', 'Gfg', 'best', 'is', 'is', 'best', 'Gfg']

a = ["Gfg", "is", "best"]
b = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]
h = []
for i in b:
    h.append(a[i])
print(h)


#Function
def convert(a, b):
    h = []
    for i in b:
        h.append(a[i])
    return h


a = ["Gfg", "is", "best"]
b = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]

print(convert(a, b))


41. Retain records with N occurrences of K

Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 2 
Output : [(4, 5, 5, 4)]

a = [(4, 5, 5, 4), (5, 4, 3)]
k = 5
n = 2
h = []
for i in a:
    c = 0
    for j in i:
        if j == k:
            c+=1
    if c == n:
        h.append(i)
print(h)

#########doubt42. Program to Sort the list according to the column

a= [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
b = sorted(a, key=lambda x: x[0])
print(b)

43. Swap elements in String list #####fav sum####
Output :
The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']

a = ['Gfg', 'is', 'best', 'for', 'Geeks']
h = []
for i in a:
    i = i.replace('G', '#')
    i = i.replace('e', 'G')
    i = i.replace('#', 'e')
    h.append(i)
print(h)


44. Reverse All Strings in String List

Output :

The original list is : ['geeks', 'for', 'geeks', 'is', 'best']
The reversed string list is : ['skeeg', 'rof', 'skeeg', 'si', 'tseb']

a =  ['geeks', 'for', 'geeks', 'is', 'best']
h = []
for i in a:
    r=i[::-1]
    h.append(r)
print(h)

#using loop
a =  ['geeks', 'for', 'geeks', 'is', 'best']
h = []
for i in a:
    r = ""
    for j in i:
        r = j + r
    h.append(r)
print(h)

#list comprehension
a =  ['geeks', 'for', 'geeks', 'is', 'best']
h = [i[::-1] for i in a]
print(h)

45. program to find the character position of Kth word from a list of strings
Input : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K = 21 
Output : 0
Explanation : 21st index occurs in “geeks” and point to “g” which is 0th element of word.

a = ["geekforgeeks", "is", "best", "for", "geeks"]
k = 21
c = 0
for i in a:
    if c + len(i) > k:
        print(k-c)
        break
    c += len(i)

46. Extract words starting with K in String List

Given list of phrases, extract all the Strings with begin with character K.
Input : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I love G4G”], K = l 
Output : [‘learning’, ‘love’] 
Explanation : All elements with L as starting letter are extracted. 

a = ["Gfg is good for learning", "Gfg is for geeks", "I love G4G"]
h = []
for i in a:
    for j in i.split():
        if j[0] in "l":
            if j not in h:
                h.append(j)
print(h)


47. Prefix frequency in string List
The original list is : ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']
Strings count with matching frequency : 3

a = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']
p = "gfg"
c = 0
for i in a:
    if i.startswith(p):
        c+=1
print(c)

a = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']
p = "gfg"
c = 0
for i in a:
    if i[:len(p)] == p:
        c+=1
print(c)

48. Split String of list on K character

Output :

The original list is : ['Gfg is best', 'for Geeks', 'Preparing']
The extended list after split strings : ['Gfg', 'is', 'best', 'for', 'Geeks', 'Preparing']

a = ['Gfg is best', 'for Geeks', 'Preparing']
h = []
for i in a:
    for j in i.split():
        h.append(j)
print(h)
    

#list comprehension
a = ['Gfg is best', 'for Geeks', 'Preparing']
h = [j for i in a for j in i.split()]
print(h)

49. Split Strings on Prefix Occurrence
Input : test_list = [“geeksforgeeks”, “best”, “geeks”, “and”], pref = “geek” 
Output : [[‘geeksforgeeks’, ‘best’], [‘geeks’, ‘and’]] 
Explanation : At occurrence of string “geeks” split is performed.

a = ["geeksforgeeks", "best", "geeks", "and"]
p = "geek"
h = []
x = []
for i in a:
    if i[:len(p)] == p and x:
        h.append(x)
        x = []
    x.append(i)
h.append(x)
print(h)

50. Replace all Characters of a List Except the given character
Input : test_list = [‘G’, ‘F’, ‘G’, ‘I’, ‘S’, ‘B’, ‘E’, ‘S’, ‘T’], repl_chr = ‘*’, ret_chr = ‘G’ 
Output : [‘G’, ‘*’, ‘G’, ‘*’, ‘*’, ‘*’, ‘*’, ‘*’, ‘*’] 


a = ["G","F", "G", "I", "S", "B", "E", "S", "T"]
repl_chr = "*"
ret_chr = "G"
h =[]
for i in a:
    if i == "G":
        h.append(i)
    else:
        h.append("*")
print(h)

51. Remove words containing list characters
Output : 

The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
The character list is : ['g', 'o']
The filtered strings are : ['is', 'best']

a = ['gfg', 'is', 'best', 'for', 'geeks']
c = ['g', 'o']
h = []

for i in a:
    f = False
    for j in c:
        if j in i:
            f = True
            break
    if not f:
        h.append(i)

print(h)

52. Ways to remove multiple empty spaces from string List
The original list is : ['gfg', '   ', ' ', 'is', '            ', 'best']
List after filtering non-empty strings : ['gfg', 'is', 'best']

a = ['gfg', '   ', ' ', 'is', '            ', 'best']
h = []
for i in a:
    if i.strip():
        h.append(i)
print(h)

53. Add Space between Potential Words

Given list of Strings, task is to add a space before sequence which begin with capital letters.
Input : test_list = [“gfgBest”, “forGeeks”, “andComputerScienceStudents”] 
Output : [‘gfg Best’, ‘for Geeks’, ‘and Computer Science Students’] 
Explanation : Words segregated by Capitals.

a = ["gfgBest", "forGeeks", "andComputerScienceStudents"]
h = []
for i in a:
    s = ""
    for j in i:
        if j.isupper():
            s = s + " "
        s = s + j
    h.append(s)
print(h)


54. Filter the List of String whose index in second List contains the given Substring

x = ["Gfg", "is", "not", "best", "and", "not", "CS"]

y = ["Its ok", "all ok", "wrong", "looks ok", "ok", "wrong", "thats ok"]

sub = "ok"
h = []
for i in range(len(x)):
    for j in range(len(y)):
        if sub in y[j]:
            if j == i:
                h.append(x[i])
print(h)


55. Convert Character Matrix to single String

Output :

The original list is : [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
The String after join : gfgisbest

a =  [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
h = ""
for i in a:
    for j in i:
        h = h + j
print(h)

'''




















