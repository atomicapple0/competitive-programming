# broken

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def iint():
    return int(input().strip())

def iints():
    return [int(x) for x in input().strip().split(" ")]

def log(s):
    if True:
        print(s)

N, M = iints()

A = iints()

DP = [(0,0,0) for _ in range(N)]
    
for i in range(N):
    best = 0
    for di in [-3,-2,-1]:
        j = i + di
        if j >= 0:
            length, prev_prev, prev = DP[j]
        else:
            length, prev_prev, prev = 0, 0, 0
        if prev_prev >= prev and prev >= A[i]:
            DP[i] = (length,prev_prev,prev)
        else:
            DP[i] = (length+1,prev,A[i])

print(DP)

for _ in range(M):
    l,r = iints()
    l-=1
    r-=1
    # print(l,r)
    print(DP[r][0] - DP[l][0] + 1)


# print(A,B)