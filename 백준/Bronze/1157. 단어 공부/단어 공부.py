w = input().lower()
wlist = list(set(w))
a = []

for i in wlist:
    count = w.count(i)
    a.append(count)
if a.count(max(a)) >=2:
    print("?")
else:
    print(wlist[(a.index(max(a)))].upper())