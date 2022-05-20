n = int(input())
number = n
count = 0

while True:
    f = number // 10
    s = number % 10
    t = (f + s) % 10
    number = (s * 10) + t

    count += 1
    if(number==n):
        break


print(count)
