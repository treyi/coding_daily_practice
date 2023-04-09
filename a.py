t=int(input())
for t1 in range(t):
    s=input()
    a=0
    b=0
    for i in s:
        if(i=='a'):
            a+=1
        else:
            b+=1
    ans="YES" if a==b else "NO"
    print(ans)