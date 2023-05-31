"""
build binary tree as below


                    1           (level 0)
                /       \
                2       3       (level 1)
            /   \      /    \
            4   5      6    7   (level 2)
        /   \
        8   9                   (level 3)


Sum all the levels as mush as nodes are present.

(level) * (# of nodes at level)
0 * 1  = 0
1 * 2 = 2
2 * 4 = 8
3 * 2 = 6

0 + 2 + 8 + 6 = 16 = Answer
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# https://www.geeksforgeeks.org/print-level-order-traversal-line-line/

my_tree = Node(1) # level 0

my_tree.left = Node(2) # level 1
my_tree.right = Node(3) # level 1

my_tree.left.left = Node(4) # level 2
my_tree.left.right = Node(5) # # level 2

my_tree.right.left = Node(6) # level 2
my_tree.right.right = Node(7) # # level 2

my_tree.left.left.left = Node(8) # level 3
my_tree.left.left.right = Node(9) # # level 3

print(my_tree.value) # 1
print(my_tree.left.value) # 2
print(my_tree.right.value) # 3

print(my_tree.left.left.value) # 4
print(my_tree.left.right.value) # 5

print(my_tree.right.left.value) # 6
print(my_tree.right.right.value) # 7

print(my_tree.left.left.left.value) # 8
print(my_tree.left.left.right.value) # 9

# solution 1 using recursive
# O(n) time complexity | O(h) space complexity
def sumAllNodeDepth(tree, depth=0):
    if tree is None:
        return 0
    return depth + sumAllNodeDepth(tree.left, depth+1) + sumAllNodeDepth(tree.right, depth+1)

print(sumAllNodeDepth(my_tree)) # 16

# solution 2 using iterative
# O(n) time complexity | O(h) space complexity
def sumAllNodeDepth(tree):
    sumOfDepths = 0
    stack = [{"node": tree, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth+1})
        stack.append({"node": node.right, "depth": depth+1})
    return sumOfDepths

print(sumAllNodeDepth(my_tree)) # 16
