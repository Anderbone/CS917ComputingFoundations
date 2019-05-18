class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def add(self, other):
        comm = self.den*other.den

        num = self.num*other.den+other.num*self.den

        return Fraction(num, comm)


if  __name__ == '__main__':
    f = Fraction(3,4)
    f1 = Fraction(1,8)
    f2= f.add(f1)
    for i in range(f.den*f1.den,1,-1):
        if ((f2.den%i==0) & (f2.num%i==0)):
            f2.num = f2.num/i
            f2.den = f2.den/i
    print(str(f2.num)+'/'+str(f2.den))
