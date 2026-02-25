s1='1100'
s2='1111'
m=0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        m+=1
if m%2==0:
    print(m//2)
else:
    print(-1)
