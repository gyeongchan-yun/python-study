def greeting(name):
    greeting_msg = "Hello"

    def add_name():
        nonlocal greeting_msg  # only python3 supports
        greeting_msg += " "
        return "%s%s" % (greeting_msg, name)

    msg = add_name()
    print (msg)


if __name__ == "__main__":
    greeting("python")
