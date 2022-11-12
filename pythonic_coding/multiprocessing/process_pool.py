#!/usr/bin/python3

import multiprocessing


def initial_msg():
    print("Start process: %s" % multiprocessing.current_process().name)


def worker(data):
    return data * 2


def main():
    pool = multiprocessing.Pool(processes=4, initializer=initial_msg)
    data = range(10)
    result = pool.map(worker, data)

    pool.close()
    pool.join()

    print("Result: %s" % result)


if __name__ == "__main__":
    main()
