#polimorphism
#one name, many behaviors
#design time/ compile time polimorphism - default arguments
class calculator:
    def add(self, a,b,c=0):
        return a+b+c
calc= calculator()
print(calc.add(10,20))
print(calc.add(10,20,30))

#runtime polimorphism
class Bank:
    def interest_rate(self):
        print("Bank interest rate")

class SBI(Bank):
    def interest_rate(self):
        print("SBI interest rate: 7%")

class HDFC(Bank):
    def interest_rate(self):
        print("HDFC interest rate: 7.5%")

class ICICI(Bank):
    def interest_rate(self):
        print("ICICI interest rate: 7.25%")
sbi = SBI()
sbi.interest_rate()
