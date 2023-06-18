import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
INF=float('inf')

def iint():
    return int(input().strip())

def iints():
    return [int(x) for x in input().strip().split(" ")]

def log(s):
    if False:
        print(s)

import math
def solve():
    N, K, G = iints()
    if N == 1:
        print(0)
        return
    if K == 0:
        print(0)
        return

    if G % 2 == 0:
        below = G // 2 - 1
    else:
        below = G // 2

    if below <= 0:
        print(0)
        return

    tot = K * G
    lol = min(N-1, tot // below)
    left = tot - lol * below
    saved = lol * below
    r = left % G
    # print(lol, left, saved, r)
    if r >= math.ceil(G / 2):
        saved -= G - r
    else:
        saved += r
    print(saved)        



T = iint()
for _ in range(T):
    solve()