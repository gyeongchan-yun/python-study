#!/usr/bin/python3


def closure():

    def inner():
        pass

    inner_atr = dir(inner())
    print("== Inner Attribute ==")
    print(inner_atr)

    return inner


if __name__ == "__main__":
    closure_atr = dir(closure())

    print("== Closure Attribute ==")
    print(closure_atr)
    closure = closure()
    print(closure.__closure__)  # print nonlocal variable in closure
