__author__ = 'Daniel Lindsley'
__license__ = 'BSD'
__version__ = (0, 1, 0)


class SingleNode(object):
    """
    A simple, singly linked list node.
    """
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def insert_after(self, new_node):
        """
        Adds a new node after the current one.

        Returns True on success (which is always).
        """
        new_node.next = self.next
        self.next = new_node
        return True

    def remove_after(self):
        """
        Removes a new node after the current one.
        """
        if self.next is None:
            return None

        old_next = self.next
        self.next = self.next.next
        return old_next


class LinkedList(object):
    """
    A simple linked list.
    """
    def __init__(self):
        self.head = None
        self._count = 0

    def __str__(self):
        return 'LinkedList: {0} items starting with {1}'.format(
            len(self),
            self.head.value
        )

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration()

        cur = self.current
        self.current = cur.next
        return cur

    def __len__(self):
        return self._count

    def insert_first(self, insert_node):
        """
        Inserts the new node at the beginning of the list.
        """
        insert_node.next = self.head
        self.head = insert_node
        self._count += 1

    def insert_after(self, existing_node, insert_node):
        """
        Inserts the new node after a given node in the list.
        """
        existing_node.insert_after(insert_node)
        self._count += 1

    def remove_first(self):
        """
        Removes the first node (if any) in the list.
        """
        if self.head is None:
            return None

        old_head = self.head
        self.head = self.head.next
        self._count -= 1
        return old_head

    def remove_after(self, existing_node):
        """
        Removes the node (if any) that follows the provided node in the list.
        """
        old_node = existing_node.remove_after()

        if old_node is not None:
            self._count -= 1

        return old_node


class Skiplist(object):
    def __init__(self, ):
        self.layers = []
