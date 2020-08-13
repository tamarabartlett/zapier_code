import sys
from pymemcache.client.base import Client

def get_cached_value(key, value):
    client = Client(('localhost', 11211))
    client.set(key, value)
    return_val = client.get(key)
    return return_val

if __name__ == '__main__':
    print(get_cached_value(sys.argv[1],sys.argv[2]))
