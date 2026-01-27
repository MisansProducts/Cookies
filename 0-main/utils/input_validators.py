"""
Input validation helper functions.
"""

import sys
from utils.error_messages import get_error_message

def get_valid_int(prompt, min_val=None, max_val=None, parameter_name="Value"):
    """Get validated integer input with range checking."""
    try:
        value = int(input(prompt))
        if min_val is not None and max_val is not None and (value < min_val or value > max_val):
            print(get_error_message('range_value', parameter_name=parameter_name, min_val=min_val, max_val=max_val))
            sys.exit(1)
        if min_val is not None and value < min_val:
            print(get_error_message('min_value', parameter_name=parameter_name, min_val=min_val))
            sys.exit(1)
        if max_val is not None and value > max_val:
            print(get_error_message('max_value', parameter_name=parameter_name, max_val=max_val))
            sys.exit(1)
        return value
    except ValueError:
        print(get_error_message('invalid_int'))
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        sys.exit(1)

def get_valid_float(prompt, min_val=None, parameter_name="Value"):
    """Get validated float input with minimum checking."""
    try:
        value = float(input(prompt))
        if min_val is not None and value < min_val:
            print(get_error_message('min_value', parameter_name=parameter_name, min_val=min_val))
            sys.exit(1)
        return value
    except ValueError:
        print(get_error_message('invalid_number'))
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        sys.exit(1)
