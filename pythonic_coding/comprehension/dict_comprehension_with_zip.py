#!/usr/bin/python3

key_list = ['a', 'b', 'c']
value_list = [1, 2, 3]

dict_by_comprehension_with_zip = {k: v for k, v in zip(key_list, value_list)}
print(dict_by_comprehension_with_zip)
