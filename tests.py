import unittest

from hashmap import HashMap


class HashMapTestCase(unittest.TestCase):

    def test_can_set_and_get_basic_case(self):
        hashmap = HashMap()
        self.assertEqual(hashmap._number_of_elements, 0)
        hashmap.set('key', 'val')
        self.assertEqual(hashmap._number_of_elements, 1)
        self.assertEqual(hashmap.get('key'), 'val')
        self.assertIsNone(hashmap.get('otherval'))

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
        self.assertIsNone(hashmap.get('blah'))

    def test_get_uses_default_when_key_not_present(self):
        hashmap = HashMap()
        hashmap['key'] = 'val'
        self.assertEqual(hashmap.get('key'), 'val')
        self.assertEqual(hashmap.get('key2', 'default'), 'default')
        self.assertEqual(hashmap.get('key2', 'blah'), 'blah')

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

    def test_getitem_magic_method_raises_value_error_when_target_key_not_extant(self):
        hashmap = HashMap()
        hashmap['key'] = 'val'
        self.assertEqual(hashmap['key'], 'val')
        with self.assertRaises(ValueError):
            hashmap['not_key']


if __name__ == '__main__':
    unittest.main()
