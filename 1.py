from itertools import*
k = 0
for x in product('01', repeat = 14):
    a = ''.join(x)
    if a.count('1')+5>a.count('0')+13:
        k+=1
print(k)