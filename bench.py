import random
import time

import skiplist


MAX_LOAD = 1000


def load_skiplist():
    skip = skiplist.Skiplist()

    for i in range(MAX_LOAD):
        print(i, end='\r')
        skip.insert(i)

    print()
    return skip


def load_list():
    the_list = []

    for i in range(MAX_LOAD):
        inserted = False

        # Simulate a sorted list.
        for offset, value in enumerate(the_list):
            if offset is 0:
                the_list.append(i)
                inserted = True
            elif value > i:
                the_list.insert(offset, i)
                inserted = True

        if not inserted:
            the_list.append(i)

    return the_list


def contains_skiplist(skip, randoms):
    for rand in randoms:
        assert rand in skip


def contains_list(the_list, randoms):
    for rand in randoms:
        try:
            assert rand in the_list
        except AssertionError:
            print("{0} not in the list?".format(rand))


def run():
    start = time.time()
    skip = load_skiplist()
    end = time.time()
    print("Skiplist loaded in {0} seconds.".format(end - start))

    start = time.time()
    the_list = load_list()
    end = time.time()
    print("List loaded in {0} seconds.".format(end - start))

    print()

    randoms = [random.randint(0, MAX_LOAD - 1) for i in range(20)]

    start = time.time()
    skip = contains_skiplist(skip, randoms)
    end = time.time()
    print("Skiplist checked contains in {0} seconds.".format(end - start))

    start = time.time()
    skip = contains_list(the_list, randoms)
    end = time.time()
    print("List checked contains in {0} seconds.".format(end - start))


if __name__ == '__main__':
    run()
