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
B = [False] * N

for i in range(1,N-1):
    if A[i-1] >= A[i] and A[i] >= A[i+1]:
        B[i] = True

# C = []
# cnt = 0
# for i in range(N):
#     if i != N-1 and B[i]:
#         pass
#     else:
#         cnt+=1
#     C.append(cnt)

# for _ in range(M):
#     l,r = iints()
#     l-=1
#     score = C[r] - C[l]
#     if l == r:
#         print(0)
#         continue
#     if B[r]:
#         score-=1
#     print(score)
    

    

for _ in range(M):
    l,r = iints()
    l-=1
    cnt = 0
    temp = []
    for i in range(l,r):
        if i != r-1 and B[i]:
            continue
        cnt += 1
        temp.append(A[i])
    print(cnt, temp, A[l:r])
    print(cnt)


# print(A,B)