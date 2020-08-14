import os
import sys
import filecmp
import time

from unittest import TestCase
from memcached_lib.memcached_client import (
    file_less_than_50mb,
    write_file,
    read_file,
    get_value,
    set_value,
    set_many,
)

ONE_MB = 1024 * 1024

def create_file(file_name, size):
    with open(file_name, 'wb') as f:
        f.write(b'0' * size)
        f.close()

class MemcachedClientTests(TestCase):

        

    def test_save_and_retrieved_files_are_same(self):
        write_file('tests/bigoldfile.dat')

        # rename original file to have something to compare against
        os.rename('tests/bigoldfile.dat','tests/bigoldfile_orig.dat')
        read_file('tests/bigoldfile.dat')

        self.assertTrue(filecmp.cmp('tests/bigoldfile_orig.dat', 'tests/bigoldfile.dat'))

        # rename back to original name, to cleanup
        # would probably do this in a cleanup method normally
        os.rename('tests/bigoldfile_orig.dat','tests/bigoldfile.dat')


    def test_get_first_mb_is_one_mb(self):
        file_name = 'tests/data/two_mb_file.txt'
        two_mb = ONE_MB * 2

        create_file(file_name, two_mb)

        expected = write_file(file_name)

        actual = get_value('1_two_mb_file.txt')
        self.assertEqual(expected, actual)


    def test_file_less_than_50mb_is_true(self):
        file_name = "tests/data/small_file.txt"
        small_file = open(file_name, "w")
        small_file.close()

        self.assertTrue(file_less_than_50mb(file_name))

    def test_file_50mb_is_true(self):
        file_name = 'tests/data/fifty_mb_file.txt'
        fifty_mb = ONE_MB * 50

        create_file(file_name, fifty_mb)

        self.assertTrue(file_less_than_50mb(file_name))

    def test_file_greater_than_50mb_is_false(self):
        file_name = 'tests/data/fifty_one_mb_file.txt'
        fifty_one_mb = ONE_MB * 51

        create_file(file_name, fifty_one_mb)

        self.assertFalse(file_less_than_50mb(file_name))

    def test_cached_value(self):
        dict = {'my_key': 'my_value'}
        dict['my_other_key'] = 'my_other_value'
        failed_keys = set_many(dict)

        returned_value = get_value('my_key')
        returned_other_value = get_value('my_other_key')

        self.assertEqual(returned_value.decode(), 'my_value')
        self.assertEqual(returned_other_value.decode(), 'my_other_value')


if __name__ == '__main__':
    unittest.main()
