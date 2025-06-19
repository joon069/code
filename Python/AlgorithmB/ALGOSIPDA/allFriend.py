def bfs(g, s):
  q = [s]
  d = set(s)

  while q:
    now = q.pop(0)
    print(now)
    for i in g[now]:
      if i not in d:
        d.add(i)
        q.append(i)


fr_info = {           
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

bfs(fr_info, 'Summer')
print()
bfs(fr_info, 'Jerry')