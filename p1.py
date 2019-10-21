#it will sort the list in ascending order and store the data of list into two diffrent lists containing even and odd numbers,and arrange the list into even ,odd,even ,odd.... 
import random as r

n=int(input("Enter the total length of the list:"))
l=[]
m= []

for j in range(n): 
    a=r.randrange(1,1000)
    l.append(a)
e=[]
o=[]
l.sort()
print("Entered list =",l)
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
        
print("Odd numbers =",o)
print("Even numbers =",e)
if o[0]<e[0]:
    if len(o)>len(e):
        for k in range(len(e)):
            m.append(o[k])
            m.append(e[k])
        for l in range(len(o)-len(e)):
            m.append(o[len(e)+l])    
    if len(o)<len(e):
        for k in range(len(o)):
            m.append(o[k])
            m.append(e[k])
        for l in range(len(e)-len(o)):
            m.append(e[len(o)+l])                                                 
    if len(o)==len(e):
        for k in range(len(e)):
            m.append(o[k])
            m.append(e[k])        
if o[0]>e[0]:
    if len(o)>len(e):
        for k in range(len(e)):
            m.append(e[k])
            m.append(o[k])
        for l in range(len(o)-len(e)):
            m.append(o[len(e)+l])    
    if len(o)<len(e):
        for k in range(len(o)):
            m.append(e[k])
            m.append(o[k])
        for l in range(len(e)-len(o)):
            m.append(e[len(o)+l])                                                 
    if len(o)==len(e):
        for k in range(len(e)):
            m.append(e[k])
            m.append(o[k])                    
print("Output = ",m)            
            
