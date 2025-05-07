print("===================================")
print("max_value")
def find_max(a, n):
    if n == 1:
        return a[0]
    max_of = find_max(a, n - 1)
    if a[n - 1] > max_of:
        return a[n - 1]
    else:
        return max_of
    
value = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(value, len(value)))


print("===================================")
print("gcd")
# Euclidean algorithm to find gcd
def gcd(a ,b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(1, 5))    # 1
print(gcd(3, 6))    # 3
print(gcd(60, 24))  # 12
print(gcd(81, 27))  # 27