"""
Performance of Python Data Structures
"""

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))


# Import the timeit module
import timeit
# Import the Timer class defined in the module
from timeit import Timer
# If the above line is excluded, you need to replace Timer with timeit.Timer when defining a Timer object
t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")


# pop performance
pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
print(pop_zero.timeit(number=1000))
print(pop_end.timeit(number=1000))


# ompare the performance of the contains operation between lists and dictionaries
import timeit
import random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x"%i, "from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)

    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)

    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))
