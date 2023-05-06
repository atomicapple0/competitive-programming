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


T = iint()

for _ in range(T):
    _ = iint()
    A = iints()
    best = 0
    curr = 0
    for a in A:
        # print(f"{A} {a} {best} {curr}")
        if a == 0:
            curr += 1
        else:
            curr = 0
        best = max(best, curr)
    print(best)