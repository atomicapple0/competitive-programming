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
    n = iint()
    best_left = 1e7
    best_right = 1e7
    best_both = 1e7
    for _ in range(n):
        line = input().strip().split(" ")
        t = int(line[0])
        s = line[1].strip()
        if s == '11':
            best_both = min(best_both, t)
        elif s == '01':
            best_left = min(best_left, t)
        elif s == '10':
            best_right = min(best_right, t)
    
    if best_both == 1e7 and (best_left == 1e7 or best_right == 1e7):
        print(-1)
    else:
        print(min(best_both, best_left + best_right))