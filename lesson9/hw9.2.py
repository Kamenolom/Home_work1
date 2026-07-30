def difference(*args):
    if not args:
        return 0
    max_number = args[0]
    min_number = args[0]
    for number in args:
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number
    return round(max_number - min_number,2)
print(difference(10.2, -2.2, 0, 1.1, 0.5))