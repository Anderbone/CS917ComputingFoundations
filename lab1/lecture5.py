class MyClass:

    i = 12345
    def f(self):
        return 'hello world'




class Complex:
    def __init__(self, realpart, imagpart):
        print("I just created a MyClass object!")
        self.r = realpart
        self.i = imagpart

x = MyClass()
print(x.f())
print(x.i)
y = Complex(3,-4.5)
print(y.r,y.i)
print(Complex.__module__)
