# Текстовый файл состоит не более чем из 10^6 символов A, B и C. 
# Определите максимальное количество идущих подряд символов C.

f = open('24_0.txt').readline()
a=[x for x in f.replace('A', ' ').replace('B', ' ').split()]

print(len(max(a, key=len)))