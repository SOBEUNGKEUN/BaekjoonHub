a = int(input())
count = 0;

for i in range(a):
    b = input()
    for j in range(len(b)-1):
        if b[j] != b[j+1]:
            c = b[j+1:]
            if b[j] in c:
                count -= 1
                break
    count += 1
print(count)