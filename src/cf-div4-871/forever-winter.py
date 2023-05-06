import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
INF=float('inf')

def iint():
    return int(input().strip())

def iints():
    return [int(x) for x in input().strip().split(" ")]

def log(s):
    if True:
        print(s)

from collections import Counter

T = iint()
for _ in range(T):
    n, m = iints()
    if m == 2:
        print(1,1)
        continue
    edges = [[] for _ in range(n)]
    for _ in range(m):
        a,b = iints()
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)
    deg = [len(x) for x in edges]
    root = [0 for _ in range(n)]
    interior = [0 for _ in range(n)]
    leaf = [0 for _ in range(n)]

    for i in range(n):
        if deg[i] == 1:
            leaf[i] = 1
    
    for i in range(n):
        is_root = 1
        for j in edges[i]:
            if leaf[j]:
                is_root = 0
        if leaf[i]:
            is_root = 0
        root[i] = is_root

    # print(leaf, root)
    
    if sum(root) == 0:
        print(1, m-1)
        continue
    
    for i in range(n):
        touches_leaf = 0
        touches_root = 0
        for j in edges[i]:
            if leaf[j]:
                touches_leaf = 1
            if root[j]:
                touches_root = 1
        interior[i] = touches_leaf and touches_root
    
    num_interior = sum(interior)
    num_leaf = sum(leaf)
    print(num_interior, num_leaf // num_interior)

    