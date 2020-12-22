class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)
    
def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val.strip() == 'null' else TreeNode(int(val.strip()))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = [root]
        while self.stack[-1].left:
            self.stack.append(self.stack[-1].left)

    def next(self) -> int:
        node = self.stack.pop()

        if node.right:
            self.stack.append(node.right)
            while self.stack[-1].left:
                self.stack.append(self.stack[-1].left)

        return node.val

    def hasNext(self) -> bool:
        if not self.stack: return False
        return True
        

if __name__ == "__main__":

    root = deserialize('[7, 3, 15, null, null, 9, 20]')
    iter = BSTIterator(root)
    iter.next()
    iter.next()
    iter.hasNext()
    iter.next()
    iter.hasNext()
    iter.next()
    iter.hasNext()
    iter.next()
    iter.hasNext()
