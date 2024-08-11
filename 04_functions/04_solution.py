
def sum_all(*args):
    print(type(args))
    return sum(args)


print(sum_all(1, 2, 3, 4, 5))