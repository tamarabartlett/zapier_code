import os
import sys
from pymemcache.client.base import Client

# def read_file(file_name):
#     concat_chunk = b''
#     count = 0
#
#     while client.check_key()
#     chunk = get_value("%s_%s" % (count, file_name))
#
#

def write_file(file_name):
    f_in = open(file_name, 'rb')

    chunk = f_in.read(1024 * 1023)
    count = 0
    key = '%s_%s' % (count, file_name)

    dict_to_write = {key: chunk}
    while chunk != b'':
        chunk = f_in.read(1024 * 1023)
        count += 1
        key = '%s_%s' % (count, file_name)
        dict_to_write[key] = chunk

    f_in.close()
    set_many(dict_to_write)


def file_less_than_50mb(file_name):
    size = os.path.getsize(file_name)
    return size <= 52428800


def get_value(key):
    client = Client(('localhost', 11211))
    return client.get(key)


def set_value(key, value):
    client = Client(('localhost', 11211))
    client.set(key, value)

def set_many(dict):
    client = Client(('localhost', 11211))
    failed_keys = client.set_many(dict, noreply=False)
    return failed_keys

if __name__ == '__main__':
    with open('derp.txt', 'wb') as f:
        f.write(b'0' * 1024 * 1024 *2)
        f.close()
    print(write_one_mb_of_file('derp.txt'))
