#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [11, 23, 32, 49, 55]
idx = 4
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
