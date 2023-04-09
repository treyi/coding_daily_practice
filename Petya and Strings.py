a=list(input().lower())
b=list(input().lower())
t=0
for i in range(len(a)):
    if (a[i]<b[i]):
        t=-1
        break
    elif(b[i]<a[i]):
        t=1
        break
print(t) 
    

