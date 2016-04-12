def adder(N):
    i=0
    accumulator=0
    while (i<N):
        i=i + 1
        accumulator= accumulator+i
    return accumulator

print "adder(5):" , adder(5)
print "adder (10):", adder(10)

###
done=False
while not done:
    character=input (str("Enter some value:"))
    if character.isdigit():
        print "Is digit"
    elif character.isalpha():
        print "Is Letter"
    else:
        done=True
        print "Thanks for using this program"

