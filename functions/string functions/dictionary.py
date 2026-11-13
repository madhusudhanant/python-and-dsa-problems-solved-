'''
Definition:
A dictionary is a collection that is ordered, changeable, and
does not allow duplicates. Dictionaries are written with curly brackets
and have keys and values.

1.creating and assending a dictionary
dic1 = {"brand": "tvs","model": "xl heavy duty","year": 2008}
print(dic1)
print(dic1["year"])
print(len(dic1))

2. dictionary with multiple type of values
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(dict1["colors"])
print(type(dict1))

3.accessing and modifying dictionary data

dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

d = dict1.get("colors")
print(d)
u = dict1.keys() #it only gives the key values
print(u)

dict1["colors"] = "white"
print(dict1)

#outputs
['red', 'white', 'blue']
#dict_keys(['brand', 'model', 'year', 'colors'])
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'colors': 'white'}

dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

###4. Dictionary Methods
print(dict1.values())
print(dict1.items())

output ;- dict_values(['Ford', 'Mustang', 1964, ['red', 'white', 'blue']])
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('colors', ['red', 'white', 'blue'])])
if "model" in dict1:
    print("yes")
dict1["year"] = 2018
print()

5. Updating, Removing, and Copying

dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

dict1.update({"year": 2020})
print(dict1)

dict1["colors"] = "red"
print(dict1)

dict1.pop("model")
print(dict1)

dict1.popitem()
print(dict1)

del dict1["year"]
print(dict1)

dict1.clear()
print(dict1)

dict3 = dict1.copy()
print(dict3)

mydict = dict(dict1)
print(mydict)

6. Looping Through Dictionary

for x in dict1:
    print(x)
brand
model
year
colors

for x in dict1:
    print(dict1[x])
Ford
Mustang
1964
['red', 'white', 'blue']

for x in dict1.values():
    print(x)
Ford
Mustang
1964
['red', 'white', 'blue']


for x in dict1.keys():
  print(x)

dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
for x, y in dict1.items():
  print(x, y)

brand Ford
model Mustang
year 1964
colors ['red', 'white', 'blue']

############## Excercise ###################
Exercise 1: Below are the two lists convert it into the dictionary

Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30,89]
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]
print(d)


Exercise 2: Merge following two Python dictionaries into one
Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)

Exercise 3: Access the value of key ‘history’ from the below dict
Expected output: 80

d ={ 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
f = d["class"]["student"]["marks"]["history"]
print(f)

Exercise 4: Initialize dictionary with default values
expected output:
{'Kelly': {'designation': 'Application Developer', 'salary': 8000}, 'Emma': {'designation': 'Application Developer', 'salary': 8000}, 'John': {'designation': 'Application Developer', 'salary': 8000}}

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
d ={}
for i in range(len(employees)):
    d[employees[i]] = defaults
print(d)

Exercise 5: Create a new dictionary by extracting the following keys from
a below dictionary

d = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

keys = ["name", "salary"]

new_dict = {}

for key in keys:
    new_dict[key] = d[key]

print(new_dict)

Exercise 6: Delete set of keys from a dictionary
Expected output:
{'city': 'New york', 'age': 25}

d = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
key=["name","salary"]

for i in key:
    del d[i]
print(d)

Exercise 7: Check if a value 200 exists in a dictionary
Expected output:
True

d = {'a': 100, 'b': 200, 'c': 300}
for i in d.values():
    if i == 200:
        print("True")


Exercise 8: Rename key city to location in the following dictionary

d = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

d["location"] = d.pop("city")
print(d)

Exercise 9: Get the key of a minimum value from the following dictionary

d = {
  'Physics': 90,
  'Math': 65,
  'history': 75
}

k = list(d.keys())
print(k)
ma = d['Physics']
ke = ""

for k, i in d.items():
    if ma >= i:
        ma = i
        ke = k
print(ke)

Exercise 10: Change Brad’s salary to 8500 from a given Python dictionary
Expected output:
{'emp1': {'name': 'Jhon', 'salary': 7500},
 'emp2': {'name': 'Emma', 'salary': 8000},
 'emp3': {'name': 'Brad', 'salary': 8500}}

d = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}

d["emp3"]["salary"] = 8500
print(d)


####### extra dictionary sums pg: 45 ######
#sort dictonary by values

1. Sort Python Dictionaries by Key or Value

Input:

{'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

Output: 
{'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}

d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

h = dict(sorted(d.items(),key=lambda x:x[1]))
print(h)

2. Handling missing keys in Python dictionaries
country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
Output: 
0091
Not Found

d = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}

k = ["India","Nepal"]
for i in k:
    if i in d:
        print(d[i])
    else:
        print("Not found")
#using get()
print(d.get("India","Not found"))

3. program to find the sum of all items in a dictionary
Examples: 
Input : {‘a’: 100, ‘b’:200, ‘c’:300}
Output : 600

d = {"a": 100, "b":200, "c":300}
s = 0
for i in d:
    s += d[i]
print(s)
#using sum
h = sum(d.values())
print(h)

4. size of a Dictionary in Python
dic1 = {"A": 1, "B": 2, "C": 3} 
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}

from sys import getsizeof
d1 = {"A": 1, "B": 2, "C": 3} 
d2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
d3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}

print(getsizeof(d1),"bytes")
print(getsizeof(d2),"bytes")
print(getsizeof(d3),"bytes")

5. Ways to sort list of dictionaries by values in Python – Using itemgetter
Output:
The list printed sorting by age: 
[{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Nandini'}, {'age': 20, 'name': 'Manjeet'}]

from operator import itemgetter

d = [{'age': 19, 'name': 'Nikhil'},
     {'age': 20, 'name': 'Nandini'},
     {'age': 20, 'name': 'Manjeet'}]

for i in range(len(d)):
    for j in range(len(d)-1):
        if d[j]['age'] > d[j+1]['age']:
            d[j], d[j+1] = d[j+1], d[j]
print(d)

d.sort(key=itemgetter("age"))
print(d)

6. Merging two Dictionaries
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

dict1.update(dict2)
print(dict1)

7. Insertion at the beginning in OrderedDict
Input: original_dict = {'a':1, 'b':2}
item to be inserted ('c', 3)

Output:  {'c':3, 'a':1, 'b':2}

from collections import OrderedDict
d = OrderedDict({'a':1, 'b':2})

d['c'] = 3
d.move_to_end('c', last=False)
print(d)                                                                                                            

8. Check order of character in string using OrderedDict( )
Examples:
Input: string = "engineers rock"
pattern = "er";
Output: true
Explanation: All 'e' in the input string are before all 'r'.

s = "engineers rock"

e_pos = []
r_pos = []
for i in range(len(s)):
    if s[i] == "e":
        e_pos.append(i)
    elif s[i] == "r":
        r_pos.append(i)
if max(e_pos) < min(r_pos):
    print(True)
else:
    print(False)

9. Find common elements in three sorted arrays by dictionary intersection

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
Output: [80, 20]

a = [1, 5, 10, 20, 40, 80]
b = [6, 7, 20, 80, 100]
c = [3, 4, 15, 20, 30, 70, 80, 120]
d = {}

for i in a:
    d[i] = 1

for i in b:
    if i in d:
        d[i] = d[i] + 1
for i in c:
    if i in d:
        d[i] = d[i] + 1
h=[]
for i in d:
    if d[i] == 3:
        h.append(i)
print(h)

# easiest method
a = [1, 5, 10, 20, 40, 80]
b = [6, 7, 20, 80, 100]
c = [3, 4, 15, 20, 30, 70, 80, 120]
h=[]
for i in a:
    if i in b and i in c:
        h.append(i)
print(h)

10. Dictionary and counter in Python to find winner of election
Examples: Input :  votes[] = {"john", "johnny", "jackie", 
                    "johnny", "john", "jackie", 
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny", 
                    "john"};
Output : John

The maximum number of votes.
If there's a tie, choose the alphabetically smallest name.

votes = ["john", "johnny", "jackie", 
        "johnny", "john", "jackie", 
        "jamie", "jamie", "john",
        "johnny", "jamie", "johnny", "john"]

d = {}

for i in votes:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
m = max(d.values())

h = []

for i in d:
    if d[i] == m:
        h.append(i)

w = min(h)
print(w)

##### pg no : 48

11. Key with maximum unique values
Given a dictionary with values list, extract key whose value has most unique values.
Input : test_dict = {“Gfg” : [5, 7, 9, 4, 0], “is” : [6, 7, 4, 3, 3], “Best” : [9, 9, 6, 5, 5]}
Output : “Gfg”
Explanation : “Gfg” having max unique elements i.e 5.


d = {"Gfg" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}

mx = 0
element = ""
for i in d:
    c = len(set(d[i]))
    print(d[i])
    if c > mx:
        mx = c
        element = i
print(element,"having max unique elements",mx)

12. Find all duplicate characters in string
Given a string, find all the duplicate characters which are similar to each other. Let us look at the example. 
Examples:

Input : geeksforgeeeks
Output : e g k s

s = "geeksforgeeeks"
d = {}
c = 0
for i in s:
    if i in d:
        d[i] +=1
    else:
        d[i] =1
        
for i in d:
    if d[i]>1:
        print(i,end=" ")

13. Group Similar items to Dictionary Values List
Given a list of elements, perform grouping of similar elements, as different key-value list in dictionary.
Input : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8] 
Output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]} 


d = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
h = {}
for i in d:
    u=[]
    for j in d:
        if i == j:
            u.append(j)
            h[i] = u
print(h)

#using one pass dict soluton
d = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
h = {}
for i in d:
    if i in h:
        h[i].append(i)
    else:
        h[i] = [i]
print(h)

14. K’th Non-repeating Character in Python using List Comprehension and OrderedDict

Input : str = geeksforgeeks, k = 3
Output : r
First non-repeating character is f,
second is o and third is r


s = "geeksforgeeks"
d ={}
k = 3
x =0
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

c = 0
for i in d:
    if d[i] ==1:
        c+=1
    if c == k:
        print(i)
        break

15. Replace String by Kth Dictionary value
Given list of Strings, replace the value mapped by Kth value of mapped list.
Input : test_list = [“Gfg”, “is”, “Best”], subs_dict = {“Gfg” : [5, 6, 7], “is” : [7, 4, 2]}, K = 0 
Output : [5, 7, “Best”] 

Explanation : “Gfg” and “is” is replaced by 5, 7 as 0th index in dictionary value list. 


d = ["Gfg", "is", "Best"]
sd = {"Gfg" : [5, 6, 7], "is" : [7, 4, 2]}
k = 0    
h = []    

for i in d: 
    if i in sd:
        h.append(sd[i][k])
    else:
        h.append(i)
print(h)

16. Ways to remove a key from dictionary
Example:
Before remove key:   {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22,  'Mani': 21}
Operation Perform:   del test_dict['Mani']


d = {'Anuradha': 21,
     'Haritha': 21,
     'Arushi': 22,
     'Mani': 21}
del d["Mani"]
print(d)

17. Replace words from Dictionary
Given String, replace it’s words from lookup dictionary.
Input : test_str = ‘geekforgeeks best for geeks’, repl_dict = {“geeks” : “all CS aspirants”} 
Output : geekforgeeks best for all CS aspirants 
Explanation : “geeks” word is replaced by lookup value. 

split() → String → List
join() → List of strings → String

test_str = "geekforgeeks best for geeks"
repl_dict = {"geeks" : "all CS aspirants"} 
y = test_str.split()
for i in range(len(y)):
    if y[i] in repl_dict:
        y[i] = repl_dict[y[i]]
print(" ".join(y))

18. Remove Dictionary Key Words
Output : 
The original string is : gfg is best for geeks
The string after replace : gfg is  for 
    

s = "gfg is best for geeks"
repl_dict = {
    "best": "",
    "geeks": ""
}
y = s.split()
h=[]
for i in y:
    if i not in repl_dict:
        h.append(i)
print(" ".join(h)) 

19. Remove all duplicates words from a given sentence
Given a sentence containing n words/strings. Remove all duplicates words/strings which are similar to each others.
Examples:  
Input : Geeks for Geeks
Output : Geeks for

Input : Python is great and Java is also great
Output : is also Java Python and great
    

s = "Geeks for Geeks"

y= s.split()
h=[]
for i in y:
    if i not in h:
        h.append(i)
print(" ".join(h))

20. Remove duplicate values across Dictionary Values
Input: test_dict = {‘Manjeet’: [1], ‘Akash’: [1, 8, 9]} 
Output: {‘Manjeet’: [], ‘Akash’: [8, 9]} 
Input: test_dict = {‘Manjeet’: [1, 1, 1], ‘Akash’: [1, 1, 1]} 
Output: {‘Manjeet’: [], ‘Akash’: []}


test_dict = {"Manjeet": [1], "Akash": [1, 8, 9]}
d={}
for i in test_dict:
    for j in test_dict[i]:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1

for i in test_dict:
    h=[]
    for j in test_dict[i]:
        if d[j] == 1:
            h.append(j)
    test_dict[i] = h
print(test_dict)

21. Dictionary to find mirror characters in a string
Examples: 
Input : N = 3
        paradox
Output : paizwlc
We mirror characters from position 3 to end.

s = "paradox"
n = 3
d={}
a = "abcdefghijklmnopqrstuvwxyz"
b = "zyxwvutsrqponmlkjihgfedcba"

final = ""
for i in range(26):
    d[a[i]] = b[i]

for i in range(len(s)):
    if i < n-1:
        print(i)
        final += s[i]
    else:
        final += d[s[i]]
print(final)


22. The frequencies in a list using dictionary in Python
Example: 
Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,
                  4, 4, 4, 2, 2, 2, 2]
Output : 1 : 5
         2 : 4
         3 : 3
         4 : 3
         5 : 2

p = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

d ={}
for i in p:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in sorted(d):
    print(i,":",d[i])

23. Dictionary Values Mean

Given a dictionary, find mean of all the values present.
Input : test_dict = {"Gfg" : 4, "is" : 4, "Best" : 4, "for" : 4, "Geeks" : 4} 
Output : 4.0 Explanation : (4 + 4 + 4 + 4 + 4) / 4 = 4.0, hence mean. 


d = {"Gfg" : 4, "is" : 4, "Best" : 4, "for" : 4, "Geeks" : 4}
s = 0
for i in d:
    s = s+ d[i]
t = s/ len(d)
print(t)

24. counter and dictionary intersection example (Make a string using deletion and rearrangement)
Given two strings, find if we can make first string from second by deleting some characters from second and rearranging remaining characters. 

Examples:
Input : s1 = ABHISHEKsinGH
      : s2 = gfhfBHkooIHnfndSHEKsiAnG
Output : Possible


s1 = "ABHISHEKsinGH"
s2 = "gfhfBHkooIHnfndSHEKsiAnG"

d1 = {}
d2 = {}
for i in s1:
    if i in d1:
        d1[i] +=1
    else:
        d1[i] = 1

for i in s2:
    if i in d2:
        d2[i] +=1
    else:
        d2[i] = 1

for i in d1:
    if i not in d2 or d1[i] > d2[i]:
        print("Not Possible")
        break
else:
    print("Possible")

25.Possible Words using given characters in Python

Given a dictionary and a character array, print all valid words that are possible using characters from the array. Note: Repetitions of characters is not allowed.
Examples:
Input : Output : go, me, goal. 


d = ["go","bat","me","eat","goal","boy", "run"]
a = ['e','o','b', 'a','m','g', 'l']
d1 = {}

for i in d:
    for j in i:
        if j not in a:
            break
    else:
        print(i)

26. Maximum record value key in dictionary
test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
             'is' : {'Manjeet' : 8, 'Himani' : 9},
             'best' : {'Manjeet' : 10, 'Himani' : 15}}
Output :
The original dictionary is : {‘best’: {‘Himani’: 15, ‘Manjeet’: 10}, ‘gfg’: {‘Himani’: 10, ‘Manjeet’: 5}, ‘is’: {‘Himani’: 9, ‘Manjeet’: 8}}
The required key is : best
      

test_dict = {
    'gfg': {'Manjeet': 5, 'Himani': 10},
    'is': {'Manjeet': 8, 'Himani': 9},
    'best': {'Manjeet': 10, 'Himani': 15}
}
mx = 0
for i in test_dict:
    for j in test_dict[i]:
        if test_dict[i][j] > mx:
            mx = test_dict[i][j]
            f = i
print(f)      


27. Extract values of Particular Key in Nested Values
Given a dictionary with nested dictionaries as values, extract all the values with of particular key.
Input : test_dict = {‘Gfg’ : {“a” : 7, “b” : 9, “c” : 12}, ‘is’ : {“a” : 15, “b” : 19, “c” : 20}, ‘best’ :{“a” : 5, “b” : 10, “c” : 2}}, temp = “b”
Output : [9, 10, 19]
Explanation : All values of “b” key are extracted.


d = {
    'Gfg': {"a": 7, "b": 9, "c": 12},
    'is': {"a": 15, "b": 19, "c": 20},
    'best': {"a": 5, "b": 10, "c": 2}
}

k = "b"
t= {}
h=[]
for i in d:
    for j in d[i]:
        if j == k:
            h.append(d[i][j])
print(sorted(h))

#or easy method

k = "b"

h = []

for i in d:
    h.append(d[i][k])

print(sorted(h))

28. Convert Key-Value list Dictionary to List of Lists
test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
Output : [['gfg', 1, 3, 4], ['is', 7, 6], ['best', 4, 5]]


t = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

h = []
for i in t:
    h1 = [i]
    for j in t[i]:
        h1.append(j)
    h.append(h1)
print(h)

29. Convert List to List of dictionaries
Given list values and keys list, convert these values to key value pairs in form of list of dictionaries.
Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”]
Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}]
Explanation : Values mapped by custom key, “name” -> “Gfg”, “id” -> 3.


t = ["Gfg", 3, "is", 8]
kt = ["name", "id"]

h =[]
for i in range(0,len(t), 2):
    d = {}
    for j in range(len(kt)):
        d[kt[j]] = t[i + j] 
    h.append(d)
print(h)


30. Convert Lists of List to Dictionary
Output :
The original list is : [[‘a’, ‘b’, 1, 2], [‘c’, ‘d’, 3, 4], [‘e’, ‘f’, 5, 6]]
The mapped Dictionary : {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’): (1, 2)}

page no: 55

t = [
    ['a', 'b', 1, 2],
    ['c', 'd', 3, 4],
    ['e', 'f', 5, 6]
]
d={}

for i in t:
    k = (i[0], i[1])
    v = (i[2], i[3])
    d[k] = v
print(d)

31. Convert Lists of List to Dictionary

Convert List of Dictionaries to List of Lists
Input : test_list = [{‘Gfg’: 123, ‘best’: 10}, {‘Gfg’: 51, ‘best’: 7}]
Output : [[‘Gfg’, ‘best’], [123, 10], [51, 7]]



d = [
    {'Gfg': 123, 'best': 10},
    {'Gfg': 51, 'best': 7}
]

h=[]
for i in d:
    h1=[]
    for j in i:
        h1.append(j)
    h.append(h1)
    break

for i in d:
    h1=[]
    for j in i:
        h1.append(i[j])
    h.append(h1)
print(h)

#using one loop
h = []

for i in range(len(d)):
    k = []
    v = []
    for j in d[i]:
        k.append(j)
        v.append(d[i][j])
    if i == 0:
        h.append(k)
    h.append(v)
print(h)

32. Convert key-values list to flat dictionary
Output : 
The original dictionary is : {‘name’: [‘Jan’, ‘Feb’, ‘March’], ‘month’: [1, 2, 3]}
Flattened dictionary : {1: ‘Jan’, 2: ‘Feb’, 3: ‘March’}


d = {"name": ["Jan", "Feb", "March","april"],
    "month": [1, 2, 3,4]}
d1 = {}
for i in range(len(d["month"])):
    d1[d["month"][i]] = d["name"][i]
print(d1)


33. Convert a list of Tuples into Dictionary
Input : [("akash", 10), ("gaurav", 12), ("anand", 14), 
         ("suraj", 20), ("akhil", 25), ("ashish", 30)]
Output : {'akash': [10], 'gaurav': [12], 'anand': [14], 
          'ashish': [30], 'akhil': [25], 'suraj': [20]}


t = [("akash", 10), ("gaurav", 12), ("anand", 14), 
         ("suraj", 20), ("akhil", 25), ("ashish", 30)]
d={}
for i in t:
    d[i[0]] = [i[1]]
print(d)

34. Convert Nested dictionary to Mapped Tuple
Input :test_dict = {‘gfg’ : {‘x’ : 5, ‘y’ : 6, ‘z’: 3}, ‘best’ : {‘x’ : 8, ‘y’ : 3, ‘z’: 5}} 
Output : [(‘x’, (5, 8)), (‘y’, (6, 3)), (‘z’, (3, 5))] 

d = {
    'gfg': {'x': 5, 'y': 6, 'z': 3},
    'best': {'x': 8, 'y': 3, 'z': 5}
}
h = []
for i in d["gfg"]:
    h.append((i, (d["gfg"][i], d["best"][i])))
print(h)

35. convert string to dictionary
str = " Jan = January; Feb = February; Mar = March"
 
Output
	{' Jan ': ' January', ' Feb ': ' February', ' Mar ': ' March'}



s = "Jan = January; Feb = February; Mar = March"
d={}
y = s.split(";")
for i in y:
    h = i.split("=")
    d[h[0]] = h[1]
print(d)


36. Convert dictionary to K sized dictionaries
Given a Dictionary, divide dictionary into K sized different dictionaries list.
Input : test_dict = {‘Gfg’ : 1, ‘is’ : 2, ‘best’ : 3, ‘for’ : 4, ‘geeks’ : 5, ‘CS’ : 6}, K = 3
Output : [{‘Gfg’: 1, ‘is’: 2, ‘best’: 3}, {‘for’: 4, ‘geeks’: 5, ‘CS’: 6}]


d = {
    'Gfg': 1,
    'is': 2,
    'best': 3,
    'for': 4,
    'geeks': 5,
    'CS': 6
    }

k = 3
h=[]
c=0
d1={}
for i in d:
    d1[i] = d[i]
    c+=1
    if c == k:
        h.append(d1)
        d1 ={}
        c=0
if d1:
    h.append(d1)
print(h)

37. Convert Matrix to dictionary
Given a Matrix, convert it into dictionary with keys as row number and value as nested list.
Input : test_list = [[5, 6, 7], [8, 3, 2]]
Output : {1: [5, 6, 7], 2: [8, 3, 2]}
Explanation : Matrix rows are paired with row number in order

d1 = [[5, 6, 7], [8, 3, 2]]
d ={}
for i in range(len(d1)):
    d[i + 1] = d1[i]
print(d)

38.Convert Dictionary and List to Nested Dictionary
test_dict = {'Gfg': 4, 'best': 9}
test_list = [8, 2]

d1 = {'Gfg': 4, 'best': 9}
d2 = [8, 2]

k = list(d1.keys())
h = {}
for i in range(len(d1)):
    d = {}
    d[k[i]] = d1[k[i]]
    h[d2[i]] = d
print(h)

39. Swapping Hierarchy in Nested Dictionaries

Input : test_dict = {‘Gfg’: { ‘a’ : [1, 3, 7, 8], ‘b’ : [4, 9], ‘c’ : [0, 7]}} 
Output : {'a': {'Gfg': [1, 3, 7, 8]}, 'b': {'Gfg': [4, 9]}, 'c': {'Gfg': [0, 7]}}

d1 = {'Gfg': {'a': [1, 3, 7, 8], 'b': [4, 9], 'c': [0, 7]}}
d = {}
for i in d1:
    for j in d1[i]:
        d[j] = {i : d1[i][j]}
print(d)

40. Reverse Dictionary Keys Order

test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5}
Output :

OrderedDict ([('best', 5), ('is', 2), ('gfg', 4)])
The original insertion order is gfg → is → best, reversing it gives best → is → gfg

from collections import OrderedDict

d = {'gfg' : 4, 'is' : 2, 'best' : 5}
k = list(d.keys())
h = OrderedDict()
for i in range(len(k)-1,-1,-1):
    print("d[k[i]] = ",d[k[i]])
    h[k[i]] = d[k[i]]
print(h)

41. Extract Key’s Value, if Key Present in List and Dictionary
Input : test_list = ["Gfg", "is", "Good", "for", "Geeks"], 
test_dict = {"Gfg" : 5, "Best" : 6}, K = "Gfg" 
Output : 5 


test_list = ["Gfg", "is", "Good", "for", "Geeks"]
d = {"Gfg" : 5, "Best" : 6}
k = "Gfg"

for i in test_list:
    if i == k:
        for j in d:
            if j == k:
                print(d[j])

42.Remove keys with Values Greater than K ( Including mixed values )
Given a dictionary with key-value pairs, remove all the keys with values greater than K, including mixed values.

Input:
test_dict = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}
Output : {'Gfg': 3, 'for': 6, 'geeks': 'CS'}
Explanation : All values greater than K are removed. Mixed value is retained. 
 
d = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}
k = 7
d1 = {}
for i in d:
    if type(d[i]) == int:
        if d[i] < k:
            d1[i] = d[i]
    else:
        d1[i] = d[i]
print(d1)

43. Remove the key if its value contains any word from sub_list
test_dict = {1: 'Gfg is best for geeks'}
sub_list = ['love', 'good']
output {1: 'Gfg is best for geeks'}
##### Strings do not have a remove() method

d = {1: 'Gfg is good for geeks'}
s = ['love', 'good']
d1={}
for i in d:
    y = d[i].split()
    for j in y:
        if j in s:
            break
    else:
        d1[i] = d[i]
print(d1)

44. Dictionary with maximum count of pairs
test_list = [{'gfg': 2, 'best': 4}, {'gfg': 2, 'is': 3, 'best': 4, 'CS': 9}, {'gfg': 2}]
Output : 4
Explanation : 2nd dictionary has maximum keys, 4.


d = [{'gfg': 2, 'best': 4}, {'gfg': 2, 'is': 3, 'best': 4, 'CS': 9}, {'gfg': 2}]
mx = 0
for i in d:
    print(i)
    c=0
    for j in i:
        c+=1
        if c > mx:
            mx = c
        
print(mx)
# easy version
for i in test_list:
    if len(i) > mx:
        mx = len(i)
print(mx)

45. Append Dictionary Keys and Values ( In order ) in dictionary
Input : test_dict = {'Gfg': 1, 'is': 2, 'Best': 3} 
Output : [‘Gfg’, ‘is’, ‘Best’, 1, 2, 3] 

d = {'Gfg': 1, 'is': 2, 'Best': 3}
k = []
v = []
for i in d:
    k.append(i)
    v.append(d[i])
k.extend(v)
print(k)

46. Extract Unique values dictionary values
Output
The original dictionary is : {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12]

d = {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
h =[]

for i in d:
    for j in d[i]:
        if j not in h:
            h.append(j)
print(sorted(h))

47. Keys associated with Values in Dictionary
Input : test_dict = {'abc': [10, 30], 'bcd': [30, 40, 10]}
output {
    10: ['abc', 'bcd'],
    30: ['abc', 'bcd'],
    40: ['bcd']
}


d = {'abc': [10, 30], 'bcd': [30, 40, 10]}
h ={}
for i in d:
    for j in d[i]:
        if j not in h:
            h[j] = []
        h[j].append(i)
print(h)

48. Filter dictionary values in heterogeneous dictionary
Input : test_dict = {‘Gfg’ : 10, ‘for’ : ‘geeks’} 
Output : {‘Gfg’: 10, ‘for’: ‘geeks’}

test_dict = {'Gfg': 10, 'for': 'geeks', 'is': 20}
h = {}
for i in test_dict:
    if type(test_dict[i]) == int:
        print(test_dict[i])
        h[i] = test_dict[i]
print(h)

49.Print anagrams together in Python using List and Dictionary
Examples:
Input: arr = ['cat', 'dog', 'tac', 'god', 'act']
Output: ‘cat tac act dog god’

a = ['cat', 'dog', 'tac', 'god', 'act']
d ={}
for i in a:
    k = "".join(sorted(i))
    if k not in d:
        d[k] = []
    d[k].append(i)
for i in d:
    for j in d[i]:
        print(j,end=" ")


50. Check if binary representations of two numbers are anagram
Examples:
Input : a = 8, b = 4 
Output : Yes


#with inbuilt function
a = 8
b = 4
if bin(a).count("1") == bin(b).count("1"):
    print(bin(a)) #print(d[k])
    print("yes")
else:
    print("no")

a = 4
b = 8

c1 = 0
c2 = 0

while a > 0:
    if a % 2 == 1:
        c1 += 1
    a = a // 2

while b > 0:
    if b % 2 == 1:
        c2 += 1
    b = b // 2

if c1 == c2:
    print("Yes")
else:
    print("No")


51. Counter to find the size of largest subset of anagram words
Examples:
Input: ant magenta magnate tan gnamate
Output: 3
Explanation
Anagram strings(1) - ant, tan
Anagram strings(2) - magenta, magnate,
                     gnamate
Thus, only second subset have largest
size i.e., 3

a = ['ant', 'magenta', 'magnate', 'tan', 'gnamate']
d = {}
for i in a:
    k = "".join(sorted(i))
    if k not in d:
        d[k] = []
    d[k].append(i)
print(d)
mx = 0
for i in d:
    if len(d[i]) > mx:
        mx = len(d[i])
print(mx)

52. Count of groups having largest size while grouping according to sum of its digits
n = 13
output = 4

n = 13
d = {}
for i in range(1, n + 1):
    s = 0
    x = i
    while x > 0:
        s += x % 10
        x = x // 10
    print("s",s)
    if s not in d:
        d[s] = []
    d[s].append(i)
print(d)
mx = 0
for i in d:
    if len(d[i]) > mx:
        mx = len(d[i])
c = 0
for i in d:
    if len(d[i]) == mx:
        c += 1
print(c)
{
1:[1,10],
2:[2,11],
3:[3,12],
4:[4,13],
5:[5],
6:[6],
7:[7],
8:[8],
9:[9]
}

53. Sort Dictionary key and values List
Input : test_dict = {‘c’: [3], ‘b’: [12, 10], ‘a’: [19, 4]}
Output : {'a': [4, 19], 'b': [10, 12], 'c': [3]}


d = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
d1={}
k = list(d.keys())
k.sort()

for i in k:
    k1 = d[i]
    k1.sort()
    d1[i] = k1
print(d1)
    
54. Sort Dictionary by Values Summation
Input : test_dict = {‘Gfg’ : [6, 7, 4], ‘best’ : [7, 6, 5]}
Output : {‘Gfg’: 17, ‘best’: 18}


a = {'Gfg': [6, 7, 4], 'best': [7, 6, 5]}
d={}
for i in a:
    s = 0
    for j in a[i]:
        s += j
    d[i] = s
print(d)


55. Sort dictionaries list by Key’s Value list index
arr = [{'Gfg':[6,7,8],'is':9,'best':10}, {'Gfg':[2,0,3],'is':11,'best':19}, {'Gfg':[4,6,9],'is':16,'best':1}]
K = "Gfg"
idx = 0
Output : [{'Gfg': [2, 0, 3], 'is': 11, 'best': 19}, {'Gfg': [4, 6, 9], 'is': 16, 'best': 1}, {'Gfg': [6, 7, 8], 'is': 9, 'best': 10}]

a = [{'Gfg':[6,7,8],'is':9,'best':10},
       {'Gfg':[2,0,3],'is':11,'best':19},
       {'Gfg':[4,6,9],'is':16,'best':1}]

ind = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i]["Gfg"][ind] > a[j]["Gfg"][ind]:
            a[i], a[j] = a[j], a[i]
print(a)


56. Sort Nested keys by Value
Output :
The original dictionary : {‘Nikhil’: {‘English’: 5, ‘Maths’: 2, ‘Science’: 14}, ‘Akash’: {‘English’: 15, ‘Maths’: 7, ‘Science’: 2}, ‘Akshat’: {‘English’: 5, ‘Maths’: 50, ‘Science’: 20}}
The sorted dictionary : {‘Nikhil’: {‘Maths’: 2, ‘English’: 5, ‘Science’: 14}, ‘Akash’: {‘Science’: 2, ‘Maths’: 7, ‘English’: 15}, ‘Akshat’: {‘English’: 5, ‘Science’: 20, ‘Maths’: 50}}

d = {'Nikhil': {'English': 5, 'Maths': 2, 'Science': 14},
     'Akash': {'English': 15, 'Maths': 7, 'Science': 2},
     'Akshat': {'English': 5, 'Maths': 50, 'Science': 20}}
h = {}
for i in d:
    t = d[i]
    k = list(t.keys())
    for x in range(len(k)):
        for y in range(x+1,len(k)):
            if t[k[x]] > t[k[y]]:
                k[x], k[y] = k[y], k[x]
    h[i] = {}
    for j in k:
        h[i][j] = t[j]
print(h)

57. Scoring Matrix using Dictionary
Input : test_list = [[‘gfg’, ‘best’], [‘geeks’], [‘is’, ‘for’]]
Output : [18, 15, 12]


t = [['gfg', 'best'], ['geeks'], ['is', 'for']]
d = {'gfg': 7, 'best': 11, 'geeks': 15, 'is': 5, 'for': 7}
h=[]
for i in t:
    h.append(sum(d[j] for j in i))
print(h)

h=[]
for i in t:
    s = 0
    for j in i:
        s += d[j]
    h.append(s)
print(h)

58. Factors Frequency Dictionary
Given a list with elements, construct a dictionary with frequency of factors.
Input : test_list = [2, 4, 6, 8]
Output : {1: 4, 2: 4, 3: 1, 4: 2, 5: 0, 6: 1, 7: 0, 8: 1}
Explanation : All factors count mapped, e.g 2 is divisible by all 4 values, hence mapped with 4.


d ={}
t = [2, 4, 6, 8]

mx = 0
for i in t:
    if i > mx:
        mx = i

for i in range(1, mx+1):
    c=0
    for j in t:
        if j % i == 0:
            c+=1
    d[i] = c
print(d)


59. Count distinct substrings of a string using Rabin Karp algorithm
Given a string, count the number of distinct substrings using Rabin Karp Algorithm.
Examples: 
Input  : str = "aba"
Output : 5


s = "aba"
d={}
for i in range(len(s)):
    for j in range(i, len(s)):
        t = s[i:j+1]
        d[t] = 1
print(len(d))

60. Building an undirected graph and finding shortest path using Dictionaries in Python
edges = [
        ["A", "B"], ["A", "E"],
        ["A", "C"], ["B", "D"],
        ["B", "E"], ["C", "F"],
        ["C", "G"], ["D", "E"]
op:{
'A': ['B', 'E', 'C'],
'B': ['A', 'D', 'E'],
'E': ['A', 'B', 'D'],
'C': ['A', 'F', 'G'],
'D': ['B', 'E'],
'F': ['C'],
'G': ['C']}

edges = [
        ["A", "B"], ["A", "E"],
        ["A", "C"], ["B", "D"],
        ["B", "E"], ["C", "F"],
        ["C", "G"], ["D", "E"]]
d = {}
for i in edges:
    a = i[0]
    b = i[1]
    if a not in d:
        d[a] = []
    if b not in d:
        d[b] = []
    d[a].append(b)
    d[b].append(a)
print(d)

'''








