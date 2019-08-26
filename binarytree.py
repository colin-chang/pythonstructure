class Node(object):
    """二叉树节点"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class CompleteBinaryTree(object):
    """完全二叉树"""

    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        """添加节点"""
        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = [self.root]
            # 广度遍历
            while True:
                # 出队一个元素
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    # 如果左右子树都不为空，入队继续遍历
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def breadth_travel(self):
        """广度优先遍历"""
        if self.root == None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.elem, end=' ')

            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)

    def preorder(self, node):
        """先序遍历"""
        if node == None:
            return

        print(node.elem, end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """中序遍历"""
        if node == None:
            return

        self.inorder(node.lchild)
        print(node.elem, end=' ')
        self.inorder(node.rchild)

    def postorder(self, node):
        """后序遍历"""
        if node == None:
            return

        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=' ')


if __name__ == '__main__':
    tree = CompleteBinaryTree()
    for i in range(10):
        tree.add(i)

    tree.breadth_travel()
    print()
    tree.preorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.postorder(tree.root)
