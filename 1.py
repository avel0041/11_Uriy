# 4 4 4 4 4 = 1024
from itertools import*
n=0
for x in product('абвгд', repeat=5):
    a=''.join(x)
    f = 0
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            f = 1
            break
    if a[0]!='а' and f==0:
        n+=1
print(n)