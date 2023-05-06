import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
INF=float('inf')

def iint():
    return int(input().strip())

def iints():
    return [int(x) for x in input().strip().split(" ")]

def log(s):
    if True:
        print(s)

def sum_from_one_to_n_sq(n):
    return n * (n + 1) * (2 * n + 1) // 6
def sum_sq(a,b):
    return sum_from_one_to_n_sq(b) - sum_from_one_to_n_sq(a-1)

arr1 = []
arr = []
i = 1
up = 1
while i < 2048*20478+121:
    arr1.append(i)
    arr.append(i*i)
    i += up
    up += 1


def rc(n):
    for i,x in enumerate(arr1):
        if x > n:
            return i-1, n - arr1[i-1]

def idx(r,c):
    return arr1[r] + c
# print(arr,arr1)
T = iint()

for _ in range(T):
    x = iint()
    # print(x)
    row, col = rc(x)
    left = col
    right = col+1
    acc = 0
    while row >= 0:
        ll = max(left, 0)
        rr = min(right, row+1)
        sumss = sum_sq(idx(row,ll), idx(row,rr-1))
        # print(f"{x} {row} {col} |{ll} {rr}| {sumss} ||{idx(row,ll)} {idx(row,rr-1)}|| {left} {right}")
        acc += sumss
        row -= 1
        left -= 1
        # right += 1
    print(acc)