from unittest import TestCase
from memcached_lib.initial_code import file_less_than_50mb

class InitialCodeTests(TestCase):

    def less_than_50mb_is_true(self):
        small_file = open("small_file.txt", "a")
        small_file.write("Now the file has more content!")
        small_file.close()

        self.assertTrue(small_file)

if __name__ == '__main__':
    unittest.main()
