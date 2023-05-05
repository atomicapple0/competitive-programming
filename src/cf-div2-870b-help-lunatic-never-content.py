import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def iint():
    return int(input().strip())

def iints():
    return [int(x) for x in input().strip().split(" ") if x]

def log(s):
    if False:
        print(s)

A = [2 * 3 * 17, 3 * 17, 3 * 11]
M = 3

for i in range(len(A) // 2):
    if A[i] % M != A[len(A) - 1 - i] % M:
        print(f"NO @ {i} with {A[i]} and {A[len(A) - 1 - i]}")
print("done")