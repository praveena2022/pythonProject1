'''res=ord('Z')
print(res)

for i in range(65,91):
    ch=chr(i)
    print(ch)
#input:abc  output=bcd
s=input()
s1=''
for i in s:
    s1=s1+chr(ord(i)+1)
print(s1)'''

#input: aabbaaaaadaaa
#a
#ouput=5 (max frequency character)
from collections import Counter
s=input()
res=Counter(s)
res=max(res,key=res.get)
print(res)