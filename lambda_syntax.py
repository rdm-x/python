# -----------------------------------------------------------------------------


def multiply(x, y):
    return x*y

# or


multiply = lambda x, y: x*y

print(multiply(3, 2))

# -----------------------------------------------------------------------------

# Lamda funtion to multiply two given numbers


def compare(x, y):
    if x > y:
        return x
    else:
        return y

# or


compare = lamdba x, y: x if x > y else y

print(compare(4, 5)

