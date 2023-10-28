class UnionFind:
	def __init__(self, n):
		self.parent = [i for i in range(n)]
		self.rank = [0] * n
	
	def find(self, x):
		if self.parent[x] == x:
			return x
		self.parent[x] = self.find(self.parent[x])
		return self.parent[x]
	
	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)
		if x == y:
			return
		if self.rank[x] < self.rank[y]:
			x, y = y, x
		self.parent[y] = x
		if self.rank[x] == self.rank[y]:
			self.rank[x] += 1

	def connected(self, x, y):
		return self.find(x) == self.find(y)

class UnionFindBasic:
	def __init__(self, n):
		self.parents = [i for i in range(n)]
		self.ranks = [0] * n
	
	def find(self, x):
		if x == self.parents[x]:
			return x
		self.parents[x] = self.find(self.parents[x])
		return self.parents[x]

	def union(self, x, y):
		x = self.parents[x]
		y = self.parents[y]
		if x == y:
			return
		self.parents[y] = x
	
	def connected(self, x, y):
		return self.find(x) == self.find(y)