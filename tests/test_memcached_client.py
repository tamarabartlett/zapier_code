from unittest import TestCase
from memcached_lib.memcached_client import get_cached_value

class MemcachedClientTests(TestCase):

    def test_cached_value(self):
        returned_value = get_cached_value('my_key', 'my_value')
        self.assertEqual(returned_value.decode(), 'my_value')

if __name__ == '__main__':
    unittest.main()
