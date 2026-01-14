from re import*

f = open('24_6029.txt').readline()
a = findall(r'(?:EF)+E?|(?:FE)+F?', f)
print(len(max(a, key = len)))