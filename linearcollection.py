__all__ = ["Stack", "Queue", "Deque"]


class _LinearCollection(object):
    def __init__(self):
        self.items = []

    def count(self):
        """返回集合元素个数"""
        return len(self.items)


class Stack(_LinearCollection):
    """栈"""

    def push(self, item):
        """压栈元素"""
        self.items.append(item)

    def pop(self):
        """出栈元素"""
        return self.items.pop()

    def peek(self, position: int = 0):
        """查看栈顶元素"""
        position = (position if position < self.count() else self.count() - 1) if position >= 0 else 0
        return self.items[self.count() - 1 - position]


class Queue(_LinearCollection):
    """队列"""

    def enqueue(self, item):
        """入队元素"""
        self.items.insert(0, item)

    def dequeue(self):
        """出队元素"""
        return self.items.pop()

    def peek(self, position: int):
        "查看队内元素而不出栈"
        position = (position if position < self.count() else self.count() - 1) if position >= 0 else 0
        return self.items[position]


class Deque(_LinearCollection):
    """双端队列"""

    def enqueue_front(self, item):
        """在队头添加元素"""
        self.items.insert(0, item)

    def enqueue_rear(self, item):
        """在队尾添加元素"""
        self.items.append(item)

    def dequeue_front(self):
        """从队头删除元素"""
        return self.items.pop(0)

    def dequeue_rear(self):
        """从队尾删除元素"""
        return self.items.pop()


if __name__ == '__main__':
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    print(stack.peek(1))
    print(stack.count())
    print(stack.pop())

    queue = Queue()
    queue.enqueue("hello")
    queue.enqueue("world")
    print(queue.peek(1))
    print(queue.count())
    print(queue.dequeue())

    deque = Deque()
    deque.enqueue_front(1)
    deque.enqueue_front(2)
    deque.enqueue_rear(3)
    deque.enqueue_rear(4)
    print(deque.count())
    print(deque.dequeue_front())
    print(deque.dequeue_front())
    print(deque.dequeue_rear())
    print(deque.dequeue_rear())
