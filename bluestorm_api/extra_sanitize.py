"""Modules integrated with the Python interpreter"""
import unicodedata


def sanitize_input(a_str):
    if not a_str == '' :
        sanitized_str = unicodedata.normalize('NFKD', a_str).encode('ascii', 'ignore').decode('ascii').upper()
    else:
        sanitized_str = ''
    
    return sanitized_str