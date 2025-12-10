
# #1
# f = open('26_9.txt').readlines()[1:]

# a = []
# for s in f:
#     p = int(s.split()[0])
#     l = str(s.split()[1])
#     a.append([p, l])

# a = sorted(a)
# k = 0

# for c in range(1, 10**10):
#     if sum(x for x, y in a[:c+1])<50000:
#         k = c
    
# print(k)
# des = []
# wor = []
# for x in a:
#     c = int(x[0])
#     lit = str(x[1])
#     if lit == 'G':
#         des.append(c)
#     else:
#         wor.append(c)

# for n in range(1, 2035):
#     su = sum(des[:n+1])+sum(des[:k-n+1])
#     if su < sum(x for x, y in a[:k+1]):
#         print(n)

# while n<=k-n:
#     k+=1
#     n+=1
#     a.append(des[n])
#     while sum(x for x, y in a[:k+1])>50000:
#         u-=1
#         a.remove(wor[-1])

# print(n, 50000-sum(x for x, y in a[:k+1]))




# #1
# f = open('26_9.txt').readlines()
# c=0
# r = ''
# rabd = []
# rabg = []

# for s in f[1:]:
#     c = int(s.split()[0])
#     r = str(s.split()[1])
#     if r == 'D':
#         rabd.append(c)
#     if r == 'G':
#         rabg.append(c)

# rabd = sorted(rabd)[::-1]
# rabg = sorted(rabg)[::-1]

# k = 0
# su = 0

# for i in range(len(rabd)):
#     if su<=2035:
#         su += rabd[i]
#         k+=1
#     else:
#         su = su - rabd[i-1]
#         k-=1
#         for n in range(2, 1000):
#             if 2035-su<=rabg[0]:
#                 su = su - rabd[i-n]
#                 k-=1
#             else:
#                 su += rabg[0]
#                 break
            
# print(k, 2035-su)

# #2
# f = open('26_10.txt').readlines()[1:199156]

# a = [int(x) for x in f[1:199156]]
# data = []

# for s in f[199156:]:
#     m, p = [int(x) for x in s.split()]
#     data.append([p, m])

# for i in range(len(a)):
    
# f = open('26_11.txt').readlines()

# #4
# f = open('26_12.txt').readlines()[1:]

# a = sorted([int(x) for x in f])

# for i in range(len(a)-1):
#     if a[i+1]-a[i]<1000:
        
# print(bin(248)[2:])
# from itertools import*
# k = 0
# for x in product('01', repeat = 6):
#     a = ''.join(x)
#     a = '11'+a
#     if a.count('1')%3==0:
#         k+=1
# print(k)

# #1
# f = open('26_1dz.txt').readlines()[1:]

# num = []
# memb = []
# pri = []
# data = []
# for s in f:
#     n, mem, pr = [int(x) for x in s.split()]
#     num.append(n)
#     memb.append(mem)
#     pri.append(pr)
#     data.append([n, mem, pr])

# a = [[0]*815 for _ in range(725)]

# k = 0

# for i in num:
#     for x in data:
#         if x[0] == i:
#             a[i][x[1]] += x[2]
            
# for i in range(len(a)):
#     a[i] = sorted(a[i])


# print(a)


# a = [0]*724

# for i in num:
#     for x in range(len(data)):
#         if data[x][0]==i: a[i]+=1

# #проданные лоты
# prod = []

# for i in range(len(a)):
#     if a[i]>=2: prod+=[i]

# it = []

# for x in prod:
#     b = []
#     for y in range(len(price)):
#         b.append(price[x][1])
#     b = sorted(b)
#     it.append(b)

# itog = 0

# for x in range(len(it)):
#     itog+=it[x][-2]
# print(len(it), itog)
# #621 161116100

# print(bin(120)[2:])
# from itertools import*
# k = 0
# for x in product('01', repeat = 6):
#     a = '10'+''.join(x)
#     if a.count('1') == a.count('0'): k +=1
# k = k*2**8
# print(k)

# #3
# f = open('26_3dz.txt').readlines()[1:]
# n = 10000
# r = 1021000
# v = 11111

# a = [int(x) for x in f]
# u = 0
# km = 0

# for i in range(len(a)-1):
#     if v>a[i+1]-a[i]:
#         v = v - (a[i+1]-a[i])
#     else:
#         v = 11111-a[i+1]
#         km = a[i+1]
#         u+=1
# print(u, km)
# #9763 570123

#4
f = open('26_4dz.txt').readlines()[1:]

s = 8200 #свободное место на диске
n = 970 #пользователи

a = sorted([int(x) for x in f])
k = []
r = 0

for i in range(len(a)):
    if sum(a[:i+1])<=s:
        k.append(a[i])
        r = s - sum(a[:i]) #оставшееся место без последнего файла
    else: break

mas = 0

for i in range(len(a)-1, -1, -1):
    if a[i]<=r:
        mas = a[i]
        break

print(len(k), mas)
#568 50 

# #3
# f = open('26_3dz.txt').readlines()[1:]
# n = 10000
# r = 1021000
# v = 11111

# a = [int(x) for x in f]
# u = 0
# km = 0

# for i in range(len(a)-1):
#     if v>a[i+1]-a[i]:
#         v = v - (a[i+1]-a[i])
#     else:
#         v = 11111-a[i+1]
#         km = a[i+1]
#         u+=1
# print(u, km)
# #9763 570123

#4
f = open('26_4dz.txt').readlines()[1:]

s = 8200 #свободное место на диске
n = 970 #пользователи

a = sorted([int(x) for x in f])
k = []
r = 0

for i in range(len(a)):
    if sum(a[:i+1])<=s:
        k.append(a[i])
        r = s - sum(a[:i]) #оставшееся место без последнего файла
    else: break

mas = 0

for i in range(len(a)-1, -1, -1):
    if a[i]<=r:
        mas = a[i]
        break

print(len(k), mas)
#568 50 
