# -----------------------------------------------------------------------------

# reduce -> applies same operation to items of a sequence 
# uses result of operation as first parameter of next operation
# returns an item not a list


n = [1, 2, 3, 4]


def mult(lst):
    prod = lst[0]
    for i in range(1, len(lst)):
        prod *= lst[i]
    return prod


print(mult(n))

# result is 24
# 1*2 = 2
# 2*3 = 6
# 6*4 = 24


# or

print(reduce(lambda x, y: x*y, n))
