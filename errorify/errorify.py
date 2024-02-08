import os
import sys
import traceback


def errorify(error):
    """
    Formats and retrieves details about the caught exception.

    Parameters:
    error (Exception): The caught exception object.

    Returns:
    str: A formatted string containing details about the exception, including:
        - Exception Name: The name of the exception class.
        - Exception Message: The message associated with the exception.
        - Exception File Path: The absolute path of the file where the exception occurred.
        - Exception File Name: The name of the file where the exception occurred.
        - Exception File Line Number: The line number in the file where the exception occurred.
        - Error File Path: The path of the file where the specific error occurred (if available).
        - Error File Name: The name of the file where the specific error occurred (if available).
        - Error File Line Number: The line number in the file where the specific error occurred (if available).

    Example:
    >>> try:
    ...     # Some code that might raise an exception
    ...     raise ValueError("Invalid value")
    ... except ValueError as e:
    ...     error_details = errorify(e)
    ...     print(error_details)
    Exception Name: ValueError
    Exception Message: Invalid value
    Exception File Path: /path/to/your/file.py
    Exception File Name: file.py
    Exception File Line Number: 42
    Error File Path: /path/to/your/error_file.py
    Error File Name: error_file.py
    Error File Line Number: 10

    Note:
    - This method is intended to be used within an exception handling block.
    - The error details include information about both the caught exception and the specific error if available.
    """
    _, exc_obj, exc_tb = sys.exc_info()
    exc_info = sys.exc_info()
    specific_error = traceback.format_exception(*exc_info)[len(traceback.format_exception(*exc_info)) - 2]

    filepath = os.path.abspath(exc_tb.tb_frame.f_code.co_filename)
    filename = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    line = exc_tb.tb_lineno

    parts = specific_error.split(', ')
    error_filepath = parts[0].split('"')[1]
    error_filename = error_filepath.split("/")[-1]
    error_line = parts[1].split(' ')[1]

    error_details = [
        '---------------- Error Details ----------------',
        f'Exception Name: {type(error).__name__}',
        f'Exception Message: {str(exc_obj)}',
        f'Exception File Path: {filepath}',
        f'Exception File Name: {filename}',
        f'Exception File Line Number: {str(line)}',
        f'Error File Path: {error_filepath}',
        f'Error File Name: {error_filename}',
        f'Error File Line Number: {error_line}',
        '-----------------------------------------------'
    ]

    return '\n'.join(error_details)
