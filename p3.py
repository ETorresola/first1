import math

def find_hypotenuse(a,b):
    hypotenuse=math.sqrt((a*a)+(b*b))
    return hypotenuse

hypotenuse1=find_hypotenuse(3,4)

print "hypotenuse1-", find_hypotenuse(3,4)


def print_name(name):
    print "person name:"+name
print_name("Jose")
