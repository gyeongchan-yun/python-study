#!/usr/bin/python3
import os
from threading import Thread
import tempfile  # in python >=3.2
import random

# == parent class == #


class InputData(object):
    def read(self):
        raise NotImplementedError


class Worker(object):
    def __init__(self, input_file):
        self.input_file = input_file
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


# == child class == #


class DirPathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


class LineCountWorker(Worker):
    def map(self):
        data = self.input_file.read()
        self.result = data.count('\n')

    def reduce(self, slave):
        self.result += slave.result


def generate_inputs(data_dir):
    for fname in os.listdir(data_dir):
        yield DirPathInputData(os.path.join(data_dir, fname))


def create_workers(inputs):
    workers = []
    for input_file in inputs:
        workers.append(LineCountWorker(input_file))
    return workers


def execute(workers):
    threads = [Thread(target=worker.map) for worker in workers]
    for thread in threads:
        thread.start()
        thread.join()

    master, slaves = workers[0], workers[1:]
    for slave in slaves:
        master.reduce(slave)
    return master.result


def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


def write_test_files(tmp_dir):
    for i in range(100):
        with open(os.path.join(tmp_dir, str(i)), 'w') as f:
            f.write("a\n" * random.randint(0, 100))


with tempfile.TemporaryDirectory() as tmp_dir:
    write_test_files(tmp_dir)
    output = mapreduce(tmp_dir)

print ("There are {} lines.".format(output))
