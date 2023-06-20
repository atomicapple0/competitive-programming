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

def main():
    T = iint()
    for _ in range(T):
        solve()

def solve():
    N = iint()
    A = iints()
    score = sum([abs(a) for a in A])
    looking = False
    looked_at = 0
    for a in A:
        if a < 0:
            if not looking:
                looking = True
                looked_at += 1
        elif a > 0:
            looking = False
    print(f"{score} {looked_at}")


main()