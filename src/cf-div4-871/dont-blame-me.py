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


def bit_set(x, i):
    return x & (1 << i) != 0

T = iint()
from itertools import combinations
for _ in range(1):
    n, k = iints()
    combos = [*combinations(range(6), k)]
    prefix = {lol:0 for lol in combos}
    print(combos, prefix)
    A = iints()
    total = 0
    new_prefix = {}
    for bs in combos:
        flag = True
        for b in range(6):
            if b in bs:
                # should be set
                for 
                if not bit_set(A[b], b):
                    flag = False
        print(bs, flag)
        if not flag:
            new_prefix[bs] = prefix[bs]
        else:
            new_prefix[bs] = 2 * prefix[bs] + 1
    prefix = new_prefix
    print(new_prefix)

    print(sum(new_prefix.values()))

