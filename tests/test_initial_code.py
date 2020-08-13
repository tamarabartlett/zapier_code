import os

from unittest import TestCase
from memcached_lib.initial_code import (
    file_less_than_50mb,
    get_one_mb_of_file,
)

class InitialCodeTests(TestCase):

    def test_get_first_mb_is_one_mb(self):
        file_name = 'two_mb_file.txt'
        with open(file_name, 'wb') as f:
            one_mb = 1024 * 1024
            two_mb = one_mb * 2
            f.write(b'0' * two_mb)

            returned_file = get_one_mb_of_file(file_name)
            file_size = os.path.getsize('two_mb_file.txt_1')
        self.assertEqual(one_mb, file_size)


    def test_file_less_than_50mb_is_true(self):
        file_name = "small_file.txt"
        small_file = open(file_name, "w")
        small_file.close()

        self.assertTrue(file_less_than_50mb(file_name))

    def test_file_50mb_is_true(self):
        file_name = 'fifty_mb_file.txt'
        with open(file_name, 'wb') as f:
            one_mb = 1024 * 1024
            fifty_mb = one_mb * 50
            f.write(b'0' * fifty_mb)

        self.assertTrue(file_less_than_50mb(file_name))

    def test_file_greater_than_50mb_is_false(self):
        file_name = 'fifty_one_mb_file.txt'
        with open(file_name, 'wb') as f:
            one_mb = 1024 * 1024
            fifty_one_mb = one_mb * 51
            f.write(b'0' * fifty_one_mb)

        self.assertFalse(file_less_than_50mb(file_name))

if __name__ == '__main__':
    unittest.main()
