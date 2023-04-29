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

N = iint()
for _ in range(N):
    n = iint()
    res = []
    if n == 1:
        res = [1]
    elif n % 2 == 1:
        res = [-1]
    else:
        for i in range(1,n+1):
            if i % 2 == 0:
                res.append(n-i+1+1)
            else:
                res.append(n-i-1+1)
        # for l in range(n):
        #     for r in range(n):
        #         if l < r and r - l >= 2:
        #             if (sum(res[l:r]) % (r - l)) == 0:
        #                 print(f'bad {res[l:r]} {l} {r}')
    print(' '.join(map(str,res)))