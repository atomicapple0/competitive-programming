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


def solve():
    N = iint()
    A = iints(  )
    from collections import Counter
    c = Counter(A)
    curr = 0
    most = -1
    # import pdb; pdb.set_trace()
    ok = True
    # print(c)
    for k in sorted(c.keys()):
        v = c[k]
        if most == -1:
            most = v
        log(f"{k} {v} {curr} {most}")
        if k == curr and most >= v:
            most = v
            curr = k + 1
        else:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")



T = iint()
for _ in range(T):
    solve()