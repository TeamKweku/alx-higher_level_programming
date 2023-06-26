#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides 2 integers and prints the result

    Args:
        a: numerator
        b: denominator

    Return:
        value of a / b or None
    """
    try:
        num = a / b
    except ZeroDivisionError:
        num = None
    finally:
        print("Inside result: {}".format(num))
        return (num)
