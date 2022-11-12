#!/usr/bin/python3

EXIST_FILE = "sample_file"
NON_EXIST_FILE = "dump_file"


def read_file(file_name):
    try:
        f = open(file_name, 'r')
    except:
        print("File Open Error")
    else:  # exception optimization
        print(f.read())
        f.close()
    finally:
        print("End file read")


if __name__ == "__main__":
    read_file(EXIST_FILE)
    read_file(NON_EXIST_FILE)
