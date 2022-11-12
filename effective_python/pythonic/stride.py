num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odds = num_list[::2]
evens = num_list[1::2]  # from index 1, slice with stride of 2
print(odds)
print(evens)
