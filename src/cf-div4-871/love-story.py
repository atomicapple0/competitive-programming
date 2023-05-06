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

cf = 'codeforces'

for _ in range(T):
    s = input().strip()
    # wrong = abs(len(s) - len(cf))
    wrong = 0
    for c1,c2 in zip(s,cf):
        if c1 != c2:
            wrong += 1
    print(wrong)