num = int(input())
seat = input()
list(seat)
if len(seat) <= num:
    count_S =0
    count_L = 0
    for i in seat:
        if(i == 'S'):
            count_S+=1
        else:
            count_L+=1

    if 'L' in seat:
        number = count_S+((count_L//2)+1)
    else:
        number = count_S
print(number)