#!/usr/bin/python3

LOWER_LIST = ["python", "python1", "python2"]
UPPER_LIST = []


def convert(text):
    return text.upper()


def main():
    UPPER_LIST = map(convert, LOWER_LIST)
    print(UPPER_LIST)

