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
    s = bin(N)[3:]
    score = 1
    running = "1"
    for c in s:
        if c == "1":
            # go right
            running += "1"
        else:
            # go left
            running += "0"
        score += int(running, 2)
    print(score)


main()