n = int(input())  
list_a = list(map(int, input().split()))
max_score = max(list_a)

list_b = []
for i in list_a :
    list_b.append(i/max_score *100)  
avg = sum(list_b)/n
print(avg)
 