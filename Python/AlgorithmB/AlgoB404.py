#엘리스 1-7
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[j])
    return result

name = ["Tom", "Jerry", "Mike", "Tom"]  # 대소문자 유의: 파이썬은 대소문자를 구분함
print(find_same_name(name))

name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))
print()
#엘리스 2-1
def fact(n):
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

print(fact(1))
print(fact(5))
print(fact(10))
print()

#엘리스 6-4
def print_pairs(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            print(a[i], "-", a[j])

name = ["Tom", "Jerry", "Mike"]
print_pairs(name)
print()
name2 = ["Tom", "Jerry", "Mike", "John"]
print_pairs(name2)