animals=["cat", "dogs", "mouse", "cow"]
for animal in animals:
    print animal

horizontal = ""
for animal in animals:
    horizontal=horizontal+ " " +animal
print horizontal

ages=[18,21,14,7,90,12]
total_age=0
for age in ages:
    total_age=age+total_age

print total_age
print"avgerageage:", total_age/ len(ages)

