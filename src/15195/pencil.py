def iint():
    return int(input().strip())

def iints():
    return [int(x) for x in input().strip().split(" ")]

n = iint()
options = [iints(), iints(), iints()]

best = 10000000000000000000000000000000000
for x,y in options:
    packs_to_buy = n // x + (0 if n % x == 0 else 1)
    best = min(best, packs_to_buy * y)
print(best)
