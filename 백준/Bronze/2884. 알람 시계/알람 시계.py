h, m = input().split()
h = int(h)
m = int(m)

m = m-45
if(m>0):
     print(h,m)
elif(m <0):
    m =60+m
    if(h == 0):
        h = 24
        h = h-1
        print(h,m)
    elif (0<h<=24) :
        h = h-1
        print(h,m)
elif(m == 0):
    print(h, m)
