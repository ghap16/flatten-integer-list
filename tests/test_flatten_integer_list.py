from unittest import TestCase
from flatten_integer_list import flatten_integer_list, NotIntegerException


class TestFlattenIntegerList(TestCase):
    def test_one_dimension_list(self):
        integer_list = [1, 2, 3, 4, 5, 6]
        self.assertEqual(
            list(flatten_integer_list(integer_list)), [1, 2, 3, 4, 5, 6]
        )

    def test_ten_dimension_list(self):
        integer_list = [
            1,
            [2, [3, [4, [5, 6, [7, 8, [9, 10, 11, [12, [13, [14]]]]]]]]],
        ]
        self.assertEqual(
            list(flatten_integer_list(integer_list)),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        )

    def test_list_with_duplicate_values(self):
        integer_list = [1, [2, [5, [4, [5, 6, [2, 3, 8, [6, 10]]]]]]]
        self.assertEqual(
            list(flatten_integer_list(integer_list)),
            [1, 2, 5, 4, 5, 6, 2, 3, 8, 6, 10],
        )

    def test_list_with_str_value(self):
        integer_list = [1, [2, [3, "test", [4, [5]]]]]
        with self.assertRaises(NotIntegerException) as nie:
            list(flatten_integer_list(integer_list))
        self.assertEqual(
            str(nie.exception), 'The value "test" is not a integer'
        )

    def test_list_with_float_value(self):
        integer_list = [1, [2, [3, 4.5, [4, [5]]]]]
        with self.assertRaises(NotIntegerException) as nie:
            list(flatten_integer_list(integer_list))
        self.assertEqual(
            str(nie.exception), 'The value "4.5" is not a integer'
        )

    def test_list_with_boolean_value(self):
        integer_list = [1, [2, [3, True, [4, [5]]]]]
        with self.assertRaises(NotIntegerException) as nie:
            list(flatten_integer_list(integer_list))
        self.assertEqual(
            str(nie.exception), 'The value "True" is not a integer'
        )
