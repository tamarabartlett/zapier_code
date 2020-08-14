import os
import sys
from pymemcache.client.base import Client

def write_one_mb_of_file(file_name):
    f_in = open(file_name, 'rb')
    one_mb = f_in.read(1024 * 1023)
    f_in.close()

    set_value('1_'+file_name, one_mb)
    return one_mb

def get_chunk(file_name):
    f_in = open(file_name, 'rb')
    chunk = f_in.read(1024 * 1023)
    f_in.close()

    return chunk

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
