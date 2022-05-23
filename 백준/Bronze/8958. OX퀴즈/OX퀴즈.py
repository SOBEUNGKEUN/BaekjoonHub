n = int(input())

for i in range(n):
    score = 0  
    sum = 0  
    lista = list(input())
   
    for i in lista:
        if i == 'O':
            score += 1 
            sum += score  
        else:
            score = 0
    print(sum)