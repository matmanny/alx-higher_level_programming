#!/usr/bin/python3
def best_score(a_dictionary):
    i = 0
    res = ""
    if a_dictionary:
        for p, m in a_dictionary.items():
            if m > i:
                res = p
                i = m
        return res
    else:
        return None
