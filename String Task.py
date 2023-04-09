s=input()
vowels=['a','e','i','o','u','y']
r=""
s=s.lower()
for i in s:
    if i not in vowels:
        r+='.'
        r+=i
print(r)

