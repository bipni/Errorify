# Errorify

Errorify is a simple Python package designed to streamline error formatting in your projects. With Errorify, you can organize and present errors in a structured and user-friendly manner, enhancing code readability and simplifying debugging processes.

## Install

You can easily install Errorify using pip:

```
pip install errorify
```

## Usage

To utilize Errorify within your Python projects, simply import it and pass the `error` object to the errorify method. It will return the formatted error details string.

Below is an example illustrating how to incorporate Errorify into your code:

```python
from errorify import errorify

try:
    raise ValueError('Invalid Value')
except Exception as e:
    print(errorify(e))
```

## Output

The code snippet provided yields the following output:

```
---------------- Error Details ----------------
Exception Name: ValueError
Exception Message: Invalid Value
Exception File Path: /home/user/Documents/test.py
Exception File Name: test.py
Exception File Line Number: 4
Error File Path: /home/user/Documents/test.py
Error File Name: test.py
Error File Line Number: 4
-----------------------------------------------
```

# Another Example

Code snippet:

```python
from errorify import errorify

try:
    value = 1 / 0

    print(value)
except Exception as e:
    print(errorify(e))
```

Output:

```
---------------- Error Details ----------------
Exception Name: ZeroDivisionError
Exception Message: division by zero
Exception File Path: /home/user/Documents/test.py
Exception File Name: test.py
Exception File Line Number: 4
Error File Path: /home/user/Documents/test.py
Error File Name: test.py
Error File Line Number: 4
-----------------------------------------------
```
