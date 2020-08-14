import os
import sys
from pymemcache.client.base import Client

def read_file(file_name):
    f = open(file_name, "wb+")
    count = 0

    for i in range (51):
        # Because the files are max 50MB and are saved in 1MB chunks,
        # there can be no more than 50 chunks
        chunk = get_value("%s_%s" % (i, file_name))
        if chunk is None:
            break
        f.write(chunk)

    f.close()

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
    # write_file('memcached_lib/bigoldfile.dat')
    # print("Wrote file")
    read_file('memcached_lib/bigoldfile.dat')
