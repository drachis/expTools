import random

def randomRow():
    r = range(1,10)
    r2 = r
    x = []
    
    for n in r:
        x.append(n)
    return x

a = randomRow()
b = a[3:] + a[0:3]
c = a[6:] + a[0:6]

d = a[1:]+a[0:1]
e = a[4:]+a[0:4]
f = a[7:]+a[0:7]

g = a[2:]+a[0:2]
h = a[5:]+a[0:5]
i = a[8:]+a[0:8]


print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
