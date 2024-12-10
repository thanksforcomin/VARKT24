import typing


def result_accumulator(func: typing.Callable) -> typing.Callable:
    l1 = []

    def wrapper(*args, **kwargs):
        func()

    return wrapper
