#class
'''
class Addition:
    def add(self):
        self.a = int(input("enter a: "))
        self.b = int(input("enter b: "))
        self.c = self.a + self.b
        print("sum=", self.c)
obj=Addition()
obj.add()
obj.sub()

#creating a class
class dog:
    pass
c = dog()

#creating object
class dog:
    pass
d1 = dog()

#3: Attributes (Data) A dog has: Name, Age, Color.
class dog():
    def __init__(self):
        self.name = "Rocky"
        self.age = 2
d1 = dog()
print(d1.name)

Task 1: Create a Class and Object

class student:
    pass
s1 = student()
print(s1)

o/p: <__main__.student object at 0x00000154D95F2D50>

Task 2: Create Multiple Objects

class student:
    pass
s1 = student()
s2 = student()
s3 = student()
print(s1)
print(s2)
print(s3)

Task 3: Print Object Type
Question: Create a class named Dog. Create two objects and print their types.

class dog:
    pass
d1 = dog()
d2 = dog()
print(type(d1))
print(type(d2))

o/p:
<class '__main__.dog'>
<class '__main__.dog'>

Task 4: Constructor
Question:
Create a class Student. Inside __init__(), print "Student Created". Create two objects.

class student:
    def __init__(self):
        print("student created")
s1 = student()

o/p: student created

Task 5: Constructor Practice
Question: Create a class Book. Print "Book Added" whenever an object is created.

class Book:
    def __init__(self):
        print("book added")
b1 = Book()
b2 = Book()
b3 = Book()
b4 = Book()
b5 = Book()

O/P:
book added
book added
book added
book added
book added

Task 6: Attributes
Question: Create a class Student. Store name and age inside the constructor.

class student:
    def __init__(self):
        self.name = "madhu"
        self.age = 22
s1 = student()
print(s1.name)
print(s1.age)

madhu
22

Task 7: Mobile Class
Question: create a class Mobile with brand and price.

class mobile:
    def __init__(self):
        self.brand = "samsung"
        self.price = 50000
m = mobile()
print(m.brand)
print(m.price)

samsung
50000

Task 8: Employee Class
Question: Create an Employee class with name and salary
# Task 11: Employee Class

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Madhu", 40000)
e2 = Employee("Rahul", 50000)
e3 = Employee("Arun", 60000)

print(e1.name, e1.salary)
print(e2.name, e2.salary)
print(e3.name, e3.salary)

Task 9: Display Method
Question: Create a Student class with a method display().

class student:
    def display(self):
        print("welcome to coimbatore")
s1 = student()
s1.display()

Task 10: Calculator
Question: Create a Calculator class with an add() method.

class calculator:
    def add(self,a,b):
        print(a+b)
c = calculator()
c.add(10,20)
c.add(20,10)

o/p: 30
30

# Task 11: Bike Challenge
class Bike:
    def __init__(self, brand, model, price, name=None):
        self.name = name
        self.brand = brand
        self.model = model
        self.price = price

    def show(self):
        if self.name:
            print("Name :", self.name)
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Price :", self.price)
        print()

b1 = Bike("Yamaha", "R15", 185000, "Madhusudhanan")
b2 = Bike("KTM", "Duke 200", 220000)
b3 = Bike("Honda", "Hornet", 165000)

b1.show()
b2.show()
b3.show()

#Class using while loop
class Current:
    def cur(self):
        n = int(input("n: "))
        if n % 2 == 0:
            n -= 1
        print("Current :", n)
        print("Previous:", n - 2)
cp = Current()
cp.cur()

#class in 4 types of function
Definition: Takes no extra input (except self) and returns nothing.
class addition:
    def add(self):
        a = 20
        b = 30
        print("addition",a+b)
s1 = addition()
s1.add()

output: addition 50

2. Arguments, No Return Value
Definition: Takes input through parameters and prints the result.

class addition:
    def add(self, a, b):
        print("addition",a+b)
s1 = addition()
s1.add(10,20)


3. No Arguments, Return Value
Definition: Takes no input but returns a value.

class addition:
    def add(self):
        a = 20
        b = 30
        return a+b
s1 = addition()
c = s1.add()
print(c)

4. Arguments, Return Value
Definition: Takes input and returns the result.

class Calculator:
    def add(self, a, b):
        return a + b
c = Calculator()
result = c.add(10, 20)
print(result)
#Output: 30

#Constructor
1.Default Constructor (Non-Parameterized Constructor)
A constructor that does not take any arguments other than self.


class student:
    def __init__(self):
        print("default constructor") #Default Constructor
s = student()

class student:
    def __init__(self):
        self.name = "madhu"
        self.age = 22
s1 = student()
print(s1.name)
print(s1.age)

2. Parameterized Constructor
A constructor that accepts arguments.

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1 = student("madhu",22)
s2 = student("ajmal",22)
print(s1.name, s1.age)
print(s2.name, s2.age)

o/p
madhu 22
ajmal 22

#can Python have multiple constructors? no
class Student:

    def __init__(self):
        print("First")

    def __init__(self, name):
        print("Second")


How does Python achieve similar behavior?
By using default parameter values.
class Student:
    def __init__(self,name = "unknown", age=0):
        self.name = name
        self.age = age
s1 = student()
s2 = student("madhu")
s3 = student("rahul", 20)
print(s1.name, s1.age)
print(s2.name, s2.age)
print(s3.name, s3.age)

'''




































