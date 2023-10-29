def bsearch(arr, l, h, x):
	if h < l:
		return -1
	mid = (l + h) // 2
	if arr[mid] == x:
		return mid
	elif arr[mid] > x:
		return bsearch(arr, l, mid-1, x)
	else:
		return bsearch(arr, mid+1, h, x)

def bsearch2(arr, x):
	l = 0
	h = len(arr) - 1
	mid = 0
	while l <= h:
		mid = (l + h) // 2
		if arr[mid] < x:
			l = mid + 1
		elif arr[mid] > x:
			h = mid - 1
		else:
			return mid
	return -1

# Test array
arr = [ 2, 3, 4, 10, 10, 10, 40 ]
x = 10
 
# Function call
print(bsearch(arr, 0, len(arr)-1, x))
print(bsearch2(arr, x))

from bisect import bisect_left, bisect_right

# each elt in prefix is < x
print(bisect_left(arr, x))
# each elt in prefix is <= x
print(bisect_right(arr, x))