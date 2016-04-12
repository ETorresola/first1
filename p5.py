def absolute(N):
    if N<0:
        return -1*N
    else:
        return N

print "|-1|=", absolute(-1)
print "|100|=",absolute (100)
print "|0|=", absolute (0)

x=10
if x<0:
    print 'Negative'
elif x==0:
    print 'Zero'

else:
    print 'Positive'
def get_tax_ammount(salary):
    if salary<20000:
        return 0
    elif salary>=20000 and salary<50000:
        return salary*0.15
    elif salary>=50000 and salary<100000:
        return salary*0.2
    else:
        return salary*0.33
print "Bob Tax-", get_tax_ammount(30000)
print "Jil Tax-", get_tax_ammount(45000)
print "Apu Tax-", get_tax_ammount(130000)
print "Tom Tax-", get_tax_ammount(170000)