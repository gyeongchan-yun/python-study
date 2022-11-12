#!/usr/bin/python3


def generator():
    yield 1
    yield 2
    yield 3


def function():
    return 1
    return 2
    return 3


def main():
    print("== print generator itself ==")
    print(generator())  # generator object

    print("== print function itself ==")
    print(function())

    print("== print generator in loop ==")
    for g in generator():
        print(g)

    print("== print function in loop ==")
    for f in function():
        print(f)  # raise error because function is not iterator


if __name__ == "__main__":
    main()
