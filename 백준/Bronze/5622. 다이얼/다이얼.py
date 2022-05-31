a = input().upper()
b = list(['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'])

c = 0

for i in range(len(a)):
    for j in range(len(b)):
        if(a[i] in b[j]) == True:
            c += (j+3)
print(c)