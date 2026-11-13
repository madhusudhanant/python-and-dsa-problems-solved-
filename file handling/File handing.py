'''
#File Handling in Python
For Creating, reading, writing, appending, and deleting files.
files are used to store data permanently on the disk

usage:
    1. Files helps to store data permanently in disk
    2. Files shared across syatems
    3. files allow reading, updateing and deleting
    4. Automationing taskes like logging, data backups and configuration handling

File models in python:
•	'r'  : Read mode. Opens the file for reading (default). Error if the file does not exist.
•	'w'  : Write mode. Creates a new file or overwrites an existing file.
•	'a'  : Append mode. Opens the file for appending. Adds new content at the end without deleting existing data.
•	'x'  : Exclusive creation. Creates a new file but returns an error if the file already exists.
•	'b'  : Binary mode. Used to handle binary files (images, videos, audio).
•	't'  : Text mode. Used for text files (default).
•	'r+' : Opens file for both reading and writing

Examples of File Handling in Python:

#1. write a file


f = open('madhu.txt', 'w')
f.write('im coding in python')
f.close()

#2. read from a file
f = open('madhu.txt', 'r')
print(f.read())
f.close()

#3 read only first 5 characters
f = open('madhu.txt', 'r')
print(f.read(5))
f.close()

#4 read one line
f = open("madhu.txt", "r")
print(f.readlines()) #readlines() Returns all lines as a list
f.close()

#5 read file line by line using loop
f = open('madhu.txt','r')
for x in f:
    print(x)
f.close()

#6 append to a file
f = open('madhu.txt','a')
f.write('\nin ysa')
f.close()

#7 read file after appending
f = open('madhu.txt', 'r')
print(f.read())
f.close()


#delete a file
import os
if os.path.exists('madhu.txt'):
    os.remove('madhu.txt')
else:
    print('the file does not exist')

#remove a folder
import os
os.rmdir('madhu')

try:
    x = 10 / 0
except Exception as e:
    f = open('madhu.txt', 'a')
    f.write(str(e) + '\n')
    f.close()

#Task 1: Create a File
f = open('student.txt','w')
f.write('helo im madhusudhanan')
f.close()

#Task 2: Read a File
f = open('student.txt','r')
print(f.read())
f.close()


#Task 3: Overwrite a File

f = open("student.txt", "w")
f.write("Python is awesome")
f.close()


#Task 4: Append to a File
f = open('student.txt', 'a')
f.write('\ni love python')
f.close()


#Task 5: Read First 10 Characters

f = open('student.txt', 'r')
print(f.read(10))
f.close()

#Task 6: Write Multiple Lines and Read Using a Loop
f = open("fruits.txt", "w")
f.write("Apple\n")
f.write("Banana\n")
f.write("Orange\n")
f.write("Mango")
f.close()

f = open("fruits.txt", "r")
for line in f:
    print(line, end="")
f.close()

#log errors

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Answer =", a / b)

except Exception as e:
    print(e)

    f = open("errors.txt", "a")
    f.write(str(e) + "\n")
    f.close()

#Bonus Task 14: Delete a File

import os

if os.path.exists('fruits.txt'):
    os.remove('fruits.txt')
    print('file deleted')
else:
    print("file does not exist")

mini notes app

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        note = input("Enter note: ")
        f = open("notes.txt", "a")
        f.write(note + "\n")
        f.close()

    elif choice == "2":
        try:
            f = open("notes.txt", "r")
            print(f.read())
            f.close()
        except FileNotFoundError:
            print("No notes found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")


# File handling menu program
def read():
    try:
        f = open("madhus.txt", 'r')
        print(f.read())
        f.close()
    except FileNotFoundError as e:
        print("file is not found")

def write():
    f = open("madhus.txt", "w")
    v = input("write here: ")
    f.write(v)
    f.close()

def append():
    f = open("madhus.txt", 'a')
    v1 = input("append: ")
    f.write(v1)
    f.close()

def delete():
    import os
    if os.path.exists("madhus.txt"):
        os.remove('madhus.txt')
        print('file deleted')
    else:
        print("file does not exist")


def choice():
    while True:
        print("\n1.read")
        print("2.write")
        print("3.append")
        print("4.delete")
        try:
            choice = int(input("choice: "))
            if choice == 1:
                read()
            elif choice == 2:
                write()
            elif choice == 3:
                append()
            elif choice == 4:
                delete()
            else:
                print("invalid choice")
        except ValueError as v:
            print("invalid choice")
    choice()
choice()

#File handling menu advanceed
import os
def read(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File does not exist.")
        ch = input("Do you want to create it? (y/n): ")
        if ch.lower() == "y":
            write(filename)
        else:
            print("Returning to menu...")


def write(filename):
    data = input("Write here: ")
    with open(filename, "w") as f:
        f.write(data)
    print("File saved successfully.")


def append(filename):
    try:
        data = input("Append here: ")
        with open(filename, "a") as f:
            f.write("\n" + data)
        print("Data appended successfully.")

    except Exception as e:
        print("Error:", e)


def delete(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully.")
    else:
        print("File does not exist.")


def choice():
    while True:
        print("1. Read File")
        print("2. Write File")
        print("3. Append File")
        print("4. Delete File")
        print("5. Exit")
        try:
            ch = int(input("Enter your choice: "))

            if ch == 1:
                filename = input("Enter file name: ")
                read(filename)

            elif ch == 2:
                filename = input("Enter file name: ")
                write(filename)

            elif ch == 3:
                filename = input("Enter file name: ")
                append(filename)

            elif ch == 4:
                filename = input("Enter file name: ")
                delete(filename)

            elif ch == 5:
                print("Thank you! Goodbye.")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter numbers only.")
choice()
'''











