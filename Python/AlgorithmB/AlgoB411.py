def find_max(a, n):
    if n == 1:
        return a[0]
    max_of_rest = find_max(a, n - 1)
    if a[n - 1] > max_of_rest:
        return a[n - 1]
    else:
        return max_of_rest
    
value = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(value, len(value)))