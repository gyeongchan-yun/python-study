# == python 3 == #
# bytes: binary(8-bit), str: unicode


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')  # decode: binary -> unicode
    else:
        value = bytes_or_str
    return value  # str instance


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')  # encode: unicode -> binary
    else:
        value = bytes_or_str
    return value  # bytes instance


# == python 2 == #
# str: binary(8-bit), unicode


def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')  # decode: binary -> unicode
    else:
        value = unicode_or_str
    return value  # unicode instance


def to_bytes(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')  # encode: unicode -> binary
    else:
        value = unicode_or_str
    return value  # str instance
