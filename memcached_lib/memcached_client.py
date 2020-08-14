import os
import sys
from pymemcache.client.base import Client

# Would normally install a linter

def cache_file(file_name):
    if file_less_than_50mb(file_name):
        if file_does_not_exist(file_name):
            return write_file(file_name)
        else:
            raise FileAlreadyExistsException("File is already in cache")
    else:
        raise FileTooLargeException("File must be less than 50mb")

def read_file(file_name):
    f = open(file_name, "wb+")
    count = 0

    for i in range (51):
        # Because the files are max 50MB and are saved in 1MB chunks,
        # there can be no more than 50 chunks
        chunk = get_value("%s_%s" % (i, file_name))
        if chunk is None:
            # if not even one chunk had any content, the file didn't exist in cache
            if i == 0:
                raise FileNotFoundExcpetion("File does not exist in cache")
            break
        f.write(chunk)
    f.close()

    return f


# I would probably normally make every method except read_file and cache_file
# some kind of private method
def file_does_not_exist(file_name):
    if get_value('0_'+file_name) is None:
        return True
    else:
        return False


def write_file(file_name):
    chunk_size = 1024 * 1023
    f_in = open(file_name, 'rb')

    chunk = f_in.read(chunk_size)
    key = '0_%s' % (file_name)
    dict_to_write = {key: chunk}

    chunk = f_in.read(chunk_size)
    count = 1
    while chunk != b'':
        key = '%s_%s' % (count, file_name)
        dict_to_write[key] = chunk
        chunk = f_in.read(chunk_size)
        count += 1

    f_in.close()
    failed_keys = set_many(dict_to_write)
    return failed_keys


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


class FileTooLargeException(Exception):
    pass


class FileNotFoundExcpetion(Exception):
    pass


class FileAlreadyExistsException(Exception):
    pass
