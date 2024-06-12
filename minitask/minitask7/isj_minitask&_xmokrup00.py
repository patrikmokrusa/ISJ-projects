# minitask 7

def deprecated(fun):
    def inner(*args, **kwargs):
        print("Call to deprecated function: "+fun.__name__)
        print("with args:",args)
        print("with kwargs:",kwargs)

        rtn_val = fun(*args, **kwargs)
        print("returning:",rtn_val)
        return rtn_val
    return inner

@deprecated
def some_old_function(x, y):
    return x + y

some_old_function(1,y=2)

# should print:
# Call to deprecated function: some_old_function
# with args: (1,)
# with kwargs: {'y': 2}
# returning: 3 