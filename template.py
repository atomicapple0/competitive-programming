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