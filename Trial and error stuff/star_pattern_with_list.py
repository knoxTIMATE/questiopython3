l1=[]
l2=[]
n=6
for i in range (-(n-1), 1):
    l1.append(' '*(-i))
    print (i)
    
for j in range (1,n+1):
    l2.append('#'*j)
    
for k in range (n):
    print (l1[k], l2[k])