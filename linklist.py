__all__ = ["SingleLinkList", "SingleCycleLinkList", "DoubleLinkList"]


class SingleNode(object):
    """单链表节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class DoubleNode(SingleNode):
    """双链表节点"""

    def __init__(self, elem):
        self.prev = None
        super().__init__(elem)


class _LinkedList(object):
    """抽象抽象类，只用于被继承，不能实例化"""

    def __init__(self):
        self.head = None

    def __str__(self, end=" -> "):
        """遍历输出整个链表"""
        cur = self.head
        elems = []
        while cur != None:
            elems.append(str(cur.elem))
            cur = cur.next

        return end.join(elems)

    def is_empty(self):
        """链表是否为空"""
        return self.head == None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def prepend(self, item):
        """链表头部添加元素(头插法)"""
        pass

    def append(self, node):
        """链表尾部添加元素(尾插法)"""
        if self.is_empty():
            self.head = node
            return None

        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = node
        return cur

    def insert(self, position, item, is_double=False):
        """指定位置添加元素
        :param  position 从0开始
        """
        if position <= 0:
            self.add(item)
        elif position > (self.length() - 1):
            self.append(item)
        else:
            if is_double:
                return True

            # 以下单链表和单向循环链表插入逻辑
            pre = self.head
            count = 0
            while count < (position - 1):
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向position-1位置
            node = SingleNode(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        pass

    def contains(self, item):
        """判断节点是否存在"""
        cur = self.head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


class SingleLinkList(_LinkedList):
    """单链表"""

    def prepend(self, item):
        """链表头部添加元素(头插法)"""
        node = SingleNode(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        """链表尾部添加元素(尾插法)"""
        node = SingleNode(item)
        super().append(node)

    def insert(self, position, item):
        """指定位置添加元素
        :param  position 从0开始
        """
        super().insert(position, item)

    def remove(self, item):
        """删除节点"""
        cur = self.head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断此结点是否是头节点
                # 头节点
                if cur == self.head:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


class SingleCycleLinkList(_LinkedList):
    """单向循环链表"""

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        # cur游标，用来移动遍历节点
        cur = self.head
        # count记录数量
        count = 1
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count

    def __str__(self):
        """遍历输出整个链表"""
        if self.is_empty():
            return ""
        cur = self.head
        first, elems = str(cur.elem) + "(head)", []
        while cur.next != self.head:
            elems.append(str(cur.elem))
            cur = cur.next
        # 退出循环，cur指向尾节点，但尾节点的元素未打印
        elems.append(str(cur.elem))
        elems.append(first)
        return " -> ".join(elems)

    def prepend(self, item):
        """链表头部添加元素(头插法)"""
        node = SingleNode(item)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            # 退出循环，cur指向尾节点
            node.next = self.head
            self.head = node
            # cur.next = node
            cur.next = self.head

    def append(self, item):
        """链表尾部添加元素(尾插法)"""
        node = SingleNode(item)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            # node.next = cur.next
            node.next = self.head
            cur.next = node

    def insert(self, position, item):
        """指定位置添加元素
        :param  position 从0开始
        """
        super().insert(position, item)

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return

        cur = self.head
        pre = None

        while cur.next != self.head:
            if cur.elem == item:
                # 先判断此结点是否是头节点
                if cur == self.head:
                    # 头节点的情况
                    # 找尾节点
                    rear = self.head
                    while rear.next != self.head:
                        rear = rear.next
                    self.head = cur.next
                    rear.next = self.head
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            if cur == self.head:
                # 链表只有一个节点
                self.head = None
            else:
                # pre.next = cur.next
                pre.next = self.head

    def contains(self, item):
        """判断节点是否存在"""
        if self.is_empty():
            return False
        cur = self.head
        while cur.next != self.head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            return True
        return False


class DoubleLinkList(_LinkedList):
    """双链表"""

    def __str__(self):
        return super().__str__(" <-> ")

    def prepend(self, item):
        """链表头部添加元素(头插法)"""
        node = DoubleNode(item)
        node.next = self.head
        self.head = node
        node.next.prev = node

    def append(self, item):
        """链表尾部添加元素(尾插法)"""
        node = DoubleNode(item)
        cur = super().append(node)
        if cur:
            node.prev = cur

    def insert(self, position, item):
        """指定位置添加元素
        :param  position 从0开始
        """

        valid = super().insert(position, item, True)
        if valid:
            cur = self.head
            count = 0
            while count < position:
                count += 1
                cur = cur.next
            # 当循环退出后，cur指向position位置
            node = DoubleNode(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除节点"""
        cur = self.head
        while cur != None:
            if cur.elem == item:
                # 先判断此结点是否是头节点
                # 头节点
                if cur == self.head:
                    self.head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个结点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next


if __name__ == '__main__':
    def test_linklist(linklist):
        def print_linklist_status(ll):
            print(
                "is_empty:%s\tlength:%s\t\r\nelements:%s\r\n" % (ll.is_empty(), ll.length(), str(ll)))

        print("-" * 15 + str(linklist.__class__) + "-" * 15)
        print_linklist_status(linklist)

        linklist.append(1)
        linklist.prepend(0)
        print_linklist_status(linklist)

        linklist.insert(1, 10)
        print("contains:%s" % linklist.contains(10))
        print_linklist_status(linklist)

        linklist.remove(10)
        print_linklist_status(linklist)


    test_linklist(SingleLinkList())
    test_linklist(SingleCycleLinkList())
    test_linklist(DoubleLinkList())
