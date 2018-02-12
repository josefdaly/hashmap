import unittest

from hashmap import HashMap


class HashMapTestCase(unittest.TestCase):

    def test_can_set_and_get_basic_case(self):
        hashmap = HashMap()
        self.assertEqual(hashmap._number_of_elements, 0)
        hashmap.set('key', 'val')
        self.assertEqual(hashmap._number_of_elements, 1)
        self.assertEqual(hashmap.get('key'), 'val')
        with self.assertRaises(Exception):
            hashmap.get('otherval')

    def test_can_set_and_get_multiple_values(self):
        hashmap = HashMap()
        self.assertEqual(hashmap._number_of_elements, 0)
        hashmap.set('key', 'val')
        self.assertEqual(hashmap._number_of_elements, 1)
        self.assertEqual(hashmap.get('key'), 'val')
        hashmap.set('otherkey', 'otherval')
        self.assertEqual(hashmap._number_of_elements, 2)
        self.assertEqual(hashmap.get('otherkey'), 'otherval')
        self.assertEqual(hashmap.get('key'), 'val')
        with self.assertRaises(Exception):
            hashmap.get('blah')

    def test_can_set_and_get_many_values(self):
        hashmap = HashMap()
        for number in range(0, 20):
            key, val = str(number), number
            hashmap.set(key, val)
        self.assertEqual(hashmap._number_of_elements, 20)
        for number in range(0, 20):
            key, expected_val = str(number), number
            self.assertEqual(hashmap.get(key), expected_val)

    def test_len_method(self):
        hashmap = HashMap()
        self.assertEqual(len(hashmap), 0)
        for number in range(0, 20):
            hashmap.set(str(number), number)
        self.assertEqual(len(hashmap), 20)

    def test_set_item_and_get_item_hook_methods(self):
        hashmap = HashMap()
        hashmap['key'] = 'val'
        hashmap['other_key'] = 'other_val'
        self.assertEqual(hashmap['key'], 'val')
        self.assertEqual(hashmap['other_key'], 'other_val')


if __name__ == '__main__':
    unittest.main()
