def iint():
    return int(input().strip())

a = iint()
b = iint()
c = iint()
d = iint()
e = iint()
f = iint()

if 3*a+2*b+c == 3*d+2*e+f:
    print('T')
elif 3*a+2*b+c > 3*d+2*e+f:
    print('A')
else:
    print('B')