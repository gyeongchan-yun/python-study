# == use list comprehension instead of map, filter with lambda. == #

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [num ** 2 for num in num_list]
print(squares)

# map
squares_by_map = map(lambda num: num ** 2, num_list)
print(squares_by_map)

even_squares = [num ** 2 for num in num_list if num % 2 == 0]
print(even_squares)

even_squares_by_map_filter = map(lambda num: num ** 2,
                                 filter(lambda num: num % 2, num_list))


# == avoid using list comprehension with multiple complex loop == #
# multiple loop
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)  # >>> [1, 2, 3, 4, 5, 6, 7, 8, 9]

square_matrix = [[x ** 2 for x in row] for row in matrix]
print(square_matrix)  # >>> [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

# List comprehension supports multiple if condition which is same as if and
evens = [num for num in num_list if x > 0 if x % 2 == 0]
evens_and = [num for num in num_list if x > 0 and x % 2 == 0]
