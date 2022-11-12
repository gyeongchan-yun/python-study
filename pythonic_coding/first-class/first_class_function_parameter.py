#!/usr/bin/python3


def square(x):
    return x * x


def bind(func, args):
    result = []
    for arg in args:
        result.append(func(arg))
    return result


def main():
    args = [5, 10]
    print("Assign function to variable & send parameter")
    binding_list = bind(square, args)  # similar with function pointer in C
    print(binding_list)


if __name__ == "__main__":
    main()
