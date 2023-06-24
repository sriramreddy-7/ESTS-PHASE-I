s=input('Enter any String  :')
k=0
l=[]
r=[]
for i in s:
    l.append(i)
r=l
r.reverse()
for i in range(0,len(l)):
    if l[i]!=s[i]:
        k=k+1
if k>1:
    print('Not a Palindrome')
else:
    print('Palindrome')

###############################
print('Method-2')
rev=s[::-1]
if s==rev:
    print('Palindrome')
else:
    print('Not a Palindrome')