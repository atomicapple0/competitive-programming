def iint():
    return int(input().strip())

def iints():
    return [int(x) for x in input().strip().split(" ")]

def log(s):
    if True:
        print(s)

memo = {}

def h(left_mul, string, target):
    return f'{left_mul}_{string}_{target}'

def find(left_mul, string, target):
    if target < 0:
        return -1
    
    if target > 0 and len(string) > 0 and int(string[0]) > 0 and left_mul > target:
        return -1

    # log(f' [find {string} {target}]')
    if h(left_mul, string, target) in memo:
        return memo[h(left_mul, string, target)]

    if string == '':
        if target == 0:
            return 0
        else:
            return -1
    
    if left_mul * int(string) == target:
        memo[h(left_mul, string, target)] = 0
        return 0

    best = 100000000000000000000
    for i in range(len(string) - 1):
        # a * l1 + f(1, suffix, target - a*l1)
        prefix = string[:i+1]
        suffix = string[i+1:]
        prefix_val = int(prefix)

        ops = find(1, suffix, target - left_mul * prefix_val)
        if ops != -1:
            best = min(best, ops+1)

        ops = find(left_mul * prefix_val, suffix, target)
        if ops != -1:
            best = min(best, ops+1)

    # log(f' <returning {string} {target}  {best}>')
    if best == 100000000000000000000:
        best = -1
    memo[h(left_mul, string, target)] = best
    return best


c = iint()
for _ in range(c):
    string = input().strip()
    target = iint()
    memo = {}
    print(find(1, string, target))
    
# print(memo)