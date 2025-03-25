n = str(input())
n = int(n,16) #이러면 16진수로 바뀜

for i in range(1,16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')