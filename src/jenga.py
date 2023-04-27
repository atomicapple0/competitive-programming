import sys
from collections import defaultdict


N = int(input())
J = defaultdict(int)
for i in range(1,19):
    for l in ['A', 'B', 'C']:
        J[str(i)+l] = 1

for i in range(N):
    a,b = input().strip().split(" ")
    pa = a[:-1]
    pb = b[:-1]
    J[a] = 0
    if J[pa+'A'] + J[pa+'B'] + J[pa+'C'] <= 1:
        if not J[pa+'B']:
            print(f"The tower collapses after removing {a}")
            sys.exit()
    J[b] = 1
    # if J[pb+'A'] + J[pb+'B'] + J[pb+'C'] == 1:
    #     if not J[pb+'B']:
    #         print(f"The tower collapses after placing {b}")
    #         sys.exit()
print(f"The tower never collapses")
