#!/usr/bin/python3

import multiprocessing
import time


def daemon():
    print("Start")
    time.sleep(5)
    print("Exit")


def main():
    p = multiprocessing.Process(target=daemon, name="Daemon process")
    p.daemon = True

    p.start()
    time.sleep(3)
    # t.join() -> If join() is called, main thread waits until damone terminates.

if __name__ == "__main__":
    main()
