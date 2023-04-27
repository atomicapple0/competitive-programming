def iint():
    return int(input().strip())

def iints():
    return [int(x) for x in input().strip().split(" ")]

def log(s):
    if False:
        print(s)

memo = {}

def update_best(best, ops):
    if ops != -1:
        ops = ops + 1
    if best == -1:
        return ops
    if ops == -1:
        return best
    return min(best, ops)

def h(string, target, can_use_star):
    return f'{string}_{target}' + ('+' if can_use_star else '')

def find(string, target, can_use_add):
    log(f' [find {string} {target}]')
    if h(string, target, can_use_add) in memo:
        return memo[h(string, target, can_use_add)]
    
    if int(string) == target:
        memo[h(string, target, can_use_add)] = 0
        return 0

    best = -1
    for i in range(len(string) - 1):
        prefix = string[:i+1]
        suffix = string[i+1:]
        log(f'   {prefix} {suffix}')

        prefix_val = int(prefix)
        # try adding
        if can_use_add:
            suffix_target_val = target - prefix_val
            ops = find(suffix, suffix_target_val, can_use_add=True)
            best = update_best(best,ops)
        # try dividing
        if prefix_val != 0 and target % prefix_val == 0:
            suffix_target_val = target // prefix_val
            ops = find(suffix, suffix_target_val, can_use_add=True)
            best = update_best(best,ops)
        if prefix_val == 0 and target == 0:
            best = 1
    
    log(f' <returning {string} {target}  {best}>')
    memo[h(string, target, can_use_add)] = best
    return best


c = iint()
for _ in range(c):
    string = input().strip()
    target = iint()
    memo = {}
    # log(f' [s {string} t {target}]')
    print(find(string, target, True))
    # print(memo)
    
    