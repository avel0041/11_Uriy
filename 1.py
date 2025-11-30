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
    
f = open('26_11.txt').readlines()
