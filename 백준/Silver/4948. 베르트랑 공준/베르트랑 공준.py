import sys
max = 123456
a = [True]*(2*max+1)
a[0], a[1] = False, False

for i in range(2, int((2*max)**0.5)+1):
    if a[i]:
        j=2
        while(i*j)<=(2*max):
            a[i*j] = False
            j += 1
while (n:= int(sys.stdin.readline())) !=0:
    print(a[n+1:(2*n)+1].count(True))