import json


def decode(data, default={}):  # default dict shares all values of args
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode('bad data')
foo['stuff'] = 5

bar = decode('also bad')
bar['meep'] = 1

print("Foo: %s" % foo)
print("Bar: %s" % bar)


# == solution: None and docstring for mutable args == #


def decode(data, default=None):
    """Load JSON data from a string.

    Args:
        data: JSON data to decode
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['stuff'] = 5

bar = decode('also bad')
bar['meep'] = 1

print("Foo: %s" % foo)
print("Bar: %s" % bar)

