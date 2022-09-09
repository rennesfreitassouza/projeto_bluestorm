"""Functions used to sanitize the input string"""
import unicodedata


def sanitize_input(a_str):
    """Function used to normalize and transform to uppercase the letters of the input string."""
    if not a_str == '' :
        sanitized_str = unicodedata.normalize('NFKD', a_str
                    ).encode('ascii', 'ignore').decode('ascii').upper()
    else:
        sanitized_str = ''
    return sanitized_str
