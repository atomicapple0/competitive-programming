import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

def iint():
    return int(input().strip())

def iints():
    return [int(x) for x in input().strip().split(" ")]

def even(a):
    return a % 2 == 0

def winnable_by_first_player(a,b,c):
    num_even = even(a) + even(b) + even(c)
    if num_even == 0:
        return False
    elif num_even == 1:
        return True
    elif num_even == 2:
        return True
    return winnable_by_first_player(a//2,b//2,c//2)

T = iint()
for _ in range(T):
    a, b, c = iints()
    res = winnable_by_first_player(a,b,c)
    if not res:
        print('YES')
    else:
        print('NO')
