import functools


def dict_list_to_csv(func):
    @functools.wraps(func)
    def wrapped(*args):
        lst = func(*args)
        data = ''
        for dct in lst:
            for key in dct:
                data += str(key) + ',' + str(dct[key]) + ','
        data = data[:-1]
        return data
    return wrapped
