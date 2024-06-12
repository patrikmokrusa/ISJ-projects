#!/usr/bin/env python3
import collections

def log_and_count(key=None, counts=None):
    def outer(fun):
        def inner(*args, **kwargs):
            if key is not None:
                key_index = key
            else:
                key_index = fun.__name__
            print(f"called {fun.__name__} with {args} and {kwargs}")
            rtn_val = fun(*args, **kwargs)
            counts[key_index] = counts[key_index] + 1
            return rtn_val
        return inner
    return outer

my_counter = collections.Counter()

@log_and_count(key = 'basic functions', counts = my_counter)
def f1(a, b=2):
    return a ** b

@log_and_count(key = 'basic functions', counts = my_counter)
def f2(a, b=3):
    return a ** 2 + b

@log_and_count(counts = my_counter)
def f3(a, b=5):
    return a ** 3 - b

f1(2)
f2(2, b=4)
f1(a=2, b=4)
f2(4)
f2(5)
f3(5)
f3(5,4)
print(my_counter)

# a vypíše postupně:
# called f1 with (2,) and {}
# called f2 with (2,) and {'b': 4}
# called f1 with () and {'a': 2, 'b': 4}
# called f2 with (4,) and {}
# called f2 with (5,) and {}
# called f3 with (5,) and {}
# called f3 with (5, 4) and {}

# a po:
# print(my_counter)
# vypíše
# Counter({'basic functions': 5, 'f3': 2})