a = int(input())

for i in range(a):
    b,c,d = map(int, input().split())
    e = 0
    f = 0
    if d % b == 0:
        e = b * 100
        f = d//b
    else:
        e = (d%b)*100
        f = 1 +d//b
    print(e + f)