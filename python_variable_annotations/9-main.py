#!/usr/bin/env python3

element_length =  __import__('9-element_length').element_length

print(element_length.__annotations__)
print(element_length.__doc__)
print(element_length.__name__)
print(element_length.__module__)
print(element_length("hello") == 5)
print(element_length([1, 2, 3]) == 3)
