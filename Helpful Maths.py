s=input()
l=[i for i in s if (i!='+')]
l.sort()
s='+'.join(l)
print(s)

