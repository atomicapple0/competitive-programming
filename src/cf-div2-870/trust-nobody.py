import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def iint():
    return int(input().strip())

def iints():
    return [int(x) for x in input().strip().split(" ")]

def log(s):
    if False:
        print(s)

T = iint()
for _ in range(T):
    N = iint()
    A = sorted(iints())
    
    j = len(A) - 1
    flag = False
    for idx in range(len(A)):
        log(f"{A} idx: {idx}, A[idx]: {A[idx]}")
        score = len(A)-(idx+1) 
        # lets assume this guy is telling truth
        # A[:idx] is truth so score >= A[idx]
        # A[idx+1:] is lie so score < A[idx+1]
        if score >= A[idx]:
            if idx == len(A) - 1 or score < A[idx+1]:
                print(score)
                flag = True
                break
        # lets assume this guy is telling lie
        # A[:idx-1] is truth so score >= A[idx-1]
        # A[idx:] is lie so score < A[idx]
        if score + 1 < A[idx]:
            if idx == 0 or score >= A[idx-1]:
                num_liar = score + 1
                this_number_is_lie = A[idx]
                idx -= 1
                while idx >= 0 and A[idx] == this_number_is_lie:
                    num_liar -= 1
                    idx -= 1
                print(num_liar)
                flag = False
                break
    if not flag:
        print(-1)
        

# print(A,B)