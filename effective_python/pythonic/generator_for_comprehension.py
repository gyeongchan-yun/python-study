value = [len(x) for x in open('temp_file.txt')]  # If file is long, memory overhead
print(value)

it = (len(x) for x in open('temp_file.txt'))  # generator
print(it)
print(next(it))
