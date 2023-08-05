# -*- coding: utf-8 -*-

"""utils CLI functions
"""

import time

from functools import wraps
import termcolor


def report_log(message: str, type_log: str ="I") -> None:
    """Returns report log
    letter code to specify type of report
    'I' > Info | 'W' > Warning | 'E' > Error | 'S' > Success | 'V' > Verbose
    """
    if type_log == "I":  # Info
        return print(f"[INFO    ℹ] {message}")
    if type_log == "W":  # Warning
        return termcolor.cprint(f"[WARNING ▲] {message}", "yellow")
    if type_log == "E":  # Error
        return termcolor.cprint(f"[ERROR   ⤬]  {message}", "red")
    if type_log == "S":  # Success
        return termcolor.cprint(f"[SUCCESS ✅]  {message}", "green")
    if type_log == "V":  # Verbose
        return termcolor.cprint(f"[DETAILS ℹ]  {message}", "blue")
    else:
        return print(message)


def timing(function):
    """A decorator to compute execution time of any function
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        report_log(f'Total execution : {end-start} secs')
        return result
    return wrapper