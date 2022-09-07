import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
cnt = 0
s = set()
check = set()
for i in range(n):
    s.add(input().rstrip()) 

for j in range(m):
    word = input().rstrip()
    if word in s: 
        cnt += 1
print(cnt)