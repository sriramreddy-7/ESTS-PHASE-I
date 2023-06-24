n=int(input())
l=[]
for i in range(0,n):
    x=int(input())
    l.append(x)
    
for i in range(0,n):
    for j in range(0,n):
        if(l[i]<l[j]):
            l[i],l[j]=l[j],l[i]
        
m=[]
for i in l:
    if i%2==0:
        m.append(i)
       
for i in l:
    if i%2!=0:
        m.append(i)
       
        
print(m)
