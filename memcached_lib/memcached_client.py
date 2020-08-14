import os
import sys
from pymemcache.client.base import Client

def write_file(file_name):
    f_in = open(file_name, 'rb')
    chunk = f_in.read(1024 * 1023)
    count = 0
    while chunk != b'':
        print("Filename: %s_%s" % (count, file_name))
        set_value("%s_%s" % (count, file_name), chunk)
        count += 1
        chunk = f_in.read(1024 * 1023)
    f_in.close()


def file_less_than_50mb(file_name):
    size = os.path.getsize(file_name)
    return size <= 52428800


def get_value(key):
    client = Client(('localhost', 11211))
    return client.get(key)


def set_value(key, value):
    client = Client(('localhost', 11211))
    client.set(key, value)


if __name__ == '__main__':
    with open('derp.txt', 'wb') as f:
        f.write(b'0' * 1024 * 1024 *2)
        f.close()
    print(write_one_mb_of_file('derp.txt'))
