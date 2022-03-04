from collections.abc import Iterable


class NotIntegerException(Exception):
    pass


def flatten_integer_list(integer_list):
    """Function that flattens a list of integers.

    :param integer_list: The integer list
    """
    for item in integer_list:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            # Get the following nested list
            yield from flatten_integer_list(item)
        else:
            if isinstance(item, int) and not isinstance(item, bool):
                # Validated is integer value and return the following value
                yield item
            else:
                # If the value is not an integer, raise a exception
                raise NotIntegerException(
                    f'The value "{item}" is not a integer'
                )
