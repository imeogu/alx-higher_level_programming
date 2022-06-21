#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        quotient = a / b
    except (TypeError, ZeroDivisionError):
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return (quotient)