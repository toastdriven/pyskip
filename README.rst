======
pyskip
======

A pure Python skiplist implementation.

A skiplist provides a quickly searchable structure (like a balanced binary
tree) that also updates fairly cheaply (no nasty rebalancing acts).
In other words, it's **awesome**.

See http://en.wikipedia.org/wiki/Skip_list for more information.

Written mostly an exercise for myself, it turns out skiplists are really useful.
It also comes with a (mostly-underdocumented) linked-list implementation
(+ a sorted variant), if that's useful.


Requirements
============

* Python 3.3+ (should work on Python 2.6+ as well, as well as PyPy 2.0+)
* ``nose>=1.30`` for running unittests


Usage
=====

Using it looks like:

    >>> import skiplist
    >>> skip = skiplist.Skiplist()
    >>> len(skip)
    0
    >>> 6 in skip
    False
    >>> skip.insert(0)
    >>> skip.insert(7)
    >>> skip.insert(3)
    >>> skip.insert(6)
    >>> skip.insert(245)
    >>> len(skip)
    5
    >>> 6 in skip
    True
    >>> skip.remove(245)
    >>> len(skip)
    4
    >>> skip.find(3)
    <Skiplist: 3>


Performance
===========

Performance is alright, though I'm sure there's room for improvement. See the
``bench.py`` script for more information.


Running Tests
=============

Run ``pip install nose`` (preferrably within a virtualenv) to install nose.

Then run ``nosetests -s -v tests.py`` to exercise the full suite.


TODO
====

* A more performant implementation of ``remove`` (still O(N))
* More performance testing

    * Loading data seems slow


Meta
====

:author: Daniel Lindsley
:license: BSD
:version: 0.9.0
