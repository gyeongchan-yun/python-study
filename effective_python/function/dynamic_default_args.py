from datetime import datetime


def log(message, when=datetime.now()):
    print("%s: %s" % (when, message))

log("Hi there!")
# datetime.now() doesn't evaluate again after module loading at initial
log("Hi again!")


# == solution: use None and docstring! == #
""" None is important if arg is mutable.
    python passes args as call by reference.
"""


def log(message, when=None):
    """ Log a message with timestamp.

    Args:
        message: Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    when = datetime.now() if when is None else when
    print("%s: %s" % (when, message))

log("Hi there!")
log("Hi again!")
