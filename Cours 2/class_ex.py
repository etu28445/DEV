class Calc:


    global a
    a = input("Number 1 > ")
    a = int(a)

    global b
    b = input("Number 2 > ")
    b = int(b)

    def addition(self):
        self.c = a + b
        return self.c

    def soustraction(self):
        self.c = a - b
        return self.c

    def multiplication(self):
        self.c = a * b
        return self.c

    def division(self):
        self.c = a / b
        return self.c

calc1 = Calc()

print("\nMake a choice :")
choix = input("(A)ddition / (S)oustraction / (D)ivision / (M)ultiplication : ")

if choix == 'A':
    operator = '+'
    print("Result : ", a, operator, b, "=", calc1.addition())
elif choix == 'M':
    operator = '*'
    print("Result : ", a, operator, b, "=", calc1.multiplication())
elif choix == 'D':
    operator = '/'
    print("Result : ", a, operator, b, "=", calc1.division())
else:
    operator = '-'
    print("Result : ", a, operator, b, "=", calc1.soustraction())