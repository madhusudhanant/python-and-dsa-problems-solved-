'''
#inheritence
1. Single Inheritance
Animal
   │
   ▼
 Dog

2. Multilevel Inheritance
Animal
   │
   ▼
Mammal
   │
   ▼
 Dog

3. Hierarchical Inheritance
        Animal
      /    |    \
    Dog   Cat   Cow

4. Multiple Inheritance
Father      Mother
     \      /
      \    /
      Child

5. Hybrid Inheritance
         Animal
        /      \
      Dog      Cat
        \      /
         Puppy

class animal:
    def __init__(self, name):
        self.name = name
    def info(self):
        print("animal name",self.name)
        
class dog(animal):
    def sound(self):
        print(self.name, "barks")

d = dog("Tommy")
d.info()
d.sound()

class animal:
    def __init__(self, name):
        self.name = name
d = animal("madhu")
print(d.name)

# Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Child Class
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)
x = Student("Brad", "Pitt", 2026)
x.printname()
x.welcome()
#Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
#Use the super() Function
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

#1. Single Inheritance
#TASK 1:
class Animal:
    def eat(self):
        print("animal is eating")
class Dog(Animal):
    pass
x = Dog()
x.eat()

animal is eating

#TASK 2:

class Vehicle:
    def start(self):
        print("Vehicle started")
class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")
x = Bike()
x.start()
x.ride()

Vehicle started
Bike is riding


#2. Multilevel Inheritance
# TASK 3

class Animal:
    def eat(self):
        print("animal is eating")
class Mammal(Animal):
    def walk(self):
        print("mammal is walking")
class Dog(Mammal):
    def bark(self):
        print("dog is barking")
x = Dog()
x.eat()
x.walk()
x.bark()

Animal is eating
mammal is walking
dog is barking

#TASK 4
class Person:
    def display_name(self):
        print("Name: MADHUSUDHANAN")
class Employee(Person):
    def display_employee(self):
        print("Salary: 400000")
class Manager(Employee):
    def display_department(self):
        print("department: sortware developement")
m = Manager()
m.display_name()
m.display_employee()
m.display_department()

o/p:
Name: MADHUSUDHANAN
Salary: 400000
department: sortware developement


3. Hierarchical Inheritance
#Task 5

class Animal:
    def eat(self):
        print("Animal is eating")
        
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class cat(Animal):
    def meow(self):
        print("cat says meowww")
class cow(Animal):
    def moo(self):
        print("cow says moooo")

d = Dog()
c = cat()
w = cow()


d.eat()
d.bark()

c.eat()
c.meow()

w.eat()
w.moo()

o/p:
Animal is eating
Dog is barking
Animal is eating
cat says meowww
Animal is eating
cow says moooo

#TASK 6
class Shape:
    def draw(self):
        print("Drawing shape")
        
class Circle(Shape):
    def Area(self):
        print("Area of Circle")
        
class Rectangle(Circle):
    def parameter(self):
        print("Parameter of rectagular")
        
class Triangle(Shape):
    def angles(self):
        print("Triangle has 3 Angles")

c = Circle()
r = Rectangle()
t = Triangle()

c.draw()
c.Area()

print()

r.draw()
r.parameter()

print()

t.draw()
t.angles()


4. Multiple Inheritance
Task 7

# Task 7

class Father:
    def money(self):
        print("Father gives care")
class Mother:
    def love(self):
        print("Mother gives love")
class Child(Father, Mother):
    pass
c = Child()
c.money()
c.love()

# Task 8

class Teacher:
    def teach(self):
        print("Teacher is Teaching")
class Singer:
    def sing(self):
        print("Singer is Singing")

class Person(Teacher, Singer):
    pass

p = Person()
p.teach()
p.sing()


#5. Hybrid Inheritance

# Task 9
class Animal:
    def eat(self):
        print("Animal is Eating")

class Dog(Animal):
    def bark(self):
        print("Dog is Barking")

class Cat(Animal):
    def meow(self):
        print("Cat says Meow")

class Puppy(Dog, Cat):
    def play(self):
        print("Puppy is Playing")

p = Puppy()
p.eat()
p.bark()
p.meow()
p.play()


# ADVANCED CONCEPTS
# 1. Constructor Chaining using super()
class person:
    def __init__(self, name):
        self.name = name
        print("person constructor")
class student(person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
        print("student constructor")
s = student("madhu", 61)
print(s.name)
print(s.roll)

Person Constructor
Student Constructor
Madhu
101

2. Three-Level Constructor Chaining

class A:
    def __init__(self):
        print("A constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("B constructor")

class C(B):
    def __init__(self):
        super().__init__()
        print("C constructor")
x = C()

3. Method Overriding

class animal:
    def sound(self):
        print("animal sound")

class Dog(animal):
    def sound(self):
        print("Dog barks")
d = Dog()
d.sound()

4. Calling Parent Method After Overriding (super())

class animal:
    def sound(self):
        print("animal sound")

class Dog(animal):
    def sound(self):
        super().sound()
        print("Dog barks")
d = Dog()
d.sound()

5. Multilevel Constructor

class grandfather:
    def __init__(self):
        print("grandfather")
class father(grandfather):
    def __init__(self):
        super().__init__()
        print("father")
class son(father):
    def __init__(self):
        super().__init__()
        print("son")
x = son()


# 6.Multiple Inheritence

class father:
    def money(self):
        print("money")
class mother:
    def love(self):
        print("Love")
class child(father, mother):
    def play(self):
        print("play")
c = child()
c.money()
c.love()
c.play()

#7. MRO (Method Resolution Order)
class A:

    def display(self):
        print("A")
class B:
    def display(self):
        print("B")
class C(A, B):
    pass
c = C()
c.display()

#8. real world example
class person:
    def __init__(self, name):
        self.name = name

class employee(person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        
class manager(employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        
    def details(self):
        print("Name      :", self.name)
        print("Salary    :", self.salary)
        print("Department:", self.department)
c = manager("madhu", 55000, "software engineer")
c.details()
'''










