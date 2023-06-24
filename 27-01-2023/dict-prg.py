# d={1:'Sriram Reddy',2:'Nihanth Reddy'}
# print(type(d))
# print(d.items())
# print(d.keys())
#
d1={1:['KSR','RED'],2:['KNR','BLUE'],3:['RAJ KUMAR','PINK'],4:['AKHIL','BLACK']}
print(d1.items())
d1.update({5:'Sathwik'})
print(d1.items())
d1.pop(3)
print(d1.items())
d1.update({6:'Dharma'})
print(d1.items())
d1.popitem()
print(d1.items())
d1.setdefault(7,'PBR')
print(d1.items())




f