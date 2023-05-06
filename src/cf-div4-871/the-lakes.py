import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
INF=float('inf')

def iint():
    return int(input().strip())

def iints():
    return [int(x) for x in input().strip().split(" ")]

def log(s):
    if True:
        print(s)

from functools import lru_cache


def dfs(i,j):
    if i < 0 or i >= h or j < 0 or j >= w:
        return 0
    if grid[i][j] == 0:
        visited[i][j] = True
        return 0
    if visited[i][j]:
        return 0
    visited[i][j] = True
    score = grid[i][j]
    left = dfs(i,j-1)
    right = dfs(i,j+1)
    up = dfs(i-1,j)
    down = dfs(i+1,j)
    return score + left + right + up + down

T = iint()

for _ in range(T):
    h,w = iints()
    grid = []
    for _ in range(h):
        grid.append(iints())
    # print(grid)
    visited = [[False for _ in range(w)] for _ in range(h)]
    best = 0
    for i in range(h):
        for j in range(w):
            best = max(best, dfs(i,j))
    # print(visited)
    print(best)