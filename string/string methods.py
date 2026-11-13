'''
1.capitalize() - "Hello, And Welcome To My World!"


t = "hello, world"
x=t.capitalize()
print(x)

2.casefold() - Converts string into lower case 

t = "Hello, And Welcome To My World!"
x=t.casefold()
print(x)

3. center() - Returns a centered string

t = "madhu"
x=t.center(10)
print(x)

4. count() - Returns the number of times a specified value occurs in a string

t = "madhu, love appaple but i love madhu"
x=t.count("madhu")
print(x)

5. encode() - Returns an encoded version of the string
txt = "My name is madhu"
x = txt.encode()
print(x)

6. endswith() - Returns true if the string ends with the specified value
txt = "My name is madhu!"
x = txt.endswith("!")
print(x)

7. expandtabs() - Sets the tab size of the string

txt = "H\te\tl\tl\to\tw"
x = txt.expandtabs(3)
print(x)  # Output: H e l l o

8. find() - Searches the string for a specified value and returns the position
txt = "Hello, welcome to my world."
x = txt.find("to")
print(x)  # Output: 7


9. format() - Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))  # Output: For only 49.00 dollars!


10. index() - Same as find() but raises an error if not found

txt = "Hello, welcome to my world."
x = txt.index("e", 1, 5)
print(x)  # Output: 7

11. isalnum() - Returns True if all characters are alphanumeric

txt = "Compan1"
x = txt.isalnum()
print(x)  # Output: True

12. isalpha() - Returns True if all characters are in the alphabet

txt = "CompanyX"
x = txt.isalpha()
print(x)  # Output: True

13. isupper() - Returns True if all characters in the string are uppercase
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)  # Output: True

14. join() - Joins the elements of an iterable

myTuple = ["John", "Peter", "Vicky"]
x = "#".join(myTuple)
print(x)  # Output: John#Peter#Vicky
 

15. lower() - Converts a string into lower case
txt = "Hello my FRIENDS"
x = txt.lower()

16. lstrip() - Returns a left trim version of the string
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
# Output: of all fruits banana      is my favorite

txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)  # Output: banana

17. replace() - Replaces a string with another string
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)  # Output: I like apples
 # Output: I like apples

18. split() - Splits the string into a list

txt = "welcome, to the jungle"
x = txt.split(",")
print(x)  # Output: ['welcome', 'to', 'the', 'jungle']

19. splitlines() - Splits the string at line breaks
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)  # Output: ['Thank you for the music', 'Welcome to the jungle']

20. upper() - Converts a string into upper case
txt = "Hello my friends"
x = txt.upper()
print(x)  # Output: HELLO MY FRIENDS



######## Built-in Math Functions
1.min(), max() - Find minimum or maximum value
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)  # Output: 5
print(y)  # Output: 25


2.abs() - Returns the absolute (positive) value
x = abs(-7.25)
print(x)  # Output: 7.25

3.pow(x, y) - Returns the value of x to the power of y (x^y)
x = pow(4, 3)
print(x)  # Output: 64


##### The Math Module

math.sqrt() - Returns the square root of a number

x = math.sqrt(64)
print(x)  # Output: 8.0

round - rounds the given floor number is above .5
x = round(69.6)
print(x)  # Output: 70


math.ceil() and math.floor() - Round a number up or down
import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)  # Output: 2
print(y)  # Output: 1

math.pi - Returns the value of PI
'''
import math
x = math.pi
print(x)  # Output: 3.141592653589793

































