def common_elements():
    first = [i for i in range(100) if i % 3 == 0]
    second = [i for i in range(100) if i % 5 == 0]
    common = set(first) & set(second)
    return common
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")