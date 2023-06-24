nl=[]
for i in range(0,5):
    name=input('Enter the Name of Students: ')
    nl.append(name)
ml=[]
for i in range(0,9):
    marks=input('Enter the Marks of Students: ')
    ml.append(marks)
ml.sort()
print(ml[8])
print(ml[0])

print(min(ml))
print(max(ml))