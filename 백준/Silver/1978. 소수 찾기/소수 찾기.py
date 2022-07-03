n = int(input())
l = list(map(int, input().split()))

count = 0

for i in l:
    a=0
    if i == 1:
        continue
    for j in range(2, i):
        if i%j ==0:
            a = 1
    if a ==0:
        count +=1
print(count)