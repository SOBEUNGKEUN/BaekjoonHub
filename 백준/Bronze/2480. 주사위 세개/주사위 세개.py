dice1, dice2, dice3 = input().split()
dice1 = int(dice1)
dice2 = int(dice2)
dice3 = int(dice3)

price = 0



if(dice1 == dice2 == dice3):
    # print("똑같넹")
    price += (dice1*1000)+10000
elif(dice1 == dice2 != dice3):
    price += (dice1 * 100)+1000
elif (dice1 == dice3 != dice2):
    price += (dice1 * 100)+1000
elif (dice2 == dice3 != dice1):
    price += (dice2 * 100)+1000
else:
    if(dice1 > dice2 and dice1 > dice3):
        price += (dice1 * 100)
    elif(dice2 > dice1 and dice2 > dice3):
        price += (dice2 * 100)
    else:
        price += (dice3 * 100)


print(price)