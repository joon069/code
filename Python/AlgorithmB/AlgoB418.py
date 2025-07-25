# 418. Fibonacci Number
print("fibpnacci")
def fibo(n):    
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(7))
print(fibo(10))


print("===================================")

print("hanoi")
def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        return print(f"{from_pos} -> {to_pos}")
    
    # 원반 n - 1개를 aux_pos로 이동(to_pos를 보조 기둥으로)
    hanoi(n-1, from_pos, aux_pos, to_pos)
    # 가장 큰 원반을 목적지로 이동
    print(f"{from_pos} -> {to_pos}")
    # aux_pos에 있는 원반 n-1개를 목적지로 이동(from_pos를 보조 기둥으로)
    hanoi(n-1, aux_pos, to_pos, from_pos)

print("n = 1")
hanoi(1, 1, 3, 2)  # 원반 한 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)
print("n = 2")
hanoi(2, 1, 3, 2)  # 원반 두 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)
print("n = 3")
hanoi(3, 1, 3, 2) # 원반 세 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)