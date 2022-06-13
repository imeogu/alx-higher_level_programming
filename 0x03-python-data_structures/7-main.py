#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (2, 80)
tuple_b = (98, 20)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (2, )))
print(add_tuple(tuple_a, ()))
