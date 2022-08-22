import sys

input = sys.stdin.readline


def solve(x: list, num: int) -> int:
    return sorted(x, reverse=True)[num-1]  
if __name__ == '__main__':
    n, k = map(int, input().split())  
    x = list(map(int, input().split()))  

    print(solve(x, k))