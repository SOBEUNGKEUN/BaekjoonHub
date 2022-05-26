def self(n):
    a = 0
    list_a = list(str(n))
    for i in list_a:
        a = a + int(i)
    return n+a

b_set = set()
for j in range(1,10000):
    b_set.add(self(j))
result = set(range(1,10000)) - b_set
for num in sorted(result):
    print(num)