'''#without argument
class Addition:
    def add():
        print(10+10)
obj=Addition
obj.add()

#even or odd
class Even:
    def odd():
        if 10 % 2 == 0:
            print("even")
        else:
            print("odd")
obj = Even
obj.odd()


#with ardument
class Argument:
    def age(n):
        if(n>18):
            print("valid")
        else:
            print("Not")
k=Argument
k.age(34)

#biggest of three numbers
class Argument:
    def age(a,b,c):
        if a > b:
            if a > c:
                print("a is bigger")
            else:
                print("c is bigger")
        else:
            if b > c:
                print("b is bigger")
            else:
                print("c is bigger")

a = int(input("a: "))            
b = int(input("b: "))
c = int(input("c: "))    
k=Argument
k.age(a,b,c)

#
class Value:
    def age(n):
        if(n>0):
            return("positive")
        else:
            return("Not")
k=Value
print(k.age(34))


#without return
class Natural():
    def loop(n):
        for i in range(1,n+1):
            print(i)
n = int(input("n: "))
obj = Natural
obj.loop(n)
x
#with return

class Largest():
    def large(n,x):
        mx = x[0] 
        for i in range(n):
            for j in range(i + 1, n):
                if mx > x[j]:
                    mx = x[j]
        return ("largest number is:",mx)

n = int(input("n: "))
x = []
for i in range(n):
    a = int(input("enter values: "))
    x.append(a)
obj = Largest
y = obj.large(n,x)
print(y)
'''
















