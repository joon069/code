n = int(input())
res = []
for i in range(1, n+1) :
    if i%3 !=0: res.append(i)
print(*res)