#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_el1 = 0 if len(tuple_a) == 0 else tuple_a[0]
    b_el1 = 0 if len(tuple_b) == 0 else tuple_b[0]
    a_el2 = 0 if len(tuple_a) <= 1 else tuple_a[1]
    b_el2 = 0 if len(tuple_b) <= 1 else tuple_b[1]
    return (a_el1 + b_el1, a_el2 + b_el2)
