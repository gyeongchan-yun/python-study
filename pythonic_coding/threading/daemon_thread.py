#!/usr/bin/python3

import logging
import threading
import time

# log record attributes: (threadName)s -> the name of thread
# Reference: https://docs.python.org/3/library/logging.html
logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")


def daemon():
    logging.debug("Start")
    time.sleep(5)
    logging.debug("Exit")


def main():
    t = threading.Thread(target=daemon, name="Daemon thread")
    t.setDaemon(True)

    t.start()
    # t.join() -> If join() is called, main thread waits until damone terminates.

if __name__ == "__main__":
    main()
