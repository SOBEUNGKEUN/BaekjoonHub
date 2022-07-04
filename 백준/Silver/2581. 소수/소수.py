a = int(input())
b = int(input()) 
arr = []

for i in range(max(2,a), b+1):
    c = True
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            c = False
            break
    if c :
        arr.append(i)
if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)