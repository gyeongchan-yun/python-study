#!/usr/bin/python3


def closure(func, *const_args):

    def wrapper(*extra_args):
        args = list(const_args)
        args.extend(extra_args)
        return func(*args)

    return wrapper


def logging(year, month, day, title, content):
    print("%s-%s-%s %s:%s" % (year, month, day, title, content))


def main():
    f = closure(logging, "2019", "01", "04")
    f("closure", "partial application")


if __name__ == "__main__":
    main()
