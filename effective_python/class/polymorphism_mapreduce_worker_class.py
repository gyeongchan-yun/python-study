#!/usr/bin/python3
import os
from threading import Thread
import tempfile  # in python >=3.2
import random

# == parent class == #


class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class GenericWorker(object):
    def __init__(self, input_file):
        self.input_file = input_file
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_cls, config):
        workers = []
        for input_file in input_cls.generate_inputs(config):
            workers.append(cls(input_file))
        return workers

# == child class == #


class DirPathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for fname in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, fname))


class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_file.read()
        self.result = data.count('\n')

    def reduce(self, slave):
        self.result += slave.result


def execute(workers):
    threads = [Thread(target=worker.map) for worker in workers]
    for thread in threads:
        thread.start()
        thread.join()

    master, slaves = workers[0], workers[1:]
    for slave in slaves:
        master.reduce(slave)
    return master.result


def mapreduce(worker_cls, input_cls, config):
    workers = worker_cls.create_workers(input_cls, config)
    return execute(workers)


def write_test_files(tmp_dir):
    for i in range(100):
        with open(os.path.join(tmp_dir, str(i)), 'w') as f:
            f.write("a\n" * random.randint(0, 100))


with tempfile.TemporaryDirectory() as tmp_dir:
    write_test_files(tmp_dir)
    config = {'data_dir': tmp_dir}
    # Take args as class and works on the same method regardless of class. -> implement polymorphism
    output = mapreduce(LineCountWorker, DirPathInputData, config)

print ("There are {} lines.".format(output))
