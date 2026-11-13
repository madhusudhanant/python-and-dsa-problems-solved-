'''
###BIGGEST OF THREE NUMBERS
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b:
    if a > c:
        print("A is bigger")
    else:
        print("C is bigger")
else:
    if b > c:
        print("B is bigger")
    else:
        print("C is bigger")

###SMALLEST OF THREE NUMBERS
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a < b:
    if a < c:
        print("A is smaller")
    else:
        print("C is smaller")
else:
    if b < c:
        print("B is smaller")
    else:
        print("C is smaller")

'''
'''
###BIGGEST OF FOUR NUMBERS
a = int(input("Enter a: "))#50
b = int(input("Enter b: "))#90
c = int(input("Enter c: "))#70
d = int(input("Enter d: "))#100

if a > b:
    if a > c:
        if a > d:
            print("A is Bigger")
        else:
             print("D is Bigger")
    else:
        if c > d:
             print("C is Bigger")
        else:
             print("D is Bigger")
else:
    if b > c:
        if b > d:
             print("B is Bigger")
        else:
             print("D is Bigger")
    else:
        if c > d:
             print("C is Bigger")
        else:
             print("D is Bigger")

###SMALLEST OF FOUR NUMBERS
a = int(input("Enter a: "))#50
b = int(input("Enter b: "))#90
c = int(input("Enter c: "))#70
d = int(input("Enter d: "))#100

if a < b:
    if a < c:
        if a < d:
             print("A is Smaller")

        else:
             print("D is Smaller")
    else:
        if a < d:
            print("A is Smaller")
        else:
            print("D is Smaller")
else:
    if b < c:
        if b < d:
            print("B is Smaller")
        else:
            print("D is Smaller")
    else:
        if c < d:
            print("C is Smaller")
        else:
            print("D is Smaller")o


###STUDENT GRADE
s1 = int(input("Enter your grade: "))
s2 = int(input("Enter your grade: "))
s3 = int(input("Enter your grade: "))
s4 = int(input("Enter your grade: "))
s5 = int(input("Enter your grade: "))

avg = (s1 + s2 + s3 + s4 + s5) // 5
print(avg)
if s1 >= 35 and s2 >= 35 and s3 >= 35 and s4 >= 35 and s5 >= 35:
    if avg >= 90:
        print("A Grade")
    else:
        if avg >= 80:
            print("B Grade")
        else:
            if avg >= 70:
                print("C Grade")
            else:
                if avg >= 60:
                    print("D Grade")
                else:
                    print("E Grade")
else:
    print("Fail")

### LEAP YEAR OR NOT
        
a = int(input("n: "))
if a % 100 == 0:
    if a % 400 == 0:
        print(a,"is leap year")
    else:
        print(a,"is not leap year")
else:
    if a % 4 == 0:
        print(a,"is leap year")
    else:
        print(a,"is not leap year")

### SWITCH CASE ###

#Equivalent day

d = int(input("Enter day( 1 to 7 any one number): "))

match d:
    case 1:
        print("Sunday")
    case 2:
        print("monday")
    case 3:
        print("tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("thursday")
    case 6:
        print("friday")
    case 7:
        print("saturday")
    case _:
        print("invalid")

#Equivalent month
m = int(input("Enter month( 1 to 12 any one number): "))

match m:
    case 1:
        print("january")
    case 2:
        print("february")
    case 3:
        print("march")
    case 4:
        print("april")
    case 5:
        print("may")
    case 6:
        print("june")
    case 7:
        print("july")
    case _:
        print("auguest")


#Equivalent month 

m = input("Enter month( 1 to 12 any one number): ")

match m:
    case '1' | 'january':
        print("31 days")
    case 's' | 'february':
        print("28 days")
    case '3' | 'march':
        print("30 days")
    case "4" | "april": 
        print("31 days")
    case '5' | 'may':
        print("may")
    case '6' | 'june':
        print("june")
    case '7' | 'july':
        print("july")
    case '8' | 'auguest':
        print("auguest")
    case _:
        print("Invalid")


### vowel or consnent
v = input("Enter month( 1 to 12 any one number): ")

match v:
    case 'a' | 'A':
        print("vowel")
    case 'e' | 'E':
        print("vowel")
    case 'i' | 'I':
        print("vowel")
    case _:
        print("consonant")





### CALCULATE FUNCTION
a = int(input("Enter calculation a: "))
b = int(input("Enter calculation b: "))
c = str(input("Function enter + or add, - or sub, * or mul, / or div, % or mod: "))

match c:
    case '+' | 'add':
        print(a + b)
        
    case '-' | 'sub':
        print(a - b)
    case '/' | 'div':
        print(a / b)
    case '*' | 'mul': 
        print(a * b)
    case '%' | 'mod':
        print(a % b)
    case _:
        print("Invalid")


### SI AND CI

a = str(input("enter sun si or ci: "))


match a:
    case "si":
        p = int(input("Enter p: "))
        r = int(input("Enter r: "))
        t = int(input("Enter t: "))
        si =(p * r * t) / 100
        print(si)
        
    case "ci":
        p = int(input("Enter p: "))
        r = int(input("Enter r: "))
        t = int(input("Enter t: "))
        ci = p *(( 1 + (r / 100))* t - 1)
        print(ci)
'''

































































