n = int(input())
 
list= []
for i in range(n):
    list.append(int(input()))
 
list.sort() # 오름차순 정렬
 
for i in list:
    print(i)