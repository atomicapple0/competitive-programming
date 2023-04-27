import sys
sys.setrecursionlimit(1000000)
from itertools import permutations

input = sys.stdin.readline

def iint():
    return int(input().strip())

def iints():
    return [int(x) for x in input().strip().split(" ")]

def log(s):
    if False:
        print(s)

T = iint()

memo = {}

def sort_tuple(a,b,c):
    return tuple(sorted([a,b,c]))

def winnable_by_first_player(l):
    if l in memo:
        return memo[l]
    a,b,c = l

    # if a == 1 and b == 1 and c == 1:
    #     memo[l] = False
    #     return False
    if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
        memo[l] = False
        return False
    if a + b + c > 1000:
        return True
    # if a % 2 == 1 and b % 2 == 1 and c % 2 == 0:
    #     memo[l] = True
    #     return True

    for i,j,k in permutations([0,1,2]):
        # keep i, remove j, split k
        for small in range(1,l[k]//2+1):
            big = l[k] - small

            if not winnable_by_first_player(sort_tuple(l[i],small,big)):
                memo[l] = True
                return True
    
    memo[l] = False
    return False
                

for _ in range(T):
    a, b, c = iints()
    res = winnable_by_first_player(sort_tuple(a,b,c))
    if not res:
        print('YES')
    else:
        print('NO')
