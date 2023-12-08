#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    i = 0
    j = 0
    for k in my_list:
        i += k[0] * k[1]
        j += k[1]
    return (i / j)
