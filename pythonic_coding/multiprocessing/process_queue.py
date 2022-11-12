#!/usr/bin/python3

import time
import multiprocessing


def set(q):
    p = multiprocessing.current_process()
    msg = "Hello World!"
    q.put(msg)
    print("[%s] set queue data: %s" % (p.name, msg))


def get(q):
    p = multiprocessing.current_process()
    print("[%s] get queue data: %s" % (p.name, q.get()))


def main():
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(name="set", target=set, args=(queue,))
    p1.start()

    p2 = multiprocessing.Process(name="get", target=get, args=(queue,))
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
