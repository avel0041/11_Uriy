<<<<<<< HEAD
f = open('26_5.txt').readlines()[1:]
n = f[0]
a = sorted([int(x) for x in f[1:]])[::-1]
k = 0
r = 0

ggfgf
# 1
while len(a)>1:
    if a[0] - a[1] >= 9:
        k+=1
        r = a[1]
        a.remove(a[0])
        a.remove(a[1])
    else:
        a.remove(a[1])
print(k, r)
=======
f = open('26_8.txt').readlines()
sd = []
nesd = []
for g in f[1:]:
    a = [int(x) for x in g.split()]
    if 2 not in a[1:]:
        sr = (sum(a[1:]))/4
        a = [-sr] + [a[0]]
        sd.append(a)
    if 2 in a[1:]:
        sr = (sum(a[1:]))/4
        a = [-sr] + a
        nesd.append(a)

n = int(f[0])//4
sd = sorted(sd)
print(sd[n-1])

nesd = sorted(nesd)
for i in nesd:
    if nesd.count(2)==3:
        
>>>>>>> 85af6feaeaa00eebd2696b7efeed1c2f22153125
