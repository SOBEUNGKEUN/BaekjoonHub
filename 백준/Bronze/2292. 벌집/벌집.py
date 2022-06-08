n = int(input())
a = 1
for i in range(n):
    a += i*6
    if n <= a:
        print(i+1)
        break