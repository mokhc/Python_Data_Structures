# Test - Doubly Linked List
# Create a doubly linked list manually
# @mokhc
# 24/11/25

class DLLNode:
    def __init__(s, x, next="", prev=""):
        s.val = x
        s.next = next
        s.prev = prev
        
# set a doubly linked list

start1a = DLLNode(5, DLLNode(4, DLLNode(3, DLLNode(2, DLLNode(1, None, DLLNode(2)), DLLNode(3)), DLLNode(4)), DLLNode(5)))

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
