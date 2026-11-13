'''
Error: Issues in the program logic such as SyntaxError, etc. It occurs at compile time.
Exception: Problems that occur at runtime and can be managed using exception handling (e.g., invalid input, missing files).

#1. SYNTEX ERROR
amount = 1000

if amount > 2999
    print("you are eligible to purchace Dsa self paced")
# syntxt error excepted (:)

#2. TYPE OF ERROR

try:
    a = 10
    b = "hari"
    c = a+b
    print(c)
except TypeError as t:
    print(t)

o/p : unsupported operand type(s) for +: 'int' and 'str'


# 3. NAME ERROR:
try:
    a = 10
    b = 20
    c = a+d
    print(c)
except NameError as n:
    print(n)
o/p: name 'd' is not defined



#4. INDEX ERROR

try:
    k = [1,2,True]
    print(k[3])
except IndexError as i:
    print(i)

o/p: list index out of range

# 5. KEY ERROR

try:
    d = {"name" : "hari", "age": 20}
    emp_name = d ["name"]
    print(emp_name)
    emp_age = d ["year"]
    print(emp_age)
except KeyError as k:
    print("key is not matched")

o/p:
hari
key is not matched "year"

# 6. VALUE ERROR

try:
    x = int(input("n:"))
    print(x)
except ValueError as v:
    print(v)

o/p: n:madhu
invalid literal for int() with base 10: 'madhu'

#7. ATTRIBUTE ERROR

try:
    t = (2,3,True)
    p = int(input("enter value: "))
    t.append(p)
    print(t)
except AttributeError as a:
    print(a)

o/p: enter value: 54
'tuple' object has no attribute 'append'

#8. IO ERROR

try:
    f = open("demo.png")
    f.write("loreum ispoum")
except IOError as ioe:
    print(ioe)
o/p: [Errno 2] No such file or directory: 'demo.png'

#9. ZERO DIVISION ERROR

try:
    a = 10
    b = 0
    c = a/b
    print(c)
except ZeroDivisionError as z:
    print(z)

o/p: division by zero

#10. IMPORT ERROR
The ModuleNotFoundError exception is raised when a module is not found during the import process

try:
    import Tensorflow
    print("hari")
except ImportError as im:
    print(im)

o/p: No module named 'Tensorflow'

#methods#
#### tryelse

try:
    print("Hello")
except:
    print("Error found")
else:
    print("nothing went wrong")

# Finally
This block always run if error occured or not

a = [1,2,3]
try:
    print("second element",a[1])
    print("thrid element",a[3])
except:
    print("an error occured")
finally:
    print(a[0])
    print("hello madhu")
    print(a[0])

o/p:
second element 2
an error occured
1
hello madhu
1

# Custome Exception
A student enters the exam hall.
You check: Hall Ticket? If missing:
You say: ExamNotAllowedError
Python doesn't have this error.
So you create it.

class ExamNotAllowedError(Exception):
    pass
Then: raise ExamNotAllowedError("Bring Hall Ticket")
Output: ExamNotAllowedError: Bring Hall Ticket

class InValidAge(Exception):
    pass
def calculate():
    number = 18
    try:
        age = int(input("Enter age: "))
        if age < number:
            raise InValidAge
        else:
            print("age is elegible for vote")
    except InValidAge:
        print("age is not eligible for voting")
        calculate()
calculate()

o/p:
Enter age: 17
age is not eligible for voting
Enter age: 18
age is elegible for vote

#Custom exception
class NotEligible(Exception):
    pass
def eligiblityForLoan():
    eligible_salary = 15000
    eligible_cibil = 700
    try:
        salary = int(input("Enter your monthly salary: "))
        cibil = float(input("Enter cibil score: "))
        if salary < eligible_salary or cibil < eligible_cibil:
            raise NotEligible
        else:
            print("your record is eligible for sanctaning loan")
    except NotEligible:
        print("you doesn't have enough credit for applying loan")
eligiblityForLoan()

o/p:
Enter your monthly salary: 12000
Enter cibil score: 250
you doesn't have enough credit for applying loan


#solving

1. Division by Zero
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Answer =", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input.")

2. Integer Input
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Invalid number.")

3. List Index
numbers = [10, 20, 30, 40]

try:
    index = int(input("Enter index: "))
    print(numbers[index])

except IndexError:
    print("Index out of range.")

except ValueError:
    print("Invalid input.")


4. calculater
try:
    a = int(input("Enter first number: "))
    op = input("Enter operator (+ - * /): ")
    b = int(input("Enter second number: "))

    if op == "+":
        print(a + b)

    elif op == "-":
        print(a - b)

    elif op == "*":
        print(a * b)

    elif op == "/":
        print(a / b)

    else:
        raise ValueError("Invalid operator")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError as e:
    print(e)


5. Dictionary Lookup
student = {
    "name": "Madhu",
    "age": 22
}

try:
    key = input("Enter key: ")
    print(student[key])

except KeyError:
    print("Key not found.")
    
6. Tuple Access

t = ("apple", "banana", "orange")

try:
    index = int(input("Enter index: "))
    print(t[index])

except ValueError:
    print("Invalid integer.")

except IndexError:
    print("Index out of range.")


#7. Using else
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    ans = a / b

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input.")

else:
    print("Division successful.")
    print("Answer =", ans)


8. Using finally
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Answer =", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input.")

finally:
    print("Program finished.")


9. custom exception
try:
    age = int(input("Enter age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age =", age)

except ValueError as e:
    print(e)

10. ATM Withdrawal

balance = 5000
try:
    amount = int(input("Enter withdrawal amount: "))

    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    if amount > balance:
        raise ValueError("Insufficient balance.")

    balance -= amount

    print("Withdrawal successful.")
    print("Remaining Balance =", balance)

except ValueError as e:
    print(e)


11. Login System (3 Attempts)

username = "madhusudhanan"
password = "1234"

def loginsystem(attempt):
    try:
        u = input("username: ")
        p = input("password: ")
        if u == username and p == password:
            print("Login Successfull")
        else:
            raise ValueError("invalid username or password")
    except ValueError as e:
        print(e)
        attempt += 1
        if attempt == 2:
            print("1 attempt remaining")
    if attempt == 3:
        print("account locked")
        return
    loginsystem(attempt)
loginsystem(0)

12. Student Marks Validation

marks = []
while len(marks) < 5:
    try:
        mark = int(input(f"enter mark {len(marks)+1}: "))
        if mark < 0 or mark > 100:
            raise ValueError("Marks should be between 0 and 100")
        marks.append(mark)
    except ValueError as e:
        print(e)
print("marks:" ,marks)
print("average =", sum(marks)/len(marks))

marks: [20, 20, 30, 40, 50]
average = 32.0

13. File Handling

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program finished.")


14. Multiple Exceptions Together
numbers = [10, 20, 30]
try:
    index = int(input("Enter index: "))
    num = int(input("Enter divisor: "))

    print(numbers[index] / num)

except ValueError:
    print("Invalid number.")

except IndexError:
    print("Invalid index.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# 15. banking system
balance = 10000

while True:
    try:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            amount = int(input("Enter deposit amount: "))

            if amount <= 0:
                raise ValueError("Amount must be positive.")

            balance += amount
            print(balance,"Deposited Successfully.")

        elif choice == 2:
            amount = int(input("Enter withdrawal amount: "))

            if amount <= 0:
                raise ValueError("Amount must be positive.")

            if amount > balance:
                raise ValueError("Insufficient balance.")

            balance -= amount
            print("Withdrawal Successful.")

        elif choice == 3:
            print("Balance =", balance)

        elif choice == 4:
            print("Thank You!")
            break

        else:
            raise ValueError("Invalid choice.")

    except ValueError as e:
        print(e)

'''




























