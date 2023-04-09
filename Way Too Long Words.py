t=int(input())
for i in range(t):
    s=input()
    r=""
    if(len(s)<=10):
        r=s
    else:
        r=s[0]+str(len(s)-2)+s[len(s)-1]
    print(r)