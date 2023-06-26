#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of int num a by int num  b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
