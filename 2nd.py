s="abcd"
t="abcde"
i=0
while i<len(s):
    if s[i] != t[i]:
        print(t[i])
        break
    i+=1
if i == len(s):
    print(t[i])