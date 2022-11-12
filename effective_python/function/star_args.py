def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(value) for value in values)
        print("%s: %s" % (message, values_str))

log("My numbers are", [1, 2])
log("Hi there")
