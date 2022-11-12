#!/usr/bin/python3

import time
import multiprocessing


def server(pipe):
    p = multiprocessing.current_process()
    msg = "Hello World!"
    pipe.send(msg)
    print("[%s] send a message to pipe: %s" % (p.name, msg))


def main():
    client_pipe, server_pipe = multiprocessing.Pipe()  # return 2 objects with 1:1 communication

    p = multiprocessing.Process(name="server process", target=server, args=(server_pipe,))
    p.start()

    print("Received message: %s" % client_pipe.recv())
    p.join()


if __name__ == "__main__":
    main()
