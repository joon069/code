def find_mindex(a):
  n = len(a)
  min_idx = 0
  for i in range(0, n):
    if a[i] <= a[min_idx]:
      min_idx = i
  return min_idx

def sel(a):
  result = []
  while a:
    min_idx = find_mindex(a)
    result.append(a.pop(min_idx))
  return result
d = [2, 4, 5, 1, 3]
print(sel(d))
