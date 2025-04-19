def outer (val):
    def inner ():
        return f'You returned {val}'
    return inner

def power_factory (exp):
    def power (x):
        return x ** exp
    return power

inner = outer (10)
print(inner.__closure__[0].cell_contents)
print(inner())

power = power_factory (3)
print (power (2))