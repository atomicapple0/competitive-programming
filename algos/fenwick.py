class Fenwick:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
    
    def get_sum(self, idx):
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & -idx
        return s
    
    def get_sum_range(self, l, r):
        return self.get_sum(r) - self.get_sum(l - 1)
    
    def add_val(self, idx, val):
        while idx < len(self.tree):
            self.tree[idx] += val
            idx += idx & -idx

fen = Fenwick(10)
arr = [1,10,100,1000,10000,100000,1000000]
for i, x in enumerate(arr):
    fen.add_val(i+1, x)
print(fen.tree)