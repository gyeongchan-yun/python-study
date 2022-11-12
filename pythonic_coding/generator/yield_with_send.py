#!/usr/bin/python3


def generator():
    value = 2
    while True:
        print (value)
        value = yield
        # yield value -> only convey value of 2


def main():
    g = generator()

    next(g)  # convey local variable 'value'
    g.send(3)
    g.send(5)
    next(g)  # convey 'None'


if __name__ == "__main__":
    main()
