"""
build binary tree as below and find depth first search

                    A
                /   |   \
               B    C    D
            /   \
           E    F
"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

tree = Node("A") # root node

tree.children # []
tree.name # 'A'

tree.addChild("B")
tree.addChild("C")
tree.addChild("D")

# add three child nodes (B,C,D) to root node (A)
tree.children # [<__main__.Node object at 0x000001F1D4A0BA10>, <__main__.Node object at 0x000001F1D4F37290>, <__main__.Node object at 0x000001F1D4F37510>]

# access B node
tree.children[0].name # B
# access child node of B
tree.children[0].children # []
# child nodes are empty for B node

# add child node "E" to B node
tree.children[0].addChild("E")
tree.children[0].children # [<__main__.Node object at 0x000001F1D4F37390>]

# add child node "F" to B node
tree.children[0].addChild("F")
tree.children[0].children # [<__main__.Node object at 0x000001F1D4F37390>, <__main__.Node object at 0x000001F1D4F37350>]

# access E and F node
tree.children[0].children[0].name # E
tree.children[0].children[1].name # F

# call depthFirstSearch recursive function
print(tree.depthFirstSearch([]))
# ['A', 'B', 'E', 'F', 'C', 'D']

# time complexity: O (v+e)
# space complexity: O (v)