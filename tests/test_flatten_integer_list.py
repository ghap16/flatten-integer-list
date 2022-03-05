from unittest import TestCase

from flatten_integer_list import flatten_integer_list, NotIntegerException


class TestFlattenIntegerList(TestCase):
    def _print_input_output(self, method, description, input_list, output):
        print("Method:", method)
        print(description)
        print("Input:", input_list)
        print("Output:", output)

    def test_list_of_one_dimensions(self):
        """Asserts that the function works with a one-dimensional list"""
        integer_list = [1, 2, 3, 4, 5, 6]
        output = list(flatten_integer_list(integer_list))
        self._print_input_output(
            self._testMethodName, self._testMethodDoc, integer_list, output
        )

        self.assertEqual(output, [1, 2, 3, 4, 5, 6])

    def test_list_of_ten_dimensions(self):
        """Asserts that the list with ten dimensions can be flattened"""
        integer_list = [
            1,
            [2, [3, [4, [5, 6, [7, 8, [9, 10, 11, [12, [13, [14]]]]]]]]],
        ]
        output = list(flatten_integer_list(integer_list))
        self._print_input_output(
            self._testMethodName, self._testMethodDoc, integer_list, output
        )

        self.assertEqual(
            output,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        )

    def test_list_with_duplicate_values(self):
        """Asserts that the list with duplicate values can be flattened"""
        integer_list = [1, [2, [5, [4, [5, 6, [2, 3, 8, [6, 10]]]]]]]
        output = list(flatten_integer_list(integer_list))
        self._print_input_output(
            self._testMethodName, self._testMethodDoc, integer_list, output
        )

        self.assertEqual(
            output,
            [1, 2, 5, 4, 5, 6, 2, 3, 8, 6, 10],
        )

    def test_list_with_str_value(self):
        """Asserts that string-valued lists are invalid"""
        integer_list = [1, [2, [3, "test", [4, [5]]]]]

        with self.assertRaises(NotIntegerException) as nie:
            list(flatten_integer_list(integer_list))

        self._print_input_output(
            self._testMethodName,
            self._testMethodDoc,
            integer_list,
            str(nie.exception),
        )

        self.assertEqual(
            str(nie.exception), 'The value "test" is not a integer'
        )

    def test_list_with_float_value(self):
        """Asserts that float-valued lists are invalid"""
        integer_list = [1, [2, [3, 4.5, [4, [5]]]]]

        with self.assertRaises(NotIntegerException) as nie:
            list(flatten_integer_list(integer_list))

        self._print_input_output(
            self._testMethodName,
            self._testMethodDoc,
            integer_list,
            str(nie.exception),
        )

        self.assertEqual(
            str(nie.exception), 'The value "4.5" is not a integer'
        )

    def test_list_with_boolean_value(self):
        """Asserts that boolean-valued lists are invalid"""
        integer_list = [1, [2, [3, True, [4, [5]]]]]

        with self.assertRaises(NotIntegerException) as nie:
            list(flatten_integer_list(integer_list))

        self._print_input_output(
            self._testMethodName,
            self._testMethodDoc,
            integer_list,
            str(nie.exception),
        )

        self.assertEqual(
            str(nie.exception), 'The value "True" is not a integer'
        )
