f = open('C:/Users/Юрий/Desktop/sadaf/11_Uriy/26_8.txt').readlines()
sd = []
nesd = []
for g in f[1:]:
    a = [int(x) for x in g.split()]
    if 2 not in a[1:]:
        sr = (sum(a[1:]))/4
        a = [-sr] + [a[0]]
        sd.append(a)
    if 2 in a[1:]:
        a = [a.count(2)] + [a[0]]
        nesd.append(a)

n = int(f[0])//4
sd = sorted(sd)
print(sd[n-1])

nesd = sorted(nesd)
for i in range(len(nesd)):
    if nesd[i][0]>=3:
        print(nesd[i][-1])
        break
