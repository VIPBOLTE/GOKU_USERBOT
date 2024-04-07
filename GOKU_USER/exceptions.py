"""
Exceptions which can be raised by GOKU_USER Itself.
"""


class GOKU_USERError(Exception):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(GOKU_USERError):
    ...
