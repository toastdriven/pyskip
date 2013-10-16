import random


__author__ = 'Daniel Lindsley'
__license__ = 'BSD'
__version__ = (0, 5, 0)


class InsertError(Exception):
    pass


class SingleNode(object):
    """
    A simple, singly linked list node.
    """
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return "{0}: {1}".format(self.__class__.__name__, self.value)

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ne__(self, other):
        return self.value != other.value


class LinkedList(object):
    """
    A simple linked list.
    """
    def __init__(self):
        self.head = None

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
        count = 0

        for node in self:
            count += 1

        return count

    def __getitem__(self, offset):
        if offset < 0:
            raise IndexError(
                "Can't do negative offsets with a singly linked list."
            )

        for i, node in enumerate(self):
            if offset == i:
                return node

        raise IndexError("Index '{0}' out of range.".format(offset))

    def __contains__(self, value):
        for node in self:
            if node.value == value:
                # We found it! Yay! Bail early.
                return True

        return False

    def insert_first(self, insert_node):
        """
        Inserts the new node at the beginning of the list.
        """
        insert_node.next = self.head
        self.head = insert_node
        return insert_node

    def insert_after(self, existing_node, insert_node):
        """
        Inserts the new node after a given node in the list.
        """
        insert_node.next = existing_node.next
        existing_node.next = insert_node
        return insert_node

    def remove_first(self):
        """
        Removes the first node (if any) in the list.
        """
        if self.head is None:
            return None

        old_head = self.head
        self.head = self.head.next
        return old_head

    def remove_after(self, existing_node):
        """
        Removes the node (if any) that follows the provided node in the list.
        """
        if existing_node.next is None:
            return None

        old_next = existing_node.next
        existing_node.next = existing_node.next.next
        return old_next


class SortedLinkedList(LinkedList):
    """
    A linked list that maintains the correct sort order.
    """
    def __contains__(self, value):
        # We can be more efficient here, since we know we're sorted.
        for node in self:
            if node.value == value:
                # We found it! Yay! Bail early.
                return True

            if node.value > value:
                # We've exceeded the value & we didn't already come across it.
                # Must not be here. Bail.
                return False

        return False

    def insert_after(self, existing_node, new_node):
        if not existing_node <= new_node:
            raise InsertError("Invalid placement for the new node.")

        if existing_node.next and not new_node <= existing_node.next:
            raise InsertError("Invalid placement for the new node.")

        return super(SortedLinkedList, self).insert_after(
            existing_node,
            new_node
        )

    def insert_first(self, new_node):
        if self.head and not new_node <= self.head:
            raise InsertError("Invalid placement for the new node.")

        return super(SortedLinkedList, self).insert_first(new_node)

    def insert(self, new_node):
        if not self.head or new_node < self.head:
            self.insert_first(new_node)
            return

        previous = self.head

        for node in self:
            if previous <= new_node <= node:
                self.insert_after(previous, new_node)
                return

            previous = node

        return self.insert_after(previous, new_node)

    def remove(self, remove_node):
        previous = self.head

        for node in self:
            if node == remove_node:
                return self.remove_after(previous)

            previous = node

        return None


class SkiplistNode(SingleNode):
    def __init__(self, value=None, next=None, down=None):
        super(SkiplistNode, self).__init__(value=value, next=next)
        self.down = down


class Skiplist(object):
    """
    Implements a basic skiplist.

    A skiplist provides a quickly searchable structure (like a balanced binary
    tree) that also updates fairly cheaply (no nasty rebalancing acts).

    In other words, it's awesome.

    See http://en.wikipedia.org/wiki/Skip_list for more information.
    """
    def __init__(self, list_class=SortedLinkedList, max_layers=32):
        self.list_class = list_class
        self.max_layers = max_layers
        self.layers = [
            self.list_class()
        ]

    def __str__(self):
        return 'Skiplist: {0} items'.format(len(self.layers[-1]))

    def __len__(self):
        return len(self.layers[-1])

    def __contains__(self, value):
        return self.find(value) is not None

    def __iter__(self):
        return iter(self.layers[-1])

    def generate_height(self):
        """
        Generates a random height (between ``2`` & ``self.max_layers``) to fill
        in.
        """
        return random.randint(2, self.max_layers)

    def find(self, value):
        current = self.layers[0].head

        while True:
            if current is None:
                # We've exhausted all options. Bail out.
                return None

            if current.value == value:
                # We found it! Bail out.
                return current

            if current.next and current.next.value <= value:
                # The next node in the current layer might match.
                current = current.next
                continue
            else:
                # Either the next node is too high or we reached the end of that
                # layer. Attempt to descend.
                if current.down is not None:
                    current = current.down
                    continue
                else:
                    return None

    def insert(self, value):
        pass

    def remove(self, value):
        pass
