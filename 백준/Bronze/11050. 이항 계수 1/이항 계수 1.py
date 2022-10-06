from sys import stdin

def factor(n):
    if n == 0:
        return 1
    return n * factor(n-1)

n, k = map(int, stdin.readline().split())
print(factor(n) // (factor(k) * factor(n - k)))