#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a if len(tuple_a) >= 2 else tuple_a + (0, 0)
    b = tuple_b if len(tuple_b) >= 2 else tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
