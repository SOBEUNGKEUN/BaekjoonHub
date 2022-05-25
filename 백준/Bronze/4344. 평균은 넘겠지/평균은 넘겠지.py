n = int(input())

for i in range(n):
    list_a = list(map(int, input().split()))
    avg = sum(list_a[1:])/list_a[0]  
    cnt = 0
    for j in list_a[1:]:
        if j > avg:
            cnt += 1
    b = cnt/list_a[0] *100
    print(f'{b:.3f}%')