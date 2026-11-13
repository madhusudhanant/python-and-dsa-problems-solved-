#if statement
'''a = 10
b = 20

if(a>b):
    print("a is big")
if(a<b)
    print("b is big")

# Even or odd
a = 13

if a % 2 == 0:
    print("even")
if a % 2 != 0:
    print("odd")


#smallest of two numbers
a = 10
b = 20

if(a<b):
    print("a is small")
if(a>b):
    print("b is big")

#positive or negative

a = -7

if a > 0:
    print("possitive number")

if a < 0:
    print("negative number")


age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for vote")

if age < 18:
    print("Not eligible for vote")

# Profit or Loss

actual_price = int(input("Enter the actual price: "))
sale_price = int(input("Enter the sale price: "))

if actual_price < sale_price:
    profit = sale_price - actual_price
    print("pofit", profit)
if actual_price > sale_price:
    loss =  actual_price - sale_price
    print("loss", loss)

#triangle formed or not

t1 = int(input("Enter the t1: "))
t2 = int(input("Enter the t2: "))
t3 = int(input("Enter the t3: "))

if t1 + t2+ t3 == 180:
    print("triangle frmed")
# Absolute positive value

import math
value = int(input("Enter the value: "))
x = pow(value, 2)
y = math.sqrt(x)
if value > 0:
    print(value)

if value < 0:
    print(int(y))

#if else statement

a = 10
b = 20

if(a>b):
    print("a is big")
else:
    print("b is big")

# Even or odd
a = 13

if a % 2 == 0:
    print("even")
else:
    print("odd") 


#smallest of two numbers
a = 10
b = 20

if(a<b):
    print("a is small")
else:
    print("b is big")


#positive or negative

a = -7

if a > 0:
    print("possitive number")

else:
    print("negative number")


age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for vote")

else:
    print("Not eligible for vote")

# Profit or Loss

actual_price = int(input("Enter the actual price: "))
sale_price = int(input("Enter the sale price: "))

if actual_price < sale_price:
    profit = sale_price - actual_price
    print("pofit", profit)
else:
    loss =  actual_price - sale_price
    print("loss", loss)

#triangle fromed or not

t1 = int(input("Enter the t1: "))
t2 = int(input("Enter the t2: "))
t3 = int(input("Enter the t3: "))

if t1 + t2+ t3 == 180:
    print("triangle frmed")
else:
    print("Not triangle formed")


# Absolute positive value

import math
value = int(input("Enter the value: "))
x = pow(value, 2)
y = math.sqrt(x)
if value > 0:
    print(value)

else:
    print(int(y))

#If else ladder(elif)

# BIGGEST THREE NUMBERS
a = 10
b = 20
c = 2

if( a>b and a>c):
    print("a is bigger")

elif (b>a and b> c):
    print("b ia bigger")

else:
    print("c is bigger") 

# SMALLEST OF THREE NUMBERS

a = 10
b = 20
c = 2

if( a<b and a<c):
    print("a is smaller")

elif (b<a and b< c):
    print("b ia smaller")

else:
    print("c is smaller")  '''
'''

#POSITIVE OR NEGATIVE OR NEUTRAL

a = int(input("Enter the value: "))

if a > 0 :
    print("a is positive")

elif a<0:
    print("a ia negative")

else:
    print("a is neutral")


#ARITHMETIC FUNTIONS
a = int(input("Enter the value: "))
b = int(input("Enter the value: "))
operation = str(input("choose the function 1 or + , 2 or - , 3 or * , 4 or / , 5 or %: "))
                      

if operation == "1" or operation == "+":
    print(a+b)
elif operation == "2" or operation == "-":
    print(a-b)
elif operation == "3" or operation == "*":
    print(a*b)                                           
elif operation == "4" or operation == "/":
    print(a/b)
elif operation == "5" or operation == "%":
    print(a%b)
else:
    print("choose the option correctly")

#TEMPERATURE

a = int(input("Enter the TEMPERATURE: "))


if a <= 0:
    print("Freezing")
elif a > 0 and a <= 10:
    print("very cold")
elif a > 10 and a <= 20:
    print("cold")
elif a > 20 and a <= 30:
    print("normal")
elif a > 30 and a <= 40:
    print("hot")
else:
    print("very hot")


# Equvlent day
a = int(input("Enter tany one number 1 to 0: "))

if a == 1:
    print("sunday")
elif a ==2 :
    print ("monday")
elif a == 3:
    print ("tuesday")
elif a == 4:
    print ("wednesday")
elif a == 5:
    print("thursday")
elif a == 6:
    print("friday")
elif a == 7:
    print("saturday")
else:
    print("choose any between 1 to 7")


#Equivalent month

a = input("Enter any one number 1 to 12 0r month: ")

if a == '1' or a == 'january':
    print("31 days")

elif a ==2 :
    print ("monday")

elif a == 3:
    print ("tuesday")
elif a == 4:
    print ("wednesday")
elif a == 5:
    print("thursday")
elif a == 6:
    print("friday")
elif a == 7:
    print("saturday")
else:
    print("choose any between 1 to 7")

#vowel or consonant
vowel = input("Enter any charectors: ")

if vowel == 'a' or vowel == 'A':
    print("vowel")
elif vowel == 'e' or vowel == 'E':
    print("vowel")
elif vowel == 'i' or vowel == 'I':
    print("vowel")
elif vowel == 'o' or vowel == 'O':
    print("vowel")
elif vowel == 'u' or vowel == 'U':
    print("vowel")
else:
    print("consonant")

#Sales and commision
a = int(input("Enter the sales: "))

if a <= 10000:
    print("commission = ", a/ 100 * 0)
elif a > 10000 and a <= 20000:
    print("commission = ", a/ 100 * 5)
elif a > 20000 and a <= 50000:
    print("commission = ", a/ 100 * 10)
elif a > 50000 and a <= 100000:
    print("commission = ", a/ 100 * 15)
else:
    print("commission = ", (a/ 100 * 20) + 500)

#Gross pay
salary = int(input("Enter the salary: "))


if salary <= 10000:
    print("gross pay is = ", salary +(salary/ 100 * 20) + (salary/ 100 * 80))
elif salary > 10000 and salary <= 20000:
    print("gross pay is = ", salary +(salary/ 100 * 25) + (salary/ 100 * 90))
else:
    print("gross pay is = ", salary +(salary/ 100 * 30) + (salary/ 100 * 95))

#purchasing
tax1 = 10000 / 100 * 10

if a <= 10000:
    print("tax = ", a/ 100 * 0)
elif a > 10000 and a <= 20000:
    tax = a - 10000
    print("tax = ", tax/ 100 * 10)
else:
    tax1 = 10000 / 100 * 10z
    tax2 = a - 20000
    tax3 = tax2 / 100 * 20
    print("tax = ", tax1 + tax3)

#Electricity bill

a = int(input("Enter the unit: "))
amount = 0

if a <= 199:
    print("Charge per unit = ", a * 1.20)
elif a > 200 and a <= 400:
    unit1 = 199 * 1.20
    unit2 = a - 199
    unit3 = unit2 * 1.50
    amount = unit1 + unit3
    print("Charge Per Unit = ", amount)
elif a > 400 and a <= 600:
    unit1 = 199 * 1.20
    unit2 = 200 * 1.50
    unit3= a - 400
    unit5 = unit3 * 1.80 
    amount = unit1 + unit2 + unit5
    print("Charge Per Unit = ", amount)
else:
    unit1 = 199 * 1.20
    unit2 = 200 * 1.50
    unit3 = 200 * 1.80
    unit4 = a - 600
    unit5 = unit4 * 2.00    
    amount = unit1 + unit2 + unit3 + unit5
    print("Charge Per Unit =", amount)

if amount > 400:
    print((amount / 100 * 15) + amount)
if amount < 100:
    print ("minimal amount is = 100 ")
    

'''
































