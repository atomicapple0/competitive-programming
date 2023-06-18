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

def dec_arr_to_val(arr):
    s = "".join([str(c) for c in arr])
    return int(s)

def val_to_dec_arr(val):
    s = str(val)
    return [int(c) for c in s]

import math
def solve():
    A, B, C, K = iints()

    if C < A or C < B:
        print(-1)
        return

    if C > A + 1 and C > B + 1:
        print(-1)
        return
    CC = [0] * C
    CC[0] = 1
    CCV = dec_arr_to_val(CC)
    AA = [0] * A
    AA[0] = 1
    AAV = dec_arr_to_val(AA)
    BBV = CCV - AAV
    BB = val_to_dec_arr(BBV)

    while CCV < 
    



T = iint()
for _ in range(T):
    solve()