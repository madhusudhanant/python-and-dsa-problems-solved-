'''
# Lambda
Lambda Functions are anonymous functions, meaning functions without a name.
insted of def -> lambda
lambda arguments: expression

When to use which?
Use a normal function (def) when:
The logic is long or complex.
You need loops or multiple if statements.
You want to reuse the function many times.
Readability is important.

Use a lambda function when:
The logic is simple (one expression).
You need a quick, short function.
You're using functions like map(), filter(), sorted(), or reduce().

Example 1: Normal function vs Lambda
#Normal function
def square(x):
    return x * x
print(square(5))
Output: 25

#Lambda function
square = lambda x: x * x
print(square(5))

Example 2: Two parameters
add = lambda a, b: a + b
print(add(10, 20))

Example 3: Three parameters
largest = lambda a, b, c: max(a, b, c)
print(largest(5, 9, 2))


#Task 1: Square a Number
square = lambda x: x*x
print(square(5))

#Task 2: Add Two Numbers
add = lambda x,y: x + y 
print(add(10, 20))

#Task 3: Check if a Number is Even
is_even = lambda x: x%2 == 0
print(is_even(8))
print(is_even(7))

#Task 4: Find the Larger Number
#lambda arguments: value_if_true if condition else value_if_false
largest = lambda x,y: x if x > y else y
print(largest(12, 8))
print(largest(5, 15))

#Program 1:
s = "im madhu ms from coimbatore"
uppercase = lambda s: s.upper()
print(uppercase(s))
o/p: IM MADHU MS FROM COIMBATORE

#Program 2:
s = lambda a,b: a+b
print("sum =", s(10,20))
o/p: sum = 30

Program 3:
big = lambda a,b: print("a is bigger") if a>b else print("b is bigger")
big(30,10)
o/p: a is bigger

#Program 4
p = lambda x: [i**2 for i in List]
List = [2,4,6,8]
print(p(List))

#1. Area of triangle 
import math
a = lambda s, a, b, c: math.sqrt(s * (s - a) * (s - b) * (s - c))
print(a(10, 3, 4, 5))
o/p: 45.8257569495584

2. Perimeter of triangle → P = a + b + c
t = lambda a,b,c: a+b+c
print(t(3,4,5))

#3. Area of Equilateral triangle → A = a²
import math
area = lambda a: (math.sqrt(3)/4) * a* a
print(area(10))

#4. Biggest of Three Numbers 
big = lambda a,b,c: print("a is bigger") if (a>b and a>c) else print("b is bigger") if (b>c) else print("c is bigger")
big(100,20,30)

#5. Smallest of Three Numbers
small = lambda a,b,c: print("a is smaller") if (a<b and a<c) else print("b is smaller") if b<c else print("c is smaller")
small(100,20,5)

#6. Biggest of Four Numbers

big=lambda a,b,c,d: print('a is bigger') if(a>b and a>c and a>d) else print('b is bigger') if(b>c and b>d) else print('c is bigger') if(c>d) else print('d is bigger')
big(10,597,4,9)

#7 Smallest number of 4 numbers
smal=lambda a,b,c,d: print('a is smaller') if(a<b and a<c and a<d) else print('b is smaller') if(b<c and b<d) else print('c is smaller') if(c<d) else print('d is smaller')
smal(32,4646,7,1)

#8 Find the length of a string
L = lambda s: len(s)
print(L("Python"))

#9 Reverse a string
r = lambda s: s[::-1]
print(r("madhu"))

#10. Lambda with Lists
vote = lambda age: "eligible" if age >= 18 else "not Eligible"
print(vote(18))

#11. Lambda with sorted()
students = [("JOhn", 90), ("Alice",75),("Bob",85)]
students.sort(key=lambda x: x[1])
print(students)

#12. Lambda with map()
What is map()?

map() applies a function to every element in an iterable
(such as a list, tuple, or string).
map(function, iterable)

#Example 1: without map
numbers = [1, 2, 3, 4]
result = []
for i in numbers:
    result.append(i**2)
print(result) #[1, 4, 9, 16]

#Example 2: Using map()
n = [1,2,3,4]
r = map(lambda x: x**2, n)
print(list(r))


List = [1,2,3,4]
p = lambda x: [i**2 for i in List]
print(p(List))

n = [1,2,3,4,5]
s = list(map(lambda x: x **2, n))
print(s)

#Filter
#Syntax: filter(function, iterable)
numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x%2==0, numbers))
print(evens)  # Output: [10, 20, 30]

#Reduce
The reduce() function is defined in the functools module. It applies a rolling computation to sequential pairs of values in an iterable.
Syntax: reduce(function, iterable)

from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x*y, numbers)
print(product)  # Output: 120


###### LAMBDA EXCERCISE ######

1. Add 15 to a given number.
Multiply two numbers and print the result.

add = lambda x: x + 15
print(add(10)) #25

multiply = lambda x,y: x*y
print(multiply(6,8)) #48

o/p
25
48

2. Multiplied with an unknown given number. 

d = lambda x: x * 2
t = lambda x: x * 3
q = lambda x: x * 4
qu = lambda x: x * 5
print("Double the number of 15 =", d(15))
print("Triple the number of 15 =", t(15))
print("Quadruple the number of 15 =", q(15))
print("Quintuple the number of 15 =", qu(15))
o/p:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number of 15 = 75

3. sort a list of tuples using a lambda function.
m = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
m.sort(key=lambda x: x[1])
print(m)

o/p: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

4. sort a list of dictionaries using a lambda function.
phone = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
phone.sort(key=lambda x: x['color'])
print(phone)

Output:[
 {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
 {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
 {'make': 'Nokia', 'model': 216, 'color': 'Black'}
]

5. Filter a list of integers using Lambda. Original list of integers:

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x%2 ==0, lst))
odd = list(filter(lambda x: x%2 !=0, lst))
print(even)
print(odd)

#single line
lst = [1,2,3,4,5,6,7,8,9,10]
print("Even:", list(filter(lambda x: x % 2 == 0, lst)),
      "\nOdd :", list(filter(lambda x: x % 2 != 0, lst)))

o/p:
[2, 4, 6, 8, 10]
[1, 3, 5, 7, 9]
Even: [2, 4, 6, 8, 10] 
Odd : [1, 3, 5, 7, 9]

6. square and cube every number in a given list of integers using Lambda

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( "Square:", list(map(lambda x: x**2, n)),
       "\nCube:", list(map(lambda x: x**3, n)))

7.Given string starts with a given character using Lambda.
start = lambda s, c: s.startswith(c)
print(start("python", "p"))
print(start("Python", "J"))
#oneline:
print((lambda s, c: s.startswith(c))("python", "p"))
print((lambda s, c: s.startswith(c))("Python", "J"))

8. Extract year, month, date and time using Lambda. 
from datetime import datetime
d = datetime.now()
print((lambda x: x.year)(d))
print((lambda x: x.month)(d))
print((lambda x: x.day)(d))
print((lambda x: x.time())(d))

2026
8
6
12:00:07.301692

9. Given string is number or not using Lambda.

check = lambda x: x.isdigit()
print(check("123"))
print(check("4567"))
print(check("Python"))
print(check("2025"))
print(check("12A"))
print(check("987"))

True
True
False
True
False
True

10. create Fibonacci series upto n using Lambda.

fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)
print(fib(8))

n = int(input("Enter n: "))
for i in range(n):
    print(fib(i), end=" ")

O/p: 0 1 1 2 3 5 8 13 21

11. intersection of two given arrays using Lambda.

a1 = [1, 2, 3, 5, 7, 8, 9, 10]
a2 = [1, 2, 4, 8, 9]
s1 = set(a1)
s2 = set(a2)
c  = lambda: s1 & s2
print(c())

#or

c = lambda a1, a2: list(set(a1) & set(a2))
print(c(a1, a2))

o/p: {8, 1, 2, 9}

#12. Rearrange positive and negative numbers in a given array using 

a = [-1, 2, -3, 5, 7, 8, 9, -10]

c = sorted(a, key=lambda x: x <0)
print(c) #true 1 , false - 0 so 0 first then 1 

#using filter
p = list(filter(lambda x: x >= 0, a))
n = list(filter(lambda x: x < 0, a))
print(p+n)

o/p: [2, 5, 7, 8, 9, -1, -3, -10]

13. count the even, odd numbers in a given array of integers
count -> len

a =[1, 2, 3, 5, 7, 8, 9, 10]
e = len(list(filter(lambda x: x%2 ==0, a)))
o = len(list(filter(lambda x: x%2 !=0, a)))
print("odd", o)
print("Even", e)
odd 5
Even 3

14. find value of length 6

d = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
r = list(filter(lambda x: len(x)==6,d))
for i in r:
    print(i)

15. add two given lists using map and lambda

a =[1, 2, 3]
b = [4, 5, 6]
r = list(map(lambda a,b: a+b, a,b))
print(r)

16. Write a Python program to find the second lowest grade of any student(s) from the given names and grades of each student using lists and lambda.
Input number of students, names and grades of each student.

n = int(input("Input number of students: "))

students = []

for i in range(n):
    name = input("Name: ")
    grade = float(input("Grade: "))
    students.append([name, grade])

print("Names and Grades of all students:")
print(students)
grade = sorted(set(map(lambda x: x[1], students)))

second = grade[1]
print("Second lowest grade",second)
print("Names: ")
names = sorted(map(lambda x: x[0], filter(lambda x: x[1] == second, students)))

for i in names:
    print(i)

Input number of students: 3
Name: bob
Grade: 3
Name: brad
Grade: 9
Name: ram
Grade: 7
Names and Grades of all students:
[['bob', 3.0], ['brad', 9.0], ['ram', 7.0]]
Second lowest grade 7.0
Names: ram

17.  find numbers divisible by nineteen or thirteen
a = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
r = list(filter(lambda x: x%19 == 0 or x%13 == 0, a))
print(r)
o/p: [19, 65, 57, 39, 152, 190]

18. find palindromes

a = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

r = list(filter(lambda x: x[::-1] == x, a))
print(r)

map = doest remove anything
filter = does

19. Anagrams of a string 
Word 1	Word 2	Anagram?
listen	silent	✅ Yes
evil	vile	✅ Yes
heart	earth	✅ Yes
race	care    ✅ yes

a = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
w = "abcd"
r = list(filter(lambda x: sorted(x) == sorted(w), a))
print(r)

20. string and store them in a list, display the numbers which are bigger than
the length of the list in sorted form.
s = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
c = []
for i in s.split():
    if i.isdigit():
        c.append(int(i))
# c = [23, 5, 56, 20, 5]
r = lambda x: x > len(c)
for i in c:
    print(r(i)) # true so prints(i)
    if r(i):
        print(i)

21. multiply each number of given list
a =  [2, 4, 6, 9, 11]
r = list(map(lambda x: x * 2, a))
print(r) #[4, 8, 12, 18, 22]

22. Sum the lengths of names starting with uppercase letters

names = ["Suresh", "ravi", "Anu", "kumar", "David", "mani"]
r = list(filter(lambda x: x[0].isupper(),names))
print(r) #['Suresh', 'Anu', 'David']
m = map(lambda x: len(x), r)
print(sum(r)) #14

23. sum of the positive and negative numbers 
a = [2, 4, -6, -9, 11, -12, 14, -5, 17]
p = sum(filter(lambda x: x > 0, a))
n = sum(filter(lambda x: x < 0, a))
print("Positive Sum =", p)
print("Negative Sum =", n)


24. Find numbers in a range that are divisible by each of their digits using lambda.
a = range(1, 24)
r = list(filter(lambda x: all(int(d) != 0 and x % int(d) == 0 for d in str(x)),a))
print(r)
o/p: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

25. the next bigger number by rearranging the digits 
from itertools import permutations
n = int(input("Enter number: "))
p = sorted(set(map(lambda x: int("".join(x)), permutations(str(n)))))
r = list(filter(lambda x: x > n, p))
print(r[0] if r else False)

n = 102
('1','0','2')
('1','2','0')
('0','1','2')
('0','2','1')
('2','1','0')
('2','0','1')


o/p: Enter number: 445
454

26. maximum and minimum length

a = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
mx = max(a, key=lambda x: len(x))
mn = min(a, key=lambda x: len(x))
print("max: ",len(mx),mx)
print("min: ",len(mn),mn)

max:  3 [13, 15, 17]
min:  1 [0]

27. sort each sublist of strings

a =[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
r = list(map(lambda x: sorted(x), a))
print(r)

#o/p: [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]


28. sort lists by length and value

a = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
r = sorted(a, key=lambda x: (len(x), x))
print(r)

29.maximum value in a given heterogeneous
a = ['Python', 3, 2, 4, 5, 'version']
r = max(filter(lambda x: type(x) == int,a))
print(r)
5

30. Sort a given matrix in ascending order according to the sum of its rows 
a = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
r = sorted(a, key=lambda x: sum(x))
print(r)
[[1, 1, 1], [1, 2, 3], [2, 4, 5]]

Another example: Multiply every matrix element by 2
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r = list(map(lambda row: list(map(lambda x: x * 2, row)), a))
print(r)
[[2, 4, 6], [8, 10, 12], [14, 16, 18]]

31. Extract specified size of strings 
a = ['Python', 'list', 'exercises', 'practice', 'solution']
n = int(input("length of the string to extract: "))
r = list(filter(lambda x : len(x) == n, a))
print(r)

length of the string to extract: 8
['practice', 'solution']

32. count float number in a given mixed 

a = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
r = len(list(filter(lambda x: type(x) == float, a)))
print(r)
3

33. capital letter, a lower case letter, a number and a minimum length
any() means: "Is at least ONE item True?" - one True is enough
s = input("Enter string: ")
r = lambda x: len(x) >= 8 and any(i.isdigit() for i in x) and any(i.isupper() for i in x) and any(i.islower() for i in x)
print(r(s))

34. Filter the height and width of students
d = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
r = dict(filter(lambda x: x[1][0] > 6 and x[1][1] >= 70 , d.items()))
print(r)
o/p: {'Cierra Vega': (6.2, 70)}

35. Specified list is sorted or not 
a = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
r = lambda x: x == sorted(x)
print(r(a))
True

36. Extract the nth element from a given list
a = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
n = int(input("n: "))
r = list(map(lambda x: x[n], a))
print(r)

n == 0 ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
n == 1 [98, 97, 91, 94]

37. sort a list by given index 
a =[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
n = int(input("Enter index: "))
r = sorted(a, key=lambda x: x[n])
print(r)

Enter index: 0
[('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]

38. remove all elements from a given list present in another list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
r = list(filter(lambda x: x not in list2, list1))
print(r)

39. Find the elements of a given list of strings that contain specific substring 
a = ['red', 'black', 'white', 'green', 'orange']
s = "ack"
r = list(filter(lambda x: s in x,a))
print(r)
['black']

40. Find the nested lists elements, which are present in another list 

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
b = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
r = list(map(lambda x: list(filter(lambda y: y in a, x)),b))
print(r)
[[12], [7, 11], [1, 5, 8]]

41. Reverse strings in a given list of string values
a = ['Red', 'Green', 'Blue', 'White', 'Black']
r = list(map(lambda x: x[::-1], a))
print(r)

['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

42. Calculate the product of a given list of numbers

from functools import reduce
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = reduce(lambda x,y: x*y, a)
print(r)

3628800

43. multiply all the numbers in a given list 
from functools import reduce
a = [4, 3, 2, 2, -1, 18]
r = reduce(lambda x,y: x*y,a)
print(r)
-864

44. average value of the numbers in a given tuple
zip(*a) → gets columns  zip() takes:
First position
10
30
81
1
map() → applies lambda to every column
lambda → calculates average
tuple() → converts the result to a tuple

a = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
r = tuple(map(lambda x: sum(x) / len(x), zip(*a)))
print(r)
(30.5, 34.25, 27.0)

45. convert string element to integer
a =  (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
r = tuple(map(lambda x: (int(x[0]), int(x[2])), a))
print(r)

((233, 33), (1416, 55), (2345, 34))

46. find index position and value of the maximum and minimum values
enumerate() - This allows you to track both the index and the item simultaneously

a = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
mx = max(enumerate(a), key=lambda x: x[1])
mn = min(enumerate(a), key=lambda x: x[1])
print(mx)
print(mn)

(5, 89)
(3, 10.11)

47.  sort a given mixed list of integers and strings. Numbers must be sorted before strings. 
a = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
r = sorted(a, key=lambda x: (isinstance(x,str),x))
print(r)
#easy solution
n = sorted(filter(lambda x: type(x) == int, a))
s = sorted(filter(lambda x: type(x) == str, a))
r = n + s
print(r)

48. sort a given list of strings(numbers) numerically 

int(x) -> temporarily converts each string to a number for comparison
a = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500'] 
r = sorted(a,key=lambda x: int(x))
print(r)
['-500', '-12', '0', '4', '7', '12', '45', '100', '200']

49. count the occurrences of the items

a=[3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
d ={}
for x in a:
    d[x] = len(list(filter(lambda y: y == x, a)))
print(d)
{3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}

50. remove specific words from a given list

a = ['orange', 'red', 'green', 'blue', 'white', 'black']
b = ['orange', 'black']
r = list(filter(lambda x: x not in b, a))
print(r)
['red', 'green', 'blue', 'white']

51. find the maximum and minimum values

a = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
mx = max(a, key=lambda x: x[1])
mn = min(a, key=lambda x: x[1])
r = (mx[1],mn[1])
print(r)
(74, 62)

52. Remove None value from a given 
d = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
r = list(filter(lambda x: x != None, d))
print(r)
[12, 0, 23, -55, 234, 89, 0, 6, -12]
'''




