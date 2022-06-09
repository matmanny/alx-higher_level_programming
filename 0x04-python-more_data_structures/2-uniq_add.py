#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    les = 0
    for i in new:
        les += i
    return les
