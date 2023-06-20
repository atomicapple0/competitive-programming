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

def main():
    T = iint()
    for _ in range(T):
        solve()

def solve():
    N = iint()
    A = iints()
    A = sorted(A)
    score = 0
    for i in range(len(A) // 2):
        score += abs(A[i] - A[len(A) - i - 1])
    print(score)

main()