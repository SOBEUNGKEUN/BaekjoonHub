h, m = input().split()
cook = int(input())

h = int(h)
m = int(m)

h += cook // 60
m += cook % 60

if m >= 60:
    h = h+1
    m = m -60
if h >= 24:
    h = h -24
print(h,m)