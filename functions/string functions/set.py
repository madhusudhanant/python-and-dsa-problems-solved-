'''
Definition:
A set is a collection that is unordered, unindexed, and contains no duplicate elements. Sets are defined using curly braces {}.

1. Creating and Accessing Sets
thisset = {"apple", "banana", "cherry"}
print(thisset)


s = {"apple", "banana", "cherry"}

for x in s:
    print(x)
print("cherry" in s)

2. Adding and Updating Items
s = {"apple", "banana", "cherry"}
s.add("kiwi")
print(s)
s = {"apple", "banana", "cherry"}
s.update(["a", "b", "c"])
print(s)

3. Removing Items

s = {"apple", "banana", "cherry"}
s.remove("dog")
print(s)

s = {"apple", "banana", "cherry"}
s.pop()
print(s)

#4. Set Operations
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

#5. Set Comparisons
x = {"a", "b", "c"}
y = {"apple", "b", "cherry"}
z = x.intersection(y)
print(z)

x = {"apple", "banana", "cherry"}
result = x.intersection({"banana", "cherry"})
print(result)

#difference
x = {"a", "b", "c"}
y = {"apple", "b", "cherry"}
r = x.difference(y)
print(r)

r2 = y.difference(x)
print(r)
print(r2)

x = {"a", "b", "c"}
z = x.isdisjoint({"facebook", "icrosoft"})
print(z)

z = {"a", "b", "c"}.issubset({"a", "b", "c", "d"})
print(z)

z = {"a", "b", "c", "d"}.issuperset({"b", "c"})
print(z)

########### Exercise ############
Exercise 1: Add a list of elements to a given set
Expected output:
Note: Set is unordered.
{'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}

s = {"Yellow", "Orange", "Black"}
l = ["Blue", "Green", "Red"]
s.update(l)
print(s)

Exercise 2: Return a new set of identical items from a given two set
identical items means duplicate elements—elements that have the same value.
Expected output:
{40, 50, 30}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

r= set1.intersection(set2)
print(r)

Exercise 3: Returns a new set with all items from both sets by removing duplicates
Expected output:
{70, 40, 10, 50, 20, 60, 30}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
r = set1.union(set2)
print(r)

Exercise 4: Given two Python sets, update the first set with items that exist only in the first set and not in the second set.
Expected output:
set1 {10, 30}

set1 = {10, 20, 30}
set2 = {20, 40, 50}

r = set1.difference(set2)
print(r)

Exercise 5: Remove items 10, 20, 30 from the following set at once
{40, 50}

set1 = {10, 20, 30, 40, 50}
s = list(set1)
d = [10,20,30]
for i in d:
    if i in s:
        s.remove(i)

print(set(s))
            
Exercise 6: Return a set of all elements in either A or B, but not both
expected output: [20, 10, 70, 60]
r = set1.symmetric_difference(set2)
print(r)

s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
set1 = list(s1)
set2 = list(s2)
print(s1^s2)

z = []
for i in range(len(set1)):
    c = 0
    for j in range(len(set2)):
        if set1[i] == set2[j]:
            c = c + 1
    if c == 0:
        z.append(set1[i])

for i in range(len(set2)):
    c = 0
    for j in range(len(set1)):
        if set2[i] == set1[j]:
            c = c + 1
    if c == 0:
        z.append(set2[i])
print(z)

Exercise 7: Check if two sets have any elements in common. If yes, display the common elements.
Expected output:
Two sets have items in common
{10}         # intersection only return duplicates

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
r = set1.intersection(set2)
print(r)

Exercise 8: Update set1 by adding items from set2, except common items
Expected output:
{70, 10, 20, 60}
The symmetric_difference() method returns a new set containing elements that are in either set, but not in both

s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
r = s1.symmetric_difference(s2)
print(r)
print(s1^s2)

Exercise 9: Remove items from set1 that are not common to both set1 and set2
Expected output:
{40, 50, 30}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

r = set1.intersection(set2)
print(r)

######## PYTHON SET EXERCISE pg: 34 #####
    
1. size of a Set in Python

import sys
set1 = {"A", 1, "B", 2, "C", 3}

print(sys.getsizeof(set1),"Bytes")

2. Iterate over a set in Python

test_set = set("geEks")
Output: 
 
g
k
E
s
e


s = set("geEks")
for i in s:
    print(i)

3. Maximum and Minimum in a Set

Input : set = ([8, 16, 24, 1, 25, 3, 10, 65, 55])
Output : max is 65


s = ([8, 16, 24, 1, 25, 3, 10, 65, 55])
f = max(s)

mx = s[0]
for i in s:
    if i > mx:
        mx = i
print(mx)

4.  Remove items from Set
Examples:
Input : s = {12, 10, 13, 15, 8, 9}
Output :
{9, 10, 12, 13, 15}
{10, 12, 13, 15}
{12, 13, 15}
{13, 15}
{15}
set()



s = {12, 10, 13, 15, 8, 9}

while len(s) > 0:
    s.pop()
    print(s)

for i in range(len(s)):
    s.pop()
    print(s)

5. Check if two lists have at-least one element common
Given two lists a, b. Check if two lists have at least one element common in them. 

Examples:
Input : a = [1, 2, 3, 4, 5]
        b = [5, 6, 7, 8, 9]
Output : True
the intersection is not empty, the answer is: True

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
s1 = set(a)
s2 = set(b)
print(len(s1 & s2) > 0)

6. Find common elements in three lists using sets

Input : ar1 = [1, 5, 10, 20, 40, 80]
        ar2 = [6, 7, 20, 80, 100]
        ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

Output : [80, 20]


ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)
print(list(s1 & s2 & s3))

7. Find missing and additional values in two lists
Input : list1 = [1, 2, 3, 4, 5, 6] 
        list2 = [4, 5, 6, 7, 8] 
Output : Missing values in list1 = [8, 7] 
         Additional values in list1 = [1, 2, 3] 
         Missing values in list2 = [1, 2, 3] 
         Additional values in list2 = [7, 8] 


Easy Trick to Remember
s1 & s2 → Common elements
s1 | s2 → All unique elements
s1 - s2 → Only in s1
s2 - s1 → Only in s2

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

s1 = set(list1)
s2 = set(list2)

print("Missing values in list1 =", list(s2 - s1))
print("Additional values in list1 =", list(s1 - s2))

print("Missing values in list2 =", list(s1 - s2))
print("Additional values in list2 =", list(s2 - s1))


8. Difference between two lists
Examples:  
Input:
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35] 
Output:
[10, 20, 30, 15]

list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]
s1 = set(list1)
s2 = set(list2)
print(s1 - s2)

9. Set difference to find lost element from a duplicated array

Input:  A = [1, 4, 5, 7, 9]
        B = [4, 5, 7, 9]
Output: [1]
1 is missing from second array.

A = [1, 4, 5, 7, 9]
B = [4, 5, 7, 9]

s1 = set(A)
s2 = set(B)

print(list(s1 ^ s2))

10. (page: 38) program to count number of vowels using sets in given string
Examples:
Input : GeeksforGeeks
Output : No. of vowels : 5


st = "GeeksforGeeks"

v = {"a","e","i","o","u"}
c = 0
for i in st.lower():
    if i in v:
        c+=1
print("No. of vowels :",c)

11. Concatenated string with uncommon characters in Python
Examples:
Input : S1 = “aacdb”, S2 = “gafd”
Output : “cbgf”



s1 = "aacdb"
s2 = "gafd"

a = set(s1)
b = set(s2)
print(a)
print(b)
c = ""

for i in s1:
    if i not in b:
        c+= i
        print("c=",c)

for i in s2:
    if i not in a:
        c+= i

print(c)

12. Program to accept the strings which contains all vowels
Examples : 
Input : geeksforgeeks
Output : Not Accepted
All vowels except 'a','i','u' are not present
Input : ABeeIghiObhkUul
Output : Accepted
All vowels are present


a = "ABeeIghiObhkUul"
v = {"a", "e", "i", "o", "u"}

for i in v:
    if i not in a.lower():
        print("not Accepted")
        break
else:
    print("Accepted")


a = "ABeeIghiObhkUul"
v = {"a", "e", "i", "o", "u"}

s = set(a.lower())
if len(s & v) == 5:
    print("Accepted")
else:
    print("Not Accepted")

13. Check if a given string is binary string or not
Given string str. The task is to check whether it is a binary string or not. 
  
Input: str = "01010101010"
Output: Yes
Input: str = "geeks101"
Output: No
 
s = "01010101010"
for i in s:
    if i != "0" and i != "1":
        print("no")
        break
else:
    print("yes")

14. set to check if string is pangram
Given a string, check if the given string is pangram or not.

Examples: 
Input : The quick brown fox jumps over the lazy dog
Output : The string is a pangram


s = "The quick brown fox jumps over the lazy dog"

a = set()
for i in s.lower():
    if i >= "a" and i <= "z":
        a.add(i)
if len(a) == 26:
    print("The string is a pangram")
else:
    print("The string is not pangram")

15.Pairs of complete strings in two sets

Examples:
Input : set1[] = {"abcdefgh", "geeksforgeeks",
                 "lmnopqrst", "abc"}
        set2[] = {"ijklmnopqrstuvwxyz", 
                 "abcdefghijklmnopqrstuvwxyz", 
                 "defghijklmnopqrstuvwxyz"} 
Output : 7
The total complete pairs that are forming are:
"abcdefghijklmnopqrstuvwxyz"
"abcdefghabcdefghijklmnopqrstuvwxyz"
"abcdefghdefghijklmnopqrstuvwxyz"
"geeksforgeeksabcdefghijklmnopqrstuvwxyz"
"lmnopqrstabcdefghijklmnopqrstuvwxyz"
"abcabcdefghijklmnopqrstuvwxyz"
"abcdefghijklmnopqrstuvwxyz"
 

s1 = {"abcdefgh", "geeksforgeeks",
                 "lmnopqrst", "abc"}
s2 = {"ijklmnopqrstuvwxyz", 
                 "abcdefghijklmnopqrstuvwxyz", 
                 "defghijklmnopqrstuvwxyz"} 
c = 0
for i in s1:
    for j in s2:
        s = i+j
        if len(set(s)) == 26:
            c+=1
print(c)

16. given string is Heterogram or not

Input : S = "the big dwarf only jumps"
Output : Yes
Each alphabet in the string S is occurred
only once.


s = "the big dwarf only jumps"
a = set()
for i in s.lower():
    if i >= "a" and i <= "z":
        if i in a:
            print("No")
            break
        a.add(i)
else:
    print("Yes")

17. convert Set into Tuple and Tuple into Set
Example:
Input: {'a', 'b', 'c', 'd', 'e'}
Output: ('a', 'c', 'b', 'e', 'd')
Explanation: converting Set to tuple


s = {'a', 'b', 'c', 'd', 'e'}
y = tuple(s)
print(y)
print(set(y))


18. Convert set into a list

Input : {1, 2, 3, 4}
Output : [1, 2, 3, 4]

s = {1, 2, 3, 4}
print(list(s))

19. Convert Set to String in Python
s = {'a', 'b', 'c', 'd'}
Output :

Initially
The datatype of s : <class 'set'>
Contents of s :  {'c', 'd', 'a', 'b'}

s = {'a', 'b', 'c', 'd'}

c = "".join(s)
print(c)

c =""
for i in s:
    c = c + i
print(c)

20. page no: 42 Convert String to Set in Python
string = "geeks"
Output :
{'s', 'g', 'e', 'k'}

s = "geeks"
print(set(s))  

21. Convert a set into dictionary
ini_set = {1, 2, 3, 4, 5}
Output: 
initial string {1, 2, 3, 4, 5}
<class 'set'>
final list {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
<class 'dict'>


s = {1, 2, 3, 4, 5}
d = {}

for i in s:
    d[i] = 0
print(d)

22. Set update() in Python to do union of n arrays
Input : arr = [[1, 2, 2, 4, 3, 6],
              [5, 1, 3, 4],
              [9, 5, 7, 1],
              [2, 4, 1, 3]]
Output : [1, 2, 3, 4, 5, 6, 7, 9]

Difference between add() and update()
a.add(5) - Adds one element.

a.update([5, 6, 7]) - Adds multiple elements from an iterable

s = [[1, 2, 2, 4, 3, 6],
              [5, 1, 3, 4],
              [9, 5, 7, 1],
              [2, 4, 1, 3]]

a = set()
for i in s:
    a.update(i)
print(sorted(a))

23. Intersection of two lists
Input : 
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
Output :
	[9, 10, 4, 5]

lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

s1 = set(lst1)
s2 = set(lst2)
print(s1 & s2)

#without sets
a = []
for i in lst1:
    if i in lst2 and i not in a:
            a.append(i)
print(a)

24. get all subsets of given size of a set
Input : {1, 2, 3}, n = 2
Output : [{1, 2}, {1, 3}, {2, 3}]

from itertools import combinations
s = {1, 2, 3}
n = 2
for i in combinations(s,n):
    print(set(i))
without itertools
h = []
a = list(s)
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        h.append({a[i], a[j]})
print(h)

25. Minimum number of subsets with distinct elements using Counter
Input : arr[] = {1, 2, 3, 4}
Output :1


from collections import Counter

a = [1, 2, 3, 3]

c = Counter(a)
print(max(c.values()))

26. dictionary, set and counter to check if frequencies can become same

Input  : str = “xyyz”
Output : Yes


from collections import Counter
s = "xyyz"
c =Counter(s)
for i in list(c):
    c[i] -= 1
    if c[i] == 0:
        del c[i]
    if len(set(c.values())) == 1:
        print("yes")
        break
    c = Counter(s)
else:
    print("No")

'''





























    














































