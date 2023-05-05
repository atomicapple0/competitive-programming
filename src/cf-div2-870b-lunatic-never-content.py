import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def iint():
    return int(input().strip())

def iints():
    return [int(x) for x in input().strip().split(" ") if x]

def log(s):
    if True:
        print(s)

from math import gcd

def solve():
    N = iint()
    A = iints()

    B = [-1 for _ in range(N//2)]
    B.append(0)
    for i in range(N//2):
        lo = i
        hi = N - i - 1
        B[lo] = max(A[lo],A[hi]) - min(A[lo],A[hi])

    # log(f"A = {A} B = {B}")
    res = gcd(B[0], B[-1])
    for i in range(N//2):
        res = gcd(res, B[i])

    return res

# -------------------------------

T = iint()
for _ in range(T):
    print(solve())
        
