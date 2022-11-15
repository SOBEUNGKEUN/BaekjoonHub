def merge_sort(list):
    n = len(list)

    if n <= 1:
        return list
    mid = (n+1)//2  
    g1 = merge_sort(list[:mid]) 
    g2 = merge_sort(list[mid:]) 
    result, i, j =[], 0, 0

    while i < len(g1) and j < len(g2):  
        if g1[i] < g2[j]: 
            result.append(g1[i])
            res.append(g1[i])
            i += 1
        else:
            result.append(g2[j])
            res.append(g2[j])
            j+=1
            
    result.extend(g1[i:])
    result.extend(g2[j:])

    res.extend(g1[i:])
    res.extend(g2[j:])

    return result

N, M = map(int,input().split())
arr = list(map(int,input().split()))
res = []

merge_sort(arr)
print(res[M-1]) if len(res) >= M else print(-1)