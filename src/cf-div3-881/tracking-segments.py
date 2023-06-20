import sys
sys.setrecursionlimit(10**5)
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

class SegmentTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        self.size = n
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            k >>= 1
            self.tree[k] = self.segfunc(self.tree[2*k], self.tree[2*k+1])

    def query(self, l, r):
        if r==self.size:
            r = self.num

        res = self.ide_ele

        l += self.num
        r += self.num
        right = []
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                right.append(self.tree[r-1])
            l >>= 1
            r >>= 1

        for e in right[::-1]:
            res = self.segfunc(res,e)
        return res

    def bisect_l(self,l,r,x):
        l += self.num
        r += self.num
        Lmin = -1
        Rmin = -1
        while l<r:
            if l & 1:
                if self.tree[l] <= x and Lmin==-1:
                    Lmin = l
                l += 1
            if r & 1:
                if self.tree[r-1] <=x:
                    Rmin = r-1
            l >>= 1
            r >>= 1

        if Lmin != -1:
            pos = Lmin
            while pos<self.num:
                if self.tree[2 * pos] <=x:
                    pos = 2 * pos
                else:
                    pos = 2 * pos +1
            return pos-self.num
        elif Rmin != -1:
            pos = Rmin
            while pos<self.num:
                if self.tree[2 * pos] <=x:
                    pos = 2 * pos
                else:
                    pos = 2 * pos +1
            return pos-self.num
        else:
            return -1



import bisect
def solve():
    # N, M = iints()
    # segs = []
    # for _ in range(M):
    #     l, r = iints()
    #     segs.append((l, r))
    # Q = iint()
    # qs = []
    # ans = -1
    # for i in range(Q):
    #     q = iint()
    #     bisect.insort(qs, q)
    #     for l,r in segs:
    #         lidx = bisect.bisect_left(qs, l)
    #         ridx = bisect.bisect_right(qs, r)
    #         num_ones = ridx - lidx
    #         tot_elems = r - l + 1
    #         # print(qs, (l, r), (lidx, ridx), num_ones, tot_elems)
    #         if num_ones > tot_elems // 2:
    #             if ans == -1:
    #                 ans = i+1
    # print(ans)
    N, M = iints()
    segments = []
    for _ in range(M):
        l,r = iints()
        segments.append((l-1, r))
    Q = iint()
    qs = []
    for _ in range(Q):
        q = iint()
        qs.append(q-1)

    def ok(x):
        seg = SegmentTree([0]*N, lambda x,y: x+y, 0)
        for q in qs[:x]:
            seg.update(q, 1)
        for l,r in segments:
            num_ones = seg.query(l, r)
            # print(qs[:x], (l, r), num_ones)
            tot_elems = r - l
            # print(qs, (l, r), (lidx, ridx), num_ones, tot_elems)
            if num_ones > tot_elems // 2:
                return True
        return False

    lo = 0
    hi = Q

    while hi-lo > 1:
        mid = (lo+hi)//2
        if ok(mid):
            hi = mid
        else:
            lo = mid

    if not ok(hi):
        print(-1)
    else:
        print(hi)


main()