a = int(input())
b = int(input())

c = b % 10
d = b % 100 // 10
e = b // 100
print(a*c)
print(a*d)
print(a*e)
f = a*d*10
g = a*e*100

print(a*c + f + g)
