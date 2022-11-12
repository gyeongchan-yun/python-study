#!/usr/bin/python3


def generator(items):
    count = 0

    for item in items:
        if count == 10:
            return 1  # In generator, if return exists StopIteration exception raise

        count += 1
        yield item


if __name__ == "__main__":
    for i in generator(range(15)):
        print(i)
