# -----------------------------------------------------------------------------

# map -> apply same function to each element of a sequence and return the modified list

n = [1, 2, 3, 4]


def square(lst1):
    lst2 = []
    for num in lst1:
        lst2.append(num**2)
    return lst2


print(square(n))

# or

print(list(map(lambda x: x**2, n)))

# list comprehension solution

print([x**2 for x in n])
