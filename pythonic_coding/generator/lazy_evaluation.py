#!/usr/bin/python3

import time


def wait(num):
    print("sleep")
    time.sleep(0.5)
    return num


def print_items(items):
    for item in items:
        print(item)


def main():
    print("==print list with wait function==")
    wait_list = [wait(i) for i in range(10)]
    print_items(wait_list)

    print("==print generator with wait function==")
    wait_generator = (wait(i) for i in range(10))
    print_items(wait_generator)


if __name__ == "__main__":
    main()
