import os
import sys
from pymemcache.client.base import Client

def get_one_mb_of_file(file_name):
    f_in = open(file_name, 'rb')
    first_mb = f_in.read(1024 * 1024)
    f_in.close()

    f_out = open(file_name+'_1', 'wb')
    f_out.write(first_mb)
    f_out.close()

    return f_out

def file_less_than_50mb(file_name):
    size = os.path.getsize(file_name)
    return size <= 52428800


def get_cached_value(key, value):
    client = Client(('localhost', 11211))
    client.set(key, value)
    return_val = client.get(key)
    return return_val

if __name__ == '__main__':
    print(get_cached_value(sys.argv[1],sys.argv[2]))
