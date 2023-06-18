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

M = 1500000
PRIME = [-1 for _ in range(M)]
# PRIME[2] = -1
for i in range(2,M):
    if (PRIME[i] == -1):
        for j in range(i, M, i):
            if PRIME[j] == -1:
                PRIME[j] = i
PRIME[0] = 0
PRIME[1] = 1
PRIME[2] = 2

# print(PRIME[:100])

def smallest_factor(x):
    return PRIME[x]

def solve():
    n, m = iints()
    if m == 1 or n == 1:
        return 'YES'
    if n % m == 0:
        return 'NO'
    if m >= n:
        return 'NO'
    if m >= smallest_factor(n):
        return 'NO'
    return 'YES'


# -------------------------------

T = iint()
for _ in range(T):
    print(solve())
        
