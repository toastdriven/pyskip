try:
    import unittest2 as unittest
except ImportError:
    import unittest

import skiplist


class TestNode(skiplist.SingleNode):
    def __init__(self, *args, **kwargs):
        super(TestNode, self).__init__(*args, **kwargs)

    @property
    def name(self):
        return 'test{0}'.format(self.value)


class SingleNodeTestCase(unittest.TestCase):
    def test_init(self):
        n1 = skiplist.SingleNode()
        self.assertEqual(n1.value, None)
        self.assertEqual(n1.next, None)

        n2 = skiplist.SingleNode(value='whatever')
        self.assertEqual(n2.value, 'whatever')
        self.assertEqual(n2.next, None)

        n3 = skiplist.SingleNode(value='another', next=n2)
        self.assertEqual(n3.value, 'another')
        self.assertEqual(n3.next, n2)


class LinkedListTestCase(unittest.TestCase):
    def setUp(self):
        super(LinkedListTestCase, self).setUp()
        self.ll = skiplist.LinkedList()

        self.head = skiplist.SingleNode(value=0)
        self.first = skiplist.SingleNode(value=2)
        self.second = skiplist.SingleNode(value=5)
        self.third = skiplist.SingleNode(value=6)

        self.ll.insert_first(self.head)
        self.ll.insert_after(self.head, self.first)
        self.ll.insert_after(self.first, self.second)
        self.ll.insert_after(self.second, self.third)

    def test_init(self):
        ll = skiplist.LinkedList()
        self.assertEqual(ll.head, None)
        self.assertEqual(ll._count, 0)

    def test_str(self):
        output = str(self.ll)
        self.assertEqual(output, 'LinkedList: 4 items starting with 0')

    def test_len(self):
        self.assertEqual(len(self.ll), 4)
        self.assertEqual(len(skiplist.LinkedList()), 0)

    def test_insert_first(self):
        ll = skiplist.LinkedList()
        self.assertEqual(ll.head, None)
        self.assertEqual(len(ll), 0)

        world = skiplist.SingleNode(value='world')
        ll.insert_first(world)
        self.assertEqual(ll.head.value, 'world')
        self.assertEqual(ll.head.next, None)
        self.assertEqual(len(ll), 1)

        hello = skiplist.SingleNode(value='Hello')
        ll.insert_first(hello)
        self.assertEqual(ll.head.value, 'Hello')
        self.assertEqual(ll.head.next, world)
        self.assertEqual(len(ll), 2)

    def test_insert_after(self):
        ll = skiplist.LinkedList()

        hello = skiplist.SingleNode(value='Hello')
        world = skiplist.SingleNode(value='world')
        there = skiplist.SingleNode(value='there')
        the_end = skiplist.SingleNode(value='the end')

        ll.insert_first(hello)
        self.assertEqual(ll.head.value, 'Hello')
        self.assertEqual(ll.head.next, None)
        self.assertEqual(len(ll), 1)

        ll.insert_after(hello, world)
        self.assertEqual(ll.head.value, 'Hello')
        self.assertEqual(ll.head.next, world)
        self.assertEqual(len(ll), 2)

        ll.insert_after(hello, there)
        self.assertEqual(ll.head.value, 'Hello')
        self.assertEqual(ll.head.next, there)
        self.assertEqual(ll.head.next.next, world)
        self.assertEqual(len(ll), 3)

        ll.insert_after(world, the_end)
        self.assertEqual(ll.head.value, 'Hello')
        self.assertEqual(ll.head.next, there)
        self.assertEqual(ll.head.next.next, world)
        self.assertEqual(ll.head.next.next.next, the_end)
        self.assertEqual(len(ll), 4)

    def test_remove_first(self):
        self.assertEqual(len(self.ll), 4)

        self.assertEqual(self.ll.remove_first().value, 0)
        self.assertEqual(len(self.ll), 3)

        self.assertEqual(self.ll.remove_first().value, 2)
        self.assertEqual(len(self.ll), 2)

        self.assertEqual(self.ll.remove_first().value, 5)
        self.assertEqual(len(self.ll), 1)

        self.assertEqual(self.ll.remove_first().value, 6)
        self.assertEqual(len(self.ll), 0)

        self.assertEqual(self.ll.remove_first(), None)
        self.assertEqual(len(self.ll), 0)

    def test_remove_after(self):
        self.assertEqual(len(self.ll), 4)

        self.assertEqual(self.ll.remove_after(self.first).value, 5)
        self.assertEqual(len(self.ll), 3)

        self.assertEqual(self.ll.remove_after(self.head).value, 2)
        self.assertEqual(len(self.ll), 2)

        self.assertEqual(self.ll.remove_after(self.head).value, 6)
        self.assertEqual(len(self.ll), 1)

        self.assertEqual(self.ll.remove_after(self.head), None)
        self.assertEqual(len(self.ll), 1)

    def test_iter(self):
        the_list = iter(self.ll)

        self.assertEqual(next(the_list).value, 0)
        self.assertEqual(next(the_list).value, 2)
        self.assertEqual(next(the_list).value, 5)
        self.assertEqual(next(the_list).value, 6)

        with self.assertRaises(StopIteration):
            next(the_list)
