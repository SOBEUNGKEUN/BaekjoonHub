Num = int(input())
while (Num>=1):
    T = int(input())
    a = T//25
    T -= (25*a)
    b = T//10
    T -= (10*b)
    c = T//5
    T -= (5*c)
    d = T//1
    T -= (1*d)
    print(a, b, c, d)
    Num -= 1