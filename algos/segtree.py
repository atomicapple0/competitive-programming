class Node:
	def __init__(self, l, r):
		self.l = l
		self.r = r
		self.x = 0
		self.lchild = None
		self.rchild = None

class SegTree:
	def __init__(self, arr):
		def helper(l, r):
			if l > r:
				return None
			if l == r:
				node = Node(l, r)
				node.x = arr[l]
				return node
			mid = (l + r) // 2
			root = Node(l, r)
			root.lchild = helper(l, mid)
			root.rchild = helper(mid + 1, r)
			root.x = root.lchild.x + root.rchild.x
			return root
		self.root = helper(0, len(arr)-1)
	
	def update(self, i, val):
		def helper(root):
			if root.l == root.r:
				root.x = val
				return
			mid = (root.l + root.r) // 2
			if i <= mid:
				helper(root.lchild)
			else:
				helper(root.rchild)
			root.x = root.lchild.x + root.rchild.x
		helper(self.root)
		return self.root.x
	
	def query(self, l, r):
		def helper(root, l, r):
			if root.l == l and root.r == r:
				return root.x
			mid = (root.l + root.r) // 2
			if r <= mid:
				return helper(root.lchild, l, r)
			elif l >= mid + 1:
				return helper(root.rchild, l, r)
			else:
				return helper(root.lchild, l, mid) + helper(root.rchild, mid+1, r)
		return helper(self.root, l, r)

class SegTree2:
	def __init(self, arr):
		self.n = len(arr)
		self.tree = [0] * 4 * self.n
		self.buildTree(arr, 0, self.n-1, 0)
	
	def buildTree(self, arr, l, r, idx):
		if l == r:
			self.tree[idx] = nums[l]
			return
		mid = (l + r) // 2
		self.buildTree(arr, l, mid, 2*idx+1)
		self.buildTree(arr, mid+1, right, 2*idx+2)
		self.tree[idx] = self.tree[2*idx+1] + self.tree[2*idx+2]
	
	def update(self, l, r, idx, pos, val):
		if pos < l or pos > r:
			return
		if l == r:
			self.tree[idx] = val
		mid = (l + r) // 2
		if pos <= mid:
			self.update(l, mid, 2*index+1, pos, val)
		else:
			self.update(mid+1, r, 2*idx+2, pos, val)
		self.tree[idx] = self.tree[2*idx+1] + self.tree[2*idx+2]
	
	def query(self, l, r, idx, ql, qr):
		if qr < left or ql > right:
			return 0
		if ql <= left and right <= qr:
			return self.tree[idx]
		mid = (l + r) // 2
		return self.query(l, mid, 2*index+1, ql, qr) + self.query(mid+1, r, 2*idx+2, ql, qr)

seg = SegTree([1,2,3,4,5])
print(seg.query(0,4))
print(seg.update(1, 10))
print(seg.query(0,4))
print(seg.query(1,1))