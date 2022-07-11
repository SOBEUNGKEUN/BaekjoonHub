n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0

i = 0
while i < n:
    s += (min(a)*max(b))
    a.remove(min(a))
    b.remove(max(b))
    i+=1
print(s)