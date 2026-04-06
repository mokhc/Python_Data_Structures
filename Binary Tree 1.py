# Test - Binary Tree
# Create a binary tree manually
# @mokhc
# 11/11/25
from print_btree import print_btree

# class BNode
class BNode():
    def __init__(self, v, l='', r=''):
        self.val = v
        self.left = l
        self.right = r

# implementation 1
t1 = BNode(1)
t1.left = BNode(2, BNode(4, BNode(8)), BNode(5))
t1.right = BNode(3, BNode(6))
print_btree(t1)
"""
   ___1___
   |     |
 __2__  _3
 |   |  |
_4   5  6
|
8
"""
# reference :
# https://weread.qq.com/web/reader/79c32c30727ecf0e79c7ef2k44f328c023e44f683a8420b
