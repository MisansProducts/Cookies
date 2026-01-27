"""
Centralized error messages for consistent user feedback.
"""

ERROR_MESSAGES = {
    'invalid_int': "Error: Please enter a valid integer!",
    'invalid_number': "Error: Please enter a valid number!",
    'min_value': "Error: {parameter_name} must be at least {min_val}!",
    'max_value': "Error: {parameter_name} must be at most {max_val}!",
    'range_value': "Error: {parameter_name} must be between {min_val} and {max_val}!",
    'positive': "Error: Value must be positive!",
    'non_negative': "Error: Value cannot be negative!",
    'format': "Error: Incorrect format."
}


def get_error_message(key, **kwargs):
    """Get formatted error message by key."""
    if key in ERROR_MESSAGES:
        return ERROR_MESSAGES[key].format(**kwargs)
    return "Error: Invalid input!"
