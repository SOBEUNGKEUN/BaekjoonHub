import sys
num = int(input())
def han(num):
    count=0;
    for i in range(1, num+1):
        n_list = list(map(int, str(i)))
        if i < 100:
            count += 1
        elif n_list[0] - n_list[1] == n_list[1] - n_list[2]:
            count += 1
    return count

print(han(num))