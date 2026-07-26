def add_one(some_list):
    number = "".join(map(str,some_list))
    number = int(number) + 1
    number = str(number)
    number = list(map(int, number))
    return number

print(add_one([1, 2, 3, 4]))
print(add_one([9, 9, 9]))
print(add_one([0]))
print(add_one([9]))