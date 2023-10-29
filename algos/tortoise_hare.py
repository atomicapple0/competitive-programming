def tortoise_hare(head):
	slow = head
	fast = head
	while fast.next and fast.next.next:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			break
	if fast.next is None or fast.next.next is None:
		return
	# find node of start of cycle
	while head != slow:
		slow = slow.next
		head = head.next
	return head