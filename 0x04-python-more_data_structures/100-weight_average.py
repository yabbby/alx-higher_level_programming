#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    freq = 0

    if not my_list:
        return 0

    for col in my_list:
        sum += col[0] * col[1]
        freq += col[1]

    return sum / freq
