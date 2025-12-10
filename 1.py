from turtle import*
screensize(1000, 1000)
color('black')
tracer(0)
k = 10
lt(90)
pd()

rt(90)
for x in range(3):
    fd(15*k)
    rt(90)
    fd(20*k)
    rt(90)
pu()
fd(7*k)
rt(90)
fd(13*k)
lt(90)
pd()
for x in range(2):
    fd(10*k)
    lt(90)
    fd(17*k)
    lt(90)
pu()

for x in range(-30*k, 30*k, k):
    for y in range(-30*k, 30*k, k):
        goto(x, y)
        dot(4, 'red')
done()

print(11*18+16*21-9*14)
#408