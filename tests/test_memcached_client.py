import os

from unittest import TestCase
from memcached_lib.memcached_client import (
    file_less_than_50mb,
    get_one_mb_of_file,
    get_value,
    set_value,
)

ONE_MB = 1024 * 1024

def create_file(file_name, size):
    with open(file_name, 'wb') as f:
        f.write(b'0' * size)
        f.close()

class MemcachedClientTests(TestCase):

    def test_get_first_mb_is_one_mb(self):
        file_name = 'two_mb_file.txt'
        two_mb = ONE_MB * 2

        create_file(file_name, two_mb)

        returned_file = get_one_mb_of_file(file_name)
        file_size = os.path.getsize('two_mb_file.txt_1')
        self.assertEqual(ONE_MB, file_size)


    def test_file_less_than_50mb_is_true(self):
        file_name = "small_file.txt"
        small_file = open(file_name, "w")
        small_file.close()

        self.assertTrue(file_less_than_50mb(file_name))

    def test_file_50mb_is_true(self):
        file_name = 'fifty_mb_file.txt'
        fifty_mb = ONE_MB * 50

        create_file(file_name, fifty_mb)

        self.assertTrue(file_less_than_50mb(file_name))

    def test_file_greater_than_50mb_is_false(self):
        file_name = 'fifty_one_mb_file.txt'
        fifty_one_mb = ONE_MB * 51

        create_file(file_name, fifty_one_mb)

        self.assertFalse(file_less_than_50mb(file_name))

    def test_cached_value(self):
        set_value('my_key', 'my_value')
        returned_value = get_value('my_key')
        self.assertEqual(returned_value.decode(), 'my_value')

if __name__ == '__main__':
    unittest.main()
