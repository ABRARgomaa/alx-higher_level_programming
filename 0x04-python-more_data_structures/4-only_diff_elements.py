#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    b = set_1.union(set_2)
    a = set_1.intersection(set_2)
    return (b - a)
