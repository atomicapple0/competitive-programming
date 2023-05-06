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

from functools import lru_cache

@lru_cache(maxsize=None)
def find(a,b):
    if a == b:
        return True
    if a < b:
        return False
    if a % 3 != 0:
        return False

    small = a // 3
    big = a - small
    return find(small,b) or find(big,b)

T = iint()

for _ in range(T):
    a,b = iints()
    if find(a,b):
        print("YES")
    else:
        print("NO")