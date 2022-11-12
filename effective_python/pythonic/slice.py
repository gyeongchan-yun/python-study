origin = ['a', 'b', 'c', 'd']
slice_origin = origin[:3]
print("slice_origin: ", slice_origin)
slice_origin[1] = 'd'
print("Change slice_origin: ", slice_origin)
print("No change origin: ", origin)  # implies sliced list is new one

copy = origin[:]  # The fancy way of deep-copy
copy[1] = 'd'
print(copy, origin)
