def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(1, 2))