from collections import deque
from collections import defaultdict

def dfs(graph, start):
	visited = set()
	stack = [start]
	while stack:
		u = stack.pop()
		if u in visited:
            continue
        visited.add(u)
        for v in graph[u]:
            stack.append(v)
	return visited

def bfs(graph, start):
	visited = set()
	queue = deque([start])
	while queue:
		u = queue.popleft()
		if u in visited:
            continue
        visited.add(u)
        for v in graph[u]:
            queue.append(v)
	return visited

def dfs_recur(graph, u, visited):
	if u in visited:
		return
	visited.add(u)
	for v in graph[u]:
		dfs_recur(graph, v, visited)

graph = defaultdict(list)
graph[0].append(1)
graph[1].append(2)
graph[3].append(4)
graph[4].append(5)

visited = set()
dfs_recur(graph, 0, visited)
print(visited)