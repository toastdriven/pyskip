import random
import time

import pyskip


MAX_LOAD = 1000


def load_skiplist():
    skip = pyskip.Skiplist()

    for i in range(MAX_LOAD):
        print(i, end='\r')
        skip.insert(i)

    print()
    return skip


def load_sorted_list():
    the_list = pyskip.SortedLinkedList()

    for i in range(MAX_LOAD):
        the_list.insert(pyskip.SingleNode(value=i))

    return the_list


def contains_skiplist(skip, randoms):
    for rand in randoms:
        assert rand in skip


def contains_sorted_list(the_list, randoms):
    for rand in randoms:
        try:
            assert rand in the_list
        except AssertionError:
            print("{0} not in the list?".format(rand))


def inserts_skiplist(skip, randoms):
    for rand in randoms:
        skip.insert(rand)


def inserts_sorted_list(the_list, randoms):
    for rand in randoms:
        the_list.insert(pyskip.SingleNode(value=rand))


def run():
    start = time.time()
    skip = load_skiplist()
    end = time.time()
    print("Skiplist loaded in {0} seconds.".format(end - start))

    start = time.time()
    the_list = load_sorted_list()
    end = time.time()
    print("Sorted Linked List loaded in {0} seconds.".format(end - start))

    print()

    randoms = [random.randint(0, MAX_LOAD - 1) for i in range(20)]

    start = time.time()
    contains_skiplist(skip, randoms)
    end = time.time()
    print("Skiplist checked contains in {0} seconds.".format(end - start))

    start = time.time()
    contains_sorted_list(the_list, randoms)
    end = time.time()
    print("Sorted Linked List checked contains in {0} seconds.".format(end - start))

    print()

    randoms = [random.randint(0, MAX_LOAD - 1) for i in range(50)]

    start = time.time()
    skip = inserts_skiplist(skip, randoms)
    end = time.time()
    print("Skiplist inserted 50 new values in {0} seconds.".format(end - start))

    start = time.time()
    skip = inserts_sorted_list(the_list, randoms)
    end = time.time()
    print("Sorted Linked List inserted 50 new values in {0} seconds.".format(end - start))


if __name__ == '__main__':
    run()
