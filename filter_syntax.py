# -----------------------------------------------------------------------------

n = [1, 2, 3, 4]


def fltr(lst):
    lst2 = [x for x in lst if x > 2]
    return lst2


print(fltr(n))

# or

print(list(filter(lambda x: x > 2, n)))

# list comprehension solution

print([x for x in n if x > 2])
