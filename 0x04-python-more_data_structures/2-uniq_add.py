#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i, num in enumerate(my_list):
        if my_list.index(num) != i:
            continue
        sum += num

    return sum
