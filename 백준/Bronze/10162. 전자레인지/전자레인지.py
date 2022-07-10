T= int(input())

a = 300
b = 60
c = 10

if(T%c != 0):
    print(-1)
else:
    num_a = T//a
    num_b = (T-(a*num_a))//b
    num_c = (T-(a*num_a)-(b*num_b))//c
    print(num_a, num_b, num_c)