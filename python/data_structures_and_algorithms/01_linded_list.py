
class Node:
    def __init__(self, value=None, next=None):
        """

        :param value: str or int
        :param next: Node
        """
        self.value = value
        self.next = next

    def __str__(self):
        return "Node: value: {}, next: {}".format(self.value, self.next)


class SingleLink:
    def __init__(self, maxsize=None):
        self.root = Node()
        self.maxsize = maxsize
        self.len = 0

    def __len__(self):
        return self.len

    def append(self, value):
        node = self.root
        for i in range(self.len):
            node = node.next
        node.next = Node(value)
        self.len += 1

    def append_left(self, value):
        node = Node(value)
        node.next = self.root
        self.root = node
        self.len += 1

    def find(self, value):
        node = self.root
        for i in range(self.len):
            if node.value == value:
                return i
            node = node.next
        return -1

    def remove(self, value):
        node = self.root
        if node.value == value:
            self.root = self.root.next
            self.len -= 1
            return True
        for i in range(self.len-1):
            node_pre = node
            node = node.next
            if node.value == value:
                node_pre.next = node.next
                self.len -= 1
                return True
        return False

