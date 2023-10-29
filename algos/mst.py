from collections import defaultdict
import heapq

def mst(graph):
	n = len(graph)
	totcost = 0
	seen = set()
	edges = []
	verts = [(0, 0, 0)]
	while len(seen) < n:
		cost, prevu, u = heapq.heappop(verts)
		if u in seen:
			continue
		edges.append((cost, prevu, u))
		totcost += cost
		seen.add(u)
		for cost, v in graph[u]:
			if v not in seen:
				heapq.heappush(verts, (cost, u, v))
	return edges[1:]

graph = defaultdict(list)
edges = [
	(100,0,1),
	(50,0,5),
	(49,5,1),
	(1,0,2),
	(1,1,3),
	(1,1,4),
	(6,4,5),
	(1,1,5),
	(3,1,0),
]
for cost, u, v in edges:
	graph[u].append((cost, v))
	graph[v].append((cost, u))
print(mst(graph))