def fn(x, n):
    c=''
    while x>0:
        c+=str(x%n)
        x=x//n
    return c[::-1]