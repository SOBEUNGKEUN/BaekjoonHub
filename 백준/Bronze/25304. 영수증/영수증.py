import sys

input = sys.stdin.readline

def solve(target, datas) -> str:
    return 'Yes' if target == sum([x[0] * x[1] for x in datas]) else 'No'

if __name__ == '__main__':
    x = int(input())  # x: 
    n = int(input())  # n: 
    datas = [list(map(int, input().split())) for _ in range(n)]

    print(solve(x, datas))