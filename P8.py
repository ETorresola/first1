class ComplexNumber(object):
    def __init__(self, a=0, b=0):
     self.a=a
     self.b=b

    def __str__(self):
        return str(self.a)+"+"+str(self.b)+"i"
    def conjugate(self):
        return ComplexNumber(self.a, -1*self.b)
    def add(self, X):
        return ComplexNumber(self.a + X.a, self.b + X.b)
    def subtract(self, X):
        real=self.a-X.a
        imaginary=self.b-X.b
        return ComplexNumber(real, imaginary)

##test
c1= ComplexNumber(2,4)
c2= ComplexNumber(-9, 20)
print "c1:", c1
print "c1.conjugate()", c1.conjugate()
print "c2:", c2
print "c2.conjugate()", c2.conjugate()

print "c1+c2:", c1.add(c2)
print "c1+c1.conjugate()", c1.add(c1.conjugate())

print "c1-c2:", c1.subtract(c2)