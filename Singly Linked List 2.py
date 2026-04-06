# Test - Singly Linked List
# Create a singly linked list manually
# @mokhc
# 15/11/25

# class SLLNode
class SLLNode:
    def __init__(s, input, next=''):
        s.val = input
        s.next = next
    
# set up singly linked list
start1b = SLLNode(5, SLLNode(4, SLLNode(3, SLLNode(2, SLLNode(1)))))

# loop through the singly linked list
start2b = start1b
while start2b is not None:
    if start2b:
        print(start2b.val)
        start2b = start2b.next
    else:
        break
