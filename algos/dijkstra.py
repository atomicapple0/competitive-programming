import heapq
from collections import defaultdict

def dijkstra(graph, start):
	h = [(0, start)]
	n = len(graph)
	best = [1e10] * n
	best[start] = 0
	expanded = set()
	for _ in range(n):
		(cost, u) = heapq.heappop(h)
		if u in expanded:
			continue
		for (weight, v) in graph[u]:
			if best[v] < cost + weight:
				continue
			best[v] = min(best[v], cost + weight)
			heapq.heappush(h, (cost + weight, v))
	return best

graph = defaultdict(list)
graph[0].append((100, 1))
graph[0].append((50, 5))
graph[5].append((49, 1))
graph[0].append((1, 2))
graph[2].append((1, 3))
graph[3].append((1, 4))
graph[4].append((6, 5))
graph[5].append((1, 1))
graph[1].append((3,0))
print(dijkstra(graph, 0))