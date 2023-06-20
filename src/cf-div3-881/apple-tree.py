import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
INF=float('inf')

def iint():
    return int(input().strip())

def iints():
    return [int(x) for x in input().strip().split(" ")]

def log(s):
    if True:
        print(s)

def main():
    T = iint()
    for _ in range(T):
        solve()
visited = []
depth = []
graph = []

from functools import lru_cache

cache = {}
def dfs(u):
    if u in cache:
        return cache[u]
    visited[u] = True
    score = int(u != 1 and len(graph[u]) == 1)
    # q = [u]
    # while len(q) > 0:
    #     u = q.pop(0)
    #     for v in graph[u]:
    #         if depth[v] > depth[u]: 
    #             if not visited[v]:  
    #                 visited[v] = True
    #                 score += int(len(graph[v]) == 1)
    #                 q.append(v)
    for v in graph[u]:
        if depth[v] > depth[u]:
            if not visited[v]:
                score += dfs(v)
    # print(f"dfs({u}) is {score}")
    cache[u] = score
    return score


from collections import deque
def bfs(graph, visited, depth):
    q = deque([1])
    visited[1] = True
    while len(q) > 0:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                q.append(v)
    return depth

def solve():
    global cache
    cache = {}
    global graph, visited, depth
    N = iint()
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = iints()
        graph[a].append(b)
        graph[b].append(a)
    M = iint()
    depth = bfs(graph, [False for _ in range(N+1)], [0 for _ in range(N+1)])
    visited = [False for _ in range(N+1)]
    for _ in range(M):
        a, b = iints()
        scorea = dfs(a)
        scoreb = dfs(b)
        print(scorea * scoreb)


main()