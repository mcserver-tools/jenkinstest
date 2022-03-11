def add_numbers(first, second):
    if type(first) == int and type(second) == int:
        return first + second
    else:
        raise TypeError("Can only add integers")
