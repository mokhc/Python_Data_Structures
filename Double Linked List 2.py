# Test - Doubly Linked List
# Create a doubly linked list manually
# @mokhc
# 24/11/25

class DLLNode:
    def __init__(t, x, next="", prev=""):
        t.val = x
        t.next = next
        t.prev = prev

# set a doubly linked list
start1a = DLLNode(5)
start1a.next = DLLNode(4)
start1a.next.prev = start1a
start1a.next.next = DLLNode(3)
start1a.next.next.prev = start1a.next
start1a.next.next.next = DLLNode(2)
start1a.next.next.next.prev = start1a.next.next
start1a.next.next.next.next = DLLNode(1)
start1a.next.next.next.next.prev = start1a.next.next.next

# loop through the doubly linked list
start2a = start1a
while start2a is not None and isinstance(start2a, str)==False:
    print("start2a.val :", start2a.val)
    last = start2a
    start2a = start2a.next
    print(isinstance(start2a, str))
    if start2a is not None and isinstance(start2a, str)==False:
        print("start2a.prev.val :", start2a.prev.val)
    else:
        print("last.val:", last.val)