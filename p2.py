def cubic (x):
    result=x*x*x
    return result

def cubic2(x):
    return x*x*x

def adder(n1,n2):
    return n1+n2

def avg_three(n1,n2,n3):
    temp=n1+n2+n3
    return temp/3.0

value1=cubic(3)

value2=cubic2(3)

print "value1-", value1
print "value2-", value2


print "adder-", adder(10,1)

print"avg-", avg_three(18, 23, 19)
print"avg-", avg_three(34,31,28)

