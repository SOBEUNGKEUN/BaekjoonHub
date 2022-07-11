n = int(input())

p = list(map(int, input().split()))
i = 1
p.sort()
while i < len(p):
   p[i] = p[i]+p[i-1]
   i+=1
print(sum(p))
