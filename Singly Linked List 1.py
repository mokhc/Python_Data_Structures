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
start1a = SLLNode(5)
start1a.next = SLLNode(4)
start1a.next.next = SLLNode(3)
start1a.next.next.next = SLLNode(2)
start1a.next.next.next.next = SLLNode(1)

# loop through the singly linked list
start2a = start1a
while start2a is not None:
    if start2a:
        print(start2a.val)
        start2a = start2a.next
    else:
        break
